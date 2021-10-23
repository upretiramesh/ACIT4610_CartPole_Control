import gym
from train_test import train_model, test_model
import config

env = gym.make('CartPole-v0')
# Reset the max step --> default is 200
env._max_episode_steps = 2000

# define path to store best rule and history during training
model_path = './models/'
result_path = './result/'

print('###### Current Configuration ######')
print(f'Neighbours: {config.NEIGHBOURS}')
print(f'Encoding policy: {config.METHOD}')
print(f'Bins size: {config.BINS}')
print(f'Mutation rate: {config.MUTATION_RATE}')
print(f'Number of rules: {config.NUMBER_OF_RULES}')
print(f'Number of generations: {config.NUMBER_OF_GENERATIONS}')
print('#####################################\n')

# train the model
train_model(model_path, result_path, env)

# test the model
# test_model(model_path, env)