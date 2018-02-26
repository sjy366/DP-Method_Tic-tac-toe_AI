import copy
from Tictactoe_Env import tictactoe
from Agent import AIagent_RL, AIagent_Base, Human_agent

env = tictactoe()
agent1 = Human_agent()
agent2 = AIagent_RL(restore=True)


def play():
    done = 0
    winner = 0
    env.reset()
    state = copy.copy(env.state)

    i = 0
    while not done:
        i += 1
        if i % 2 == 1:
            action = agent1.policy(state)
        else:
            action = agent2.policy(state)
        next_state, done, reward, winner = env.step(action)
        state = copy.copy(next_state)
        env.render()

    if winner == 0:
        print("Draw!")
    else:
        print("Winner is agent %d!" % winner)


if __name__ == "__main__":
    play()
