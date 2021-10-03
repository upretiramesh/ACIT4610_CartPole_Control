import gym
import pandas as pd
import numpy as np
from collections import defaultdict


env = gym.make('CartPole-v0')
env._max_episode_steps = 500
env.reset()


'''
Action:
0 : "push cart to the left" 
1 : "push cart to the right"
Observation:
{
cart position, cart velocity, pole angle, pole velocity
}
'''

# print('## observation high and low limit')
# print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)
#
# print('## action space ##')
# print(env.action_space)

game = defaultdict(list)

for i_episode in range(20):
    observation = env.reset()
    for t in range(1000):
        env.render()
        if observation[3] < -0.7003292:
            action = 0
        elif observation[3] > 0.7003292:
            action = 1
        elif observation[2] < -0.11003292:
            action = 0
        elif observation[2] > 0.11003292:
            action = 1
        else:
            action = env.action_space.sample()

        game['aa'].append(action)
        # print(observation, action)
        observation, reward, done, info = env.step(action)

        for x, y in zip(['cp', 'cv', 'pa', 'pv'], observation):
            game[x].append(y)

        if done:
            print('####### Finished ############')
            print("Episode finished after {} timesteps".format(t+1))
            print('################################################3')
            break
env.close()
#
df = pd.DataFrame(game)
df.astype(dtype=np.float64)


print('## describe ##')
# print(df.describe())

print('## correlation ##')
print(df.corr())

print('##################################')
print('CP: ', df.cp.min(), df.cp.max())
print('CV: ', df.cv.min(), df.cv.max())
print('PA: ', df.pa.min(), df.pa.max())
print('PV: ', df.pv.min(), df.pv.max())
print('#######################################')
