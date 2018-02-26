import copy
from Functions import is_finished


# return who's turn
def ret_turn(state):
    one_count = two_count = 0

    for x in state:
        if x == 1:
            one_count += 1
        elif x == 2:
            two_count += 1
    if one_count > two_count:
        turn = 2
    else:
        turn = 1

    return turn


# predict (next_state, reward)
def predict(state, action):
    next_state = copy.copy(state)
    turn = ret_turn(state)

    next_state[action] = turn
    done, winner = is_finished(next_state)

    reward = 0
    if done and winner == 1: reward = 1
    if done and winner == 2: reward = -1
    if done and winner == 0: reward = 0

    return next_state, reward


# 'O' : 1, 'X' : 2
class tictactoe():
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turn = 1

    def step(self, action):
        self.state[action] = self.turn
        self.turn = self.turn % 2 + 1
        done, winner = is_finished(self.state)
        reward = 0
        if done and winner == 1: reward = 1
        if done and winner == 2: reward = -1
        if done and winner == 0: reward = 0

        return self.state, done, reward, winner

    def reset(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turn = 1

    def render(self):
        print('------------------------------------------')
        for i in range(3):
            print('|', end='')
            for j in range(3):
                if self.state[3 * i + j] == 0:
                    print(' |', end='')
                elif self.state[3 * i + j] == 1:
                    print('O|', end='')
                elif self.state[3 * i + j] == 2:
                    print('X|', end='')
            print()
        print('------------------------------------------')
