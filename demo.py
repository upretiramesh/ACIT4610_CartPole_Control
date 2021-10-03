import gym
from encoder import Encoder
from cellular_automata import CellularAutomata
import config

ITERATION = 100
DECISION_LIMIT = ITERATION*4/2

env = gym.make('CartPole-v0')

for _ in range(5):
    observation = env.reset()
    for t in range(200):
        env.render()
        encode = Encoder(observation, method=config.METHOD)
        cells = encode.cells
        ca = CellularAutomata(cells, config.NEIGHBOURS, config.ITERATION_CA)
        observation, reward, done, info = env.step(ca.action)
        print('obs: ',observation, 'count: ', 'action: ', ca.action)
        if done:
            print('####### Finished ############')
            print("Episode finished after {} timesteps".format(t + 1))
            print('################################################3')
            break
env.close()
