import numpy as np


class Model:
    def __init__(self, cells, current_rule, neighbours, iters, model):
        """
        :argument
        cells: current observation cells
        neighbours: number of neighbours
        iters: how many times you want to run CA before taking decision
        """

        self.cells = cells
        self.current_rule = current_rule
        self.neighbours = neighbours
        self.iterations = iters
        self.model = model
        self.action = None
        self.updates()

    def updates(self):
        n = len(self.cells)
        for _ in range(self.iterations):
            for idx in range(n):
                if self.model == 'CA':
                    self.cells[idx] = self.update_cell_CA(idx, n)
                else:
                    self.cells[idx] = self.update_cell_NX(idx)
        self.action = 1 if sum(self.cells) >= n / 2 else 0

    def update_cell_CA(self, i, n):
        low, high = -int(self.neighbours / 2), int(self.neighbours / 2) + 1
        match = []
        for j in range(low, high):
            match.append(self.cells[(i + j) % n])
        rule_ix = sum(2 ** (self.neighbours - (c_idx + 1)) for c_idx in range(self.neighbours) if match[c_idx] == 1)

        return self.current_rule.rule[rule_ix]

    def update_cell_NX(self, i):
        connected_nodes = np.where(self.current_rule.rule[i, :] == 1)
        match = []
        if len(connected_nodes) == 0:
            return self.cells[i]
        else:
            for idx in connected_nodes[0]:
                match.append(self.cells[idx])
            return 1 if sum(match) >= len(match)/2 else 0