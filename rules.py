import random
import config


class DefineRule:
    def __init__(self, idx=None, rules=None):
        self.n_neighbours = config.NEIGHBOURS
        self.fitness_value = random.randint(0, 50)
        self.rule = []
        self.rule_list = rules
        if self.rule_list:
            self.rule = self.rule_list
        else:
            self.create_new_rule(idx)

    def create_new_rule(self, idx):
        if idx == 0:
            for n in range(2 ** self.n_neighbours):
                binary_number = format(n, 'b')
                total = sum([int(i) for i in binary_number])
                self.rule.append(1 if total > int(self.n_neighbours / 2) else 0)
        elif idx == 1:
            for n in range(2 ** self.n_neighbours):
                binary_number = format(n, 'b')
                total = sum([int(i) for i in binary_number])
                self.rule.append(1 if total % 2 == 0 else 0)
        else:
            for n in range(2 ** self.n_neighbours):
                self.rule.append(random.randint(0, 1))


def Define_Rule(idx, n_neighbours):
    rule = []
    if idx == 0:
        for n in range(2 ** n_neighbours):
            binary_number = format(n, 'b')
            total = sum([int(i) for i in binary_number])
            rule.append(1 if total > int(n_neighbours / 2) else 0)
    elif idx == 1:
        for n in range(2 ** n_neighbours):
            binary_number = format(n, 'b')
            total = sum([int(i) for i in binary_number])
            rule.append(1 if total % 2 == 0 else 0)
    else:
        for n in range(2 ** n_neighbours):
            rule.append(random.randint(0, 1))

    # use last index to store fitness value
    rule.append(0)

    return rule
