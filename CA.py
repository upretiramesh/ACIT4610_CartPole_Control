import numpy as np
import pandas as pd
import gym


class Create2DGrid:
    """
    Define Two Dimensional Cellular Automaton Environment
    """

    def __init__(self, binss):
        self.env = gym.make('CartPole-v0')
        self.high = self.env.observation_space.high
        self.low = self.env.observation_space.low
        self.grid_size = int(np.sqrt(binss))
        self.binss = self.grid_size ** 2
        self.grid = np.zeros((self.grid_size * 2, self.grid_size * 2))

        self.grid[0:self.grid_size, 0:self.grid_size] = np.array(
            pd.cut([self.high[0], self.low[0]], bins=self.binss + 1,
                   retbins=True)[1][1:-1]).reshape(self.grid_size, self.grid_size)
        self.grid[0:self.grid_size, self.grid_size:] = np.array(pd.cut([self.high[1], self.low[1]], bins=self.binss + 1,
                                                                       retbins=True)[1][1:-1]).reshape(self.grid_size,
                                                                                                       self.grid_size)
        self.grid[self.grid_size:, 0:self.grid_size] = np.array(pd.cut([self.high[2], self.low[3]], bins=self.binss + 1,
                                                                       retbins=True)[1][1:-1]).reshape(self.grid_size,
                                                                                                       self.grid_size)
        self.grid[self.grid_size:, self.grid_size:] = np.array(pd.cut([self.high[0], self.low[0]], bins=self.binss + 1,
                                                                      retbins=True)[1][1:-1]).reshape(self.grid_size,
                                                                                                      self.grid_size)

    def find_closet_observation_index(self, obs):
        """
        :param obs: observation value getting from Gym Environment
        :return: the index(x,y) which is closet to the observation value
        eg:
        """

        cart_position = obs[0]
        cart_velocity = obs[1]
        pole_angle = obs[2]
        pole_velocity = obs[3]

        cart_position_idx = np.digitize([cart_position],
                                        np.array(self.grid[:self.grid_size, :self.grid_size]).reshape())
        cp_idx = int(cart_position_idx / self.grid_size)
        cp_idy = cart_position_idx % self.grid_size

        cart_velocity_idx = np.digitize([cart_velocity],
                                        np.array(self.grid[:self.grid_size, self.grid_size:]).reshape())
        cv_idx = int(cart_velocity_idx / self.grid_size)
        cv_idy = cart_velocity_idx % self.grid_size

        pole_angle_idx = np.digitize([pole_angle], np.array(self.grid[self.grid_size:, :self.grid_size]).reshape())
        pa_idx = int(pole_angle_idx / self.grid_size)
        pa_idy = pole_angle_idx % self.grid_size

        pole_velocity_idx = np.digitize([pole_velocity],
                                        np.array(self.grid[self.grid_size:, self.grid_size:]).reshape())
        pv_idx = int(pole_velocity_idx / self.grid_size)
        pv_idy = pole_velocity_idx % self.grid_size


grid = CreateGrid(111)
# print(grid.grid_size)
# print(grid.binss)
# print(grid.high)
# print(grid.grid)

# for i in range(10):
#     grid.grid[:i, 0:10] = grid.grid[:i, 0:10] - np.array(0.2)

# plt.imshow(grid.grid, cmap='hot')
# plt.show()
