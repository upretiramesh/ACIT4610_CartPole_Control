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

        if self.model == '2DCA':
            self.size = int(np.sqrt(len(self.cells)))
            self.cells = np.array(self.cells[:self.size**2]).reshape(self.size, self.size)
            self.updates_2D_CA()
        else:
            self.updates()

    def updates(self):
        n = len(self.cells)
        for _ in range(self.iterations):
            for idx in range(n):
                if self.model == '1DCA':
                    self.cells[idx] = self.update_cell_1DCA(idx, n)
                else:
                    self.cells[idx] = self.update_cell_NX(idx)
        self.action = 1 if sum(self.cells) >= n / 2 else 0

    def update_cell_1DCA(self, i, n):
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

    def updates_2D_CA(self):
        for _ in range(self.iterations):
            for dx in range(self.size):
                for dy in range(self.size):
                    self.cells[dx, dy] = self.update_cell_2DCA(dx, dy)
        self.action = 1 if np.sum(self.cells) >= (self.size*self.size) / 2 else 0

    def update_cell_2DCA(self, x, y):
        low, high = -int(self.neighbours / 2), int(self.neighbours / 2) + 1
        match = []
        for i in range(low, high):
            for j in range(low, high):
                match.append(self.cells[(x + i) % self.size, (y + j) % self.size])

        rule_ix = sum(2 ** (self.neighbours**2 - (c_idx + 1)) for c_idx in range(self.neighbours**2) if match[c_idx] == 1)

        return self.current_rule.rule[rule_ix]