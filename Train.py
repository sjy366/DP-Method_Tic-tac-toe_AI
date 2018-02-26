import copy
import itertools
from Tictactoe_Env import tictactoe, predict, ret_turn
from Agent import AIagent_RL, AIagent_Base
from Functions import is_finished, available_actions

verify_episode = 100
discount_factor = 0.9

env = tictactoe()
agent = AIagent_RL(restore=False)
agent_base = AIagent_Base()


def policy_evaluation(agent):
    theta = 1e-9

    while True:
        delta = 0.0

        state_list = itertools.product([0, 1, 2], repeat=9)
        for state in state_list:
            state = list(state)
            done, winner = is_finished(state)
            if not done:  # except for terminal state
                v = agent.value(state)

                action = agent.policy(state)
                next_state, reward = predict(state, action)
                agent.assign_value(state, reward + discount_factor * agent.value(next_state))

                delta = max([delta, abs(v - agent.value(state))])

        if delta < theta:
            break


def polcy_improvement(agent):
    policy_stable = True

    state_list = itertools.product([0, 1, 2], repeat=9)
    for state in state_list:
        state = list(state)
        done, winner = is_finished(state)
        if not done:  # except for terminal state
            available = available_actions(state)
            turn = ret_turn(state)

            old_action = agent.policy(state)

            max_value = -9999999
            min_value = 9999999
            if turn == 1:
                for action in available:
                    next_state, reward = predict(state, action)
                    value = reward + discount_factor * agent.value(next_state)
                    if value > max_value:
                        max_value = value
                        new_action = action
            else:
                for action in available:
                    next_state, reward = predict(state, action)
                    value = reward + discount_factor * agent.value(next_state)
                    if value < min_value:
                        min_value = value
                        new_action = action

            agent.assign_policy(state, new_action)

            if old_action != new_action:
                policy_stable = False

    if policy_stable:
        return True
    else:
        return False


def train():
    iteration = 0
    while True:
        iteration += 1

        # policy iteration
        policy_evaluation(agent)
        stop = polcy_improvement(agent)

        # verification stage
        win = lose = draw = 0
        for i in range(verify_episode):
            done = 0
            env.reset()
            state = copy.copy(env.state)

            winner = 0
            j = 0
            while not done:
                j += 1
                turn = copy.copy(env.turn)
                if (i + j) % 2 == 1:
                    action = agent.policy(state)
                else:
                    action = agent_base.policy(state, turn)
                next_state, done, reward, winner = env.step(action)
                state = copy.copy(next_state)

            if winner == 0:
                draw += 1
            elif (i + j) % 2 == 1:
                win += 1
            else:
                lose += 1
        win_rate = (win + draw) / verify_episode
        print("[Iteration %d] Win : %d Draw : %d Lose : %d Win_rate: %.2f" % (iteration, win, draw, lose, win_rate))
        agent.save()

        if stop:
            break


if __name__ == "__main__":
    train()
