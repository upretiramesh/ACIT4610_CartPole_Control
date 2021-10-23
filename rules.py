import random
import config
import numpy as np


class DefineRule:
    def __init__(self, idx=None, rules=None):
        if config.MODEL == '2DCA':
            self.n_neighbours = config.NEIGHBOURS**2
        else:
            self.n_neighbours = config.NEIGHBOURS
        self.fitness_value = 0
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


class DefineRuleForNetwork:
    def __init__(self, mut_rule=None):
        """

        :type mut_rule: mutated 2d table >> numpy 2d


        """

        if config.METHOD in ['pole_angle_velocity', 'cart_position_velocity']:
            self.rule_size = 2 * config.BINS
        elif config.METHOD == 'cart_pole':
            self.rule_size = 4 * config.BINS
        else:
            print('choose of the of the encoder: pole_angle_velocity, cart_position_velocity, cart_pole')
            exit()

        self.fitness_value = 0
        self.rule = np.zeros((self.rule_size, self.rule_size))
        self.mut_rule = mut_rule

        try:
            if self.mut_rule:
                self.rule = self.mut_rule
            else:
                self.create_new_rule()
        except:
            self.rule = self.mut_rule

    def create_new_rule(self):
        for i in range(self.rule_size):
            self.rule[i, :] = random.choices([0, 1], weights=[0.7, 0.3], k=self.rule_size)
