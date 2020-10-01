import numpy as np
import matplotlib.pyplot as plt
import random

# alfa: probabilidade de ter arvore na colina
# beta: probabilidade de n ter arvore na floresta

def createClareira(cx, cy, tam, env, alfa=0.85):
    d3 = int(np.ceil(tam/3))
    inc = 1

    for k in range(d3):
        for i in range(cx-tam+1, cx+tam):
            if random.random() < alfa: env[i][cy+k] = 0
            if random.random() < alfa: env[i][cy-k] = 0

        for i in range(cy-tam+1, cy+tam):
            if random.random() < alfa: env[cx+k][i] = 0
            if random.random() < alfa: env[cx-k][i] = 0

    while d3 < tam-3:
        for i in range(d3,d3+2):
            for k in range(cx-tam+inc+1, cx+tam-inc):
                if random.random() < alfa: env[k][cy+i] = 0
                if random.random() < alfa: env[k][cy-i] = 0

        for i in range(d3,d3+2):
            for k in range(cy-tam+inc+1, cy+tam-inc):
                if random.random() < alfa: env[cx+i][k] = 0
                if random.random() < alfa: env[cx-i][k] = 0
        d3 += 2
        inc += 1
    
    return env

# size1, size2 = 110, 120
# alfa = 0.8
# beta = 0.15
# matriz = np.ones((size1, size2))


# matriz[i][j] = [[0 for i in range(size1)] for j in range(size2) if random.random() < beta]

# # for i in range(size1):
# #     for j in range(size2):
# #         if random.random() < beta: matriz[i][j] = 0

# matriz = createClareira(20, 20, 10, matriz, alfa)
# matriz = createClareira(30, 85, 20, matriz, alfa)
# matriz = createClareira(80, 40, 25, matriz, alfa)


# camX, camY = [], []

# plt.grid
# plt.imshow(matriz)
# plt.show()

