import numpy as np
import matplotlib.pyplot as plt
import machineLearning.mazegen

class MazeEnv(object):
    label_to_action = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
    action_to_label = {0: 'up', 1: 'down', 2: 'left', 3: 'right'}
    observation_types = ['player_position', 'image']

    def __init__(self, mx=10, my=10, xs=1, ys=1, xt=9, yt=9, ox=[], oy=[], limiar=100, max_reward_treasure=100., reward_wall=-1., observation_type='player_position', new_maze_on_reset=False):
        self.mx = mx
        self.my = my
        self.max_reward_treasure = max_reward_treasure
        self.reward_wall = reward_wall
        if observation_type not in self.observation_types:
            raise ValueError('observation_type not recognized')
        self.observation_type = observation_type
        self.new_maze_on_reset = new_maze_on_reset
        self.xs = xs
        self.ys = ys
        self.xt = xt
        self.yt = yt
        self.ox = ox
        self.oy = oy
        self.limiar = limiar
        o = []
        for i, j in zip(self.ox, self.oy):
            o.append([i, j])
        self.obs = o
        # print("3")
        self._set_up_maze()
        # print("4")
        self.reset()

    def _set_up_maze(self):
        self.maze = machineLearning.mazegen.make_maze(self.mx, self.my, self.ox, self.oy, self.xs, self.ys, self.xt, self.yt, self.obs, self.limiar)
        # plt.imshow(self.maze.T, interpolation='none', origin='lower', cmap='Greys')
        # plt.show()
        self.treasure = (int(self.xt), int(self.yt))
        # while self.treasure == (self.xt, self.yt) or self.maze[self.treasure] == 1:
        #     self.treasure = (np.random.randint(self.mx), np.random.randint(self.my))

    def reset(self):
        if self.new_maze_on_reset:
            self._set_up_maze()
        self.player = [self.xs, self.ys]
        self.time = 0
        self.trajectory_x = []
        self.trajectory_y = []
        self.trajectory_x.append(self.player[0])
        self.trajectory_y.append(self.player[1])
        return self._generate_observation()

    def step(self, action):
        self.time += 1
        new_player = list(self.player)

        if action == self.label_to_action['up']:
            new_player[1] += 1
        elif action == self.label_to_action['down']:
            new_player[1] -= 1
        elif action == self.label_to_action['left']:
            new_player[0] -= 1
        elif action == self.label_to_action['right']:
            new_player[0] += 1

        if new_player[0] >= 0 and new_player[1] >= 0 and new_player[0] < self.mx and new_player[1] < self.my and self.maze[tuple(new_player)] == 0:
            self.player = new_player
            reached_treasure = (tuple(self.player) == self.treasure)
            reward = self.max_reward_treasure * reached_treasure / self.time

            self.trajectory_x.append(self.player[0])
            self.trajectory_y.append(self.player[1])
        else:
            reached_treasure = False
            reward = self.reward_wall

        return self._generate_observation(), reward, reached_treasure, {'time': self.time, 'trajectory_x': self.trajectory_x, 'trajectory_y': self.trajectory_y, 'player_position': tuple(self.player), 'treasure_position': self.treasure}

    # plt.ion()
    # fig = plt.figure()

    def _generate_observation(self):
        self.player[0] = int(self.player[0])
        self.player[1] = int(self.player[1])
        return tuple(self.player)

    def render(self):
        # plt.figure(figsize=(10, 5))
        # plt.imshow(self.maze.T, interpolation='none', origin='lower', cmap='Greys')
        # plt.plot(self.ox, self.oy, ".k")
        # plt.plot(self.trajectory_x, self.trajectory_y, 'r')
        # plt.plot(self.treasure[0], self.treasure[1], 'y*', mec='none', markersize=17)
        # plt.plot(self.player[0], self.player[1], 'ro', mec='none', markersize=8)
        # plt.xlim(-0.5, self.mx - 0.5)
        # plt.ylim(-0.5, self.my - 0.5)
        # return plt, self.trajectory_x, self.trajectory_y
        return 0, self.trajectory_x, self.trajectory_y