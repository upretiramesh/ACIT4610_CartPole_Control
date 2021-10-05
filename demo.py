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


for gn in range(config.NUMBER_OF_GENERATIONS):
    for rn, rule in enumerate(rules):
        fitness = []
        for t in range(config.RULE_ITERATION):
            observation = env.reset()
            env.render()
            done = False
            fitness_count = 0
            while not done:
                encoded_observation = Encoder(observation, method=config.METHOD).cells
                ca = CellularAutomata(encoded_observation, rule, config.NEIGHBOURS, config.ITERATION_CA)
                observation, reward, done, info = env.step(ca.action)
                fitness_count += 1
            fitness.append(fitness_count)
        # update fitness value
        rule.fitness_value = min(fitness)
        print('Generation ', gn, 'Rule no ', rn, 'Fitness ',  min(fitness), max(fitness))
    # optimization
env.close()
