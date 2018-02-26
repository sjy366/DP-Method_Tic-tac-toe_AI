import random
import itertools
import pickle
from Functions import is_finished, encode, available_actions


class AIagent_RL:
    def __init__(self, restore=False):
        self._value = dict()
        self._policy = dict()

        if not restore:
            self.init_value()
        else:
            self.restore()

    def init_value(self):
        state_list = itertools.product([0, 1, 2], repeat=9)

        for state in state_list:
            state = list(state)
            encoded = encode(state)
            done, winner = is_finished(state)
            if not done:
                self._value[encoded] = random.uniform(-0.5, 0.5)
                self._policy[encoded] = random.choice(available_actions(state))
            # terminal state value
            else:
                self._value[encoded] = 0

    def value(self, state):
        encoded = encode(state)
        return self._value[encoded]

    def assign_value(self, state, x):
        encoded = encode(state)
        self._value[encoded] = x

    def policy(self, state):
        encoded = encode(state)
        return self._policy[encoded]

    def assign_policy(self, state, x):
        encoded = encode(state)
        self._policy[encoded] = x

    def save(self):
        f = open("./data/save_value.dat", 'wb')
        pickle.dump(self._value, f)
        f = open("./data/save_policy.dat", 'wb')
        pickle.dump(self._policy, f)
        print("saved!")

    def restore(self):
        f = open("./data/save_value.dat", 'rb')
        self._value = pickle.load(f)
        f = open("./data/save_policy.dat", 'rb')
        self._policy = pickle.load(f)
        print("restored!")


class AIagent_Base:
    def policy(self, state, turn):
        available = available_actions(state)
        action_list = []

        for i in available:
            state[i] = turn
            done, winner = is_finished(state)
            state[i] = 0
            if done:
                action_list.append(i)
        if len(action_list) == 0:
            action_list = available

        return random.choice(action_list)


class Human_agent:
    def policy(self, state):
        available = available_actions(state)

        while True:
            ret = int(input("input [0 1 2 / 3 4 5 / 6 7 8] : "))
            if ret in available:
                break
        return ret
