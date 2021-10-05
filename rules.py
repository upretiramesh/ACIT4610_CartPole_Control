import random
import config


class DefineRule:
    def __init__(self, idx):
        self.n_neighbours = config.NEIGHBOURS
        self.fitness_value = 0
        self.rule = []
        if idx == 0:
            for n in range(2**self.n_neighbours):
                binary_number = format(n, 'b')
                total = sum([int(i) for i in binary_number])
                self.rule.append(1 if total > int(self.n_neighbours/2) else 0)
        elif idx == 1:
            for n in range(2**self.n_neighbours):
                binary_number = format(n, 'b')
                total = sum([int(i) for i in binary_number])
                self.rule.append(1 if total%2 == 0 else 0)
        else:
            for n in range(2 ** self.n_neighbours):
                self.rule.append(random.randint(0,1))