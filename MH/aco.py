import matplotlib.pyplot as plt
import numpy as np
from itertools import product
import time

from helper.ambiente import Pontos
from curves import bSpline
from helper.utils import distancia_rota, diminuir_pontos

# algorithm config
ALPHA = 1
BETA = 2.5
EVAPORATION = 0.2
ANTS = 5

# simulation config
ITERATIONS_CLEAN = 20
ITERATIONS_OBSTICLE = 20


class SimpleMap:
    dir = ((-1, 0),
           (0, 1),
           (1, 0),
           (0, -1))

    def __init__(self, map, xs, ys, xt, yt, heuristic=lambda y_s, x_s, y_t, x_t: 0):
        self.map = map
        self.hw = np.shape(map)
        self.h, self.w = self.hw
        self.p_map = np.ones(self.hw) * 0.1
        self.heuristic = heuristic
        self.start = (xs, ys)
        self.end = (xt, yt)

    def adj(self, y, x):
        ans = np.zeros(4)
        if y>0 and self.map[int(y-1)][int(x)]==0: # up
            ans[0] = 1
        if x<self.w-1 and self.map[int(y)][int(x+1)]==0: # right
            ans[1] = 1
        if y<self.h-1 and self.map[int(y+1)][int(x)]==0: # down
            ans[2] = 1
        if x>0 and self.map[int(y)][int(x-1)]==0: # left
            ans[3] = 1
        return ans

    def prob_numinator(self, dst_y, dst_x):
        return np.power(self.p_map[int(dst_y), int(dst_x)], ALPHA) +\
               np.power(self.heuristic(dst_y, dst_x), BETA) # pheromone-component^alpha + heuristic-component^beta

    def run(self, ants, iterations, show_p=0):
        # init path and path length
        best_len = np.inf
        best_path = None

        for i in range(iterations):
            # set start position
            paths = tuple(list() for l in range(ants))
            lengths = np.empty(ants)

            for m in range(ants):
                # a single ant walk
                paths[m].clear
                paths[m].append(self.start)
                lengths[m] = 0

                # walk until you've reached the end
                y, x = self.start
                while not (y == self.end[0] and x == self.end[1]):
                    # get probabilities for next step
                    prob = self.adj(y, x)
                    if y > 0:
                        prob[0] *= self.prob_numinator(y-1, x) # up
                    if x < self.w-1:
                        prob[1] *= self.prob_numinator(y, x+1) # right
                    if y < self.h-1:
                        prob[2] *= self.prob_numinator(y+1, x) # down
                    if x > 0:
                        prob[3] *= self.prob_numinator(y, x-1) # left

                    # normalize
                    prob /= np.sum(prob)

                    # save last step (fur heuristic 2)
                    last_y, last_x = y, x

                    # pick next step
                    c = np.random.choice(4, p=prob)
                    d_y, d_x = self.dir[c]
                    y += d_y
                    x += d_x

                    # save current path
                    paths[m].append((y, x))
                    lengths[m] += 1

                # update best path
                if lengths[m]<best_len:
                    best_len = lengths[m]
                    best_path = paths[m][:]

            # if show_p>0 and i%show_p==0:
            #     plt.imshow(self.p_map, interpolation="nearest")
            #     plt.show()

            # evaporate pheromones
            self.p_map *= (1 - EVAPORATION)

            # update new pheromones
            for m in range(ants):
                for y, x in paths[m]:
                    self.p_map[int(y), int(x)] += 1/lengths[m]

            print(i, best_len)
        return best_path

    def add_obstacles_global(self, obsx, obsy):
        for x, y in zip(obsx, obsy):
            self.map[int(x), int(y)]=1
            self.p_map[int(x), int(y)]=0
        # self.p_map = np.ones(self.hw) * 0.1
        # for o in obs:
        #     for y, x in product(range(o.ul_y, o.lr_y), range(o.ul_x, o.lr_x)):
        #         self.map[y, x] = 1
        #         self.p_map[y, x] = 0

    def add_obstacles_local(self, obs, max_dist=4):
        max_p = np.max(self.p_map)
        for o in obs:
            for y, x in product(range(self.h), range(self.w)):
                d = o.get_dist(y, x)
                if d == 0: # in obsticle
                    self.map[y, x] = 1
                    self.p_map[y, x] = 0
                elif d <= max_dist:
                    self.p_map[y, x] = max_p / 2 ** d


class Obstacle:
    def __init__(self, ul_y, ul_x, lr_y, lr_x):
        self.ul_y = ul_y
        self.ul_x = ul_x
        self.lr_y = lr_y
        self.lr_x = lr_x

    def get_dist(self, y, x):
        # case given point inside object
        if self.ul_y <= y <= self.lr_y and self.ul_x <= x <= self.lr_x:
            return 0

        # find reference y
        if self.ul_y <= y <= self.lr_y:
            ref_y = y
        else:
            ref_y = self.ul_y if abs(y-self.ul_y) < abs(y-self.lr_y) else self.lr_y

        # find reference x
        if self.ul_x <= x <= self.lr_x:
            ref_x = x
        else:
            ref_x = self.ul_x if abs(x-self.ul_x) < abs(x-self.lr_x) else self.lr_x

        # return distance to reference point = l1 norm
        return abs(y-ref_y) + abs(x-ref_x)


def display_path(map, path):
    d_map = np.array(map.map)
    obsx, obsy = [], []
    for indexx, element in enumerate(d_map):
        for indexy in range(len(element)):
            if d_map[indexx][indexy] == 1:
                obsx.append(indexx)
                obsy.append(indexy)

    xx, yy = [], []
    for x, y in path:
        xx.append(x)
        yy.append(y)

    # plt.imshow(d_map, interpolation="nearest", cmap="gray_r")
    plt.plot(obsx, obsy, ".k")
    plt.plot(xx, yy)
    plt.show()

def run(show=False, vmx=None, vmy=None, startx=None, starty=None):
    p = Pontos()

    raw_map = np.zeros((p.limiar+1, p.limiar+1))

    # Heuristica 1
    h1 = lambda y_d, x_d: y_d+x_d
    
    # # Heuristica 2
    # last_x, last_y = (0, 0)
    # h2 = lambda y_d, x_d: 1 if y_d == last_y and x_d == last_x else 0.5
    
    start = time.time()
    if startx == None:
        smap = SimpleMap(raw_map,xs=p.xs,ys=p.ys,xt=p.xt,yt=p.yt,heuristic=h1)
        smap.add_obstacles_global(p.xobs, p.yobs)
    else:
        smap = SimpleMap(raw_map,xs=startx,ys=starty,xt=p.xt,yt=p.yt,heuristic=h1)
        smap.add_obstacles_global(vmx, vmy)
    path = smap.run(ANTS, ITERATIONS_OBSTICLE, show_p=show)
    # display_path(smap, path)

    _, px, py = distancia_rota(path)

    a, b = diminuir_pontos(px, py, p.xobs, p.yobs)

    curv = bSpline.B_spline(a, b) if abs(startx - p.xs) < 5 and abs(starty - p.ys) < 5 else bSpline.B_spline(a[:-1], b[:-1]) 
    xnew, ynew = curv.get_curv()

    end = time.time() - start

    distancia2 = distancia_rota(xnew, ynew)    

    return distancia2, end, xnew, ynew
