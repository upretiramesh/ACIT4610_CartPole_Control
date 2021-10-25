import random
from itertools import combinations
from rules import DefineRule, DefineRuleForNetwork
import config


def Optimization(lst_rules, best_parents, model):
    """

    :param best_parents: number of parents selected for mutation >> int
    :param model: type of model >> string
    :param lst_rules: list of rules with updated fitness values >> list

    :return new updated rules >> list
    """
    ruleId_fitness = {}

    # sort the rules based on fitness value
    for id, rule in enumerate(lst_rules):
        ruleId_fitness[id] = rule.fitness_value
    ruleId_fitness = sorted(ruleId_fitness.items(), key=lambda kv: kv[1], reverse=True)

    parents = [lst_rules[rule[0]] for rule in ruleId_fitness][:best_parents]

    if 'CA' in model:
        if config.MUTATION_TYPE == 'RM':
            return ca_rule_mutation(parents, len(lst_rules), best_parents)
        else:
            return ca_rule_crossover(parents, len(lst_rules), best_parents)
    elif model == 'NX':
        # crossover feature is not implemented for network model
        return network_rule_mutation(parents, len(lst_rules), best_parents)


def ca_rule_mutation(parents, total_rule, best_parents):
    new_rules = []
    for rule in parents:
        new_rules.append(DefineRule(rules=rule.rule))
        for i in range(int((total_rule - best_parents) / best_parents)):
            updated_rule = []
            for idx, val in enumerate(rule.rule):
                if random.random() <= config.MUTATION_RATE:
                    updated_rule.append(1 if val == 0 else 0)
                else:
                    updated_rule.append(val)
            new_rules.append(DefineRule(rules=updated_rule))

    return new_rules


def network_rule_mutation(parents, total_rule, best_parents):
    new_rules = []
    for rule in parents:
        new_rules.append(DefineRuleForNetwork(mut_rule=rule.rule))
        for i in range(int((total_rule - best_parents) / best_parents)):
            updated_rule = rule.rule
            for dx in range(updated_rule.shape[0]):
                for dy in range(updated_rule.shape[0]):
                    if random.random() <= config.MUTATION_RATE:
                        updated_rule[dx, dy] = 1 if updated_rule[dx, dy] == 0 else 0
            new_rules.append(DefineRuleForNetwork(mut_rule=updated_rule))

    return new_rules


def ca_rule_crossover(parents, total_rule, best_parents):

    # keep the best parents as it is --> reproduction
    reproduction_rules = []
    for rule in parents:
        reproduction_rules.append(DefineRule(rules=rule.rule))

    # cross over between parents to create child, each time 25% of gens are cross over
    cross_rules = []
    for p1, p2 in list(combinations(parents, 2)):
        start = 0
        for per in [0.25, 0.50, 0.75, 1]:
            rule1 = p1.rule
            rule2 = p2.rule
            end = int(len(rule1) * per)

            # apply mutation if both rules have same value in crossover
            if rule1[start:end] == rule2[start:end]:
                for mut_rule in [rule1, rule2]:
                    updated_rule = []
                    for val in mut_rule:
                        if random.random() <= config.MUTATION_RATE:
                            updated_rule.append(1 if val == 0 else 0)
                        else:
                            updated_rule.append(val)
                    cross_rules.append(DefineRule(rules=updated_rule))
            else:
                rule1[start:end], rule2[start:end] = rule2[start:end], rule1[start:end]
                cross_rules.append(DefineRule(rules=rule1))
                cross_rules.append(DefineRule(rules=rule2))
            start = end

    # if total number of rules are not created, apply the mutation to crossover child
    mutated_rules = []
    if total_rule > len(cross_rules) + best_parents:
        for i in range(total_rule - best_parents - len(cross_rules)):
            updated_rule = []
            idx = random.randint(0, len(cross_rules) - 1)
            for val in cross_rules[idx].rule:
                if random.random() <= config.MUTATION_RATE:
                    updated_rule.append(1 if val == 0 else 0)
                else:
                    updated_rule.append(val)
            mutated_rules.append(DefineRule(rules=updated_rule))

    return reproduction_rules + cross_rules + mutated_rules
