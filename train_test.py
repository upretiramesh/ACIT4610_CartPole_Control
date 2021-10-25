import time
import os
from tqdm import tqdm
import pickle
import numpy as np
import pandas as pd
from encoder import Encoder
from model import Model
from rules import DefineRule, DefineRuleForNetwork
from optimization import Optimization
import config


def train_model(mPath, rPath, env):
    # create folder to store best rule if folder does not exists
    if not os.path.exists(mPath):
        os.mkdir(mPath)
    else:
        for file in os.listdir(mPath):
            os.remove(mPath + file)

    # Creates rules
    rules = []
    for n in range(config.NUMBER_OF_RULES):
        if 'CA' in config.MODEL:
            rule = DefineRule(n)
            rules.append(rule)
        elif config.MODEL == 'NX':
            rule = DefineRuleForNetwork()
            rules.append(rule)
        else:
            print('Choose correct model name: CA or NX')
            exit()

    performance = []
    best_fitness = 0
    best_fitness_min = 0
    best_fitness_max = 0

    for gn in tqdm(range(config.NUMBER_OF_GENERATIONS), desc='Training in Process'):
        for rule in rules:
            start = time.perf_counter()
            fitness = []
            for t in range(config.RULE_ITERATION):
                observation = env.reset()
                # env.render()
                # time.sleep(0.05)
                done = False
                fitness_count = 0
                while not done:
                    encoded_observation = Encoder(observation, method=config.METHOD).cells
                    ca = Model(encoded_observation, rule, config.NEIGHBOURS, config.ITERATION_CA, config.MODEL)
                    observation, reward, done, info = env.step(ca.action)
                    fitness_count += 1
                fitness.append(fitness_count)

            # update fitness value
            fitness_value = np.mean(fitness)
            rule.fitness_value = fitness_value

            # calculate rule number
            if 'CA' in config.MODEL:
                rn = sum(2 ** (len(rule.rule) - (c_idx + 1)) for c_idx in range(len(rule.rule)) if rule.rule[c_idx] == 1)

            # save best rule so far based on highest average fitness
            if fitness_value > best_fitness:
                outfile = open(mPath + 'best_rule_train_on_avg', 'wb')
                pickle.dump(rule, outfile)
                best_fitness = fitness_value
                outfile.close()

            # save best rule so far based on highest minimum fitness
            if np.min(fitness) > best_fitness_min:
                outfile = open(mPath + 'best_rule_train_on_min', 'wb')
                pickle.dump(rule, outfile)
                best_fitness_min = np.min(fitness)
                outfile.close()

            # save best rule so far based on highest maximum fitness
            if np.max(fitness) > best_fitness_max:
                outfile = open(mPath + 'best_rule_train_on_max', 'wb')
                pickle.dump(rule, outfile)
                best_fitness_max = np.max(fitness)
                outfile.close()

            end = time.perf_counter()
            if 'CA' in config.MODEL:
                performance.append({'model':config.MODEL, 'generation': gn, 'rule': rn, 'min': min(fitness), 'avg': np.mean(fitness),
                                'max': max(fitness), 'neighbour': config.NEIGHBOURS,
                                'ca_size': len(encoded_observation), 'time': end - start})
            else:
                performance.append({'model':config.MODEL, 'generation': gn, 'min': min(fitness), 'avg': np.mean(fitness),
                                    'max': max(fitness), 'ca_size': len(encoded_observation), 'time': end - start})
        # optimization
        rules = Optimization(rules, config.PARENTS, config.MODEL)
    train_history = pd.DataFrame(performance)

    # create folder to store training history if not exists
    if not os.path.exists(rPath):
        os.mkdir(rPath)

    # save training history
    train_history.to_csv(rPath +
                         'performance_m:{}_en:{}_mr:{}_p:{}_n:{}_bin:{}_ca:{}.csv'.format(config.MODEL, config.METHOD, config.MUTATION_RATE,
                                                                         config.PARENTS, config.NEIGHBOURS, config.BINS,
                                                                         len(encoded_observation)), index=False)


def test_model(mPath, env):
    # load the saved rules
    for path in os.listdir(mPath):
        openfile = open(mPath + path, 'rb')
        rule = pickle.load(openfile)

        observation = env.reset()
        done = False
        fitness_count = 0
        while not done:
            env.render()
            time.sleep(0.01)
            encoded_observation = Encoder(observation, method=config.METHOD).cells
            ca = Model(encoded_observation, rule, config.NEIGHBOURS, config.ITERATION_CA, config.MODEL)
            observation, reward, done, info = env.step(ca.action)
            fitness_count += 1

        print(f'################ {path} #################')
        print('Fitness value of test: ', fitness_count)
        print('############################################\n\n')
