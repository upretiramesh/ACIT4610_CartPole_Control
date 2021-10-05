import config


class CellularAutomata:
    def __init__(self, cells, current_rule, neighbours, iters):
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
        self.action = None
        self.updates()

    def updates(self):
        n = len(self.cells)
        for _ in range(config.ITERATION_CA):
            for idx in range(n):
                self.cells[idx] = self.update_cell(idx, n)

        self.action = 1 if sum(self.cells) >= n/2 else 0

    def update_cell(self, i, n):
        low, high = -int(self.neighbours / 2), int(self.neighbours / 2) + 1
        match = []
        for j in range(low, high):
            match.append(self.cells[(i+j)%n])
        rule_ix = sum(2**(self.neighbours-(c_idx+1)) for c_idx in range(self.neighbours) if match[c_idx]==1)

        return self.current_rule.rule[rule_ix]