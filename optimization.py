import random
from rules import DefineRule
import config


def Mutation(lst_rules, best_parents):
    """

    :param best_parents: number of parents used for optimization
    :type lst_rules: list of object rules
    """
    ruleId_fitness = {}

    # sort the rules based on fitness value
    for id, rule in enumerate(lst_rules):
        ruleId_fitness[id] = rule.fitness_value
    ruleId_fitness = sorted(ruleId_fitness.items(), key=lambda kv:kv[1], reverse=True)

    parents = [lst_rules[rule[0]] for rule in ruleId_fitness][:best_parents]
    new_rules = []

    for rule in parents:
        new_rules.append(DefineRule(rules=rule.rule))
        for i in range(int((len(lst_rules)-best_parents)/best_parents)):
            updated_rule = []
            for idx, val in enumerate(rule.rule):
                if random.random() <= config.MUTATION_RATE:
                    updated_rule.append(1 if val == 0 else 0)
                else:
                    updated_rule.append(val)
            new_rules.append(DefineRule(rules=updated_rule))

    return new_rules


def Crossover():
    pass
