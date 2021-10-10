import time
import numpy as np
import pandas as pd
import gym
from encoder import Encoder
from cellular_automata import CellularAutomata
from rules import DefineRule
from optimization import Mutation
import config


env = gym.make('CartPole-v0')
# Reset the max step --> default is 200
env._max_episode_steps = 1000

# Creates rules
rules = []
for n in range(config.NUMBER_OF_RULES):
    rule = DefineRule(n)
    rules.append(rule)

performance = []

for gn in range(config.NUMBER_OF_GENERATIONS):
    for rule in rules:
        fitness = []
        for t in range(config.RULE_ITERATION):
            observation = env.reset()
            # env.render()
            # time.sleep(0.05)
            done = False
            fitness_count = 0
            while not done:
                encoded_observation = Encoder(observation, method=config.METHOD).cells
                ca = CellularAutomata(encoded_observation, rule, config.NEIGHBOURS, config.ITERATION_CA)
                observation, reward, done, info = env.step(ca.action)
                fitness_count += 1
            fitness.append(fitness_count)
        # update fitness value
        rule.fitness_value = min(fitness)  # np.mean(fitness)
        rn = sum(2 ** (len(rule.rule) - (c_idx + 1)) for c_idx in range(len(rule.rule)) if rule.rule[c_idx] == 1)
        # print(rule.rule)
        # print('Generation ', gn, 'Rule no ', rn, 'Fitness ',  min(fitness), max(fitness), np.mean(fitness))
        print(f'{gn} generation complete')
        performance.append({'generation':gn, 'rule':rn, 'min':min(fitness), 'avg':np.mean(fitness),
                            'max':max(fitness),'neighbour':config.NEIGHBOURS, 'ca_size':len(rule.rule)})
    # optimization
    rules = Mutation(rules, config.PARENTS)
df = pd.DataFrame(performance)
df.to_csv('performance_1. sv', index=False)
env.close()
