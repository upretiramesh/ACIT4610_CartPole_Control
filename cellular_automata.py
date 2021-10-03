class CellularAutomata:
    def __init__(self, cells, neighbours, iters):
        """
        :argument
        cells: current observation cells
        neighbours: number of neighbours
        iters: how many times you want to run CA before taking decision
        """

        self.cells = cells
        self.neighbours = neighbours
        self.iterations = iters
        self.action = None
        self.run()

    def run(self):
        low, high = -int(self.neighbours / 2), int(self.neighbours / 2) + 1
        n = len(self.cells)
        for idx in range(n):
            self.cells[idx] = 1 if sum(self.cells[(idx + low) % n:(idx + high) % n])>1 else 0

        self.action = 1 if sum(self.cells) >= n/2 else 0
