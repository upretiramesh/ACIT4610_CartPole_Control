import random
from rules import DefineRule, DefineRuleForNetwork
import config


def Mutation(lst_rules, best_parents, model):
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
        return ca_rule_mutation(parents, len(lst_rules), best_parents)
    elif model == 'NX':
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
