import numpy as np
import matplotlib.pyplot as plt
from helper.ambiente import Pontos
from helper.utils import distancia_rota, diminuir_pontos, simulate_points
from machineLearning.ambienteML import MazeEnv
from machineLearning.commom import cruz, setas, show_heatmap
import time
from curves import bSpline

alpha = 0.9  # taxa de aprendizado, ie, qual fração dos valores Q deve ser atualizada
gamma = 0.2  # fator de desconto, ie, algoritmo considera possíveis recompensas futuras
epsilon = 0.1  # probabilidade de escolher uma ação aleatória em vez da melhor ação
maxIt = 900

# TEM DECAIMENTO DE ALPHA??? 0.998

# alpha = 0.99  # taxa de aprendizado, ie, qual fração dos valores Q deve ser atualizada
# gamma = 0.5  # fator de desconto, ie, algoritmo considera possíveis recompensas futuras
# epsilon = 0.05  # probabilidade de escolher uma ação aleatória em vez da melhor ação
# maxIt = 900


def choose_action(state, Q, mx):
    action=0
    if np.random.rand() <= epsilon:
        action = np.random.randint(4)
    else:
        action = np.argmax(Q[state_index(state, mx)])
    return action

def history(mx, my, env, Q):
    history = []
    recompensas = []
    heatmap = np.zeros((mx, my))

    for indexx in range(maxIt): 
        # print(indexx)
        if indexx == maxIt - 1: print("Treinamento concluído") 
        state = env.reset()
        done = False
        rw = 0
        
        while not done:
            heatmap[state] += 1
            
            action = choose_action(state, Q, mx)
            # if np.random.rand() <= epsilon:
            #     action = np.random.randint(4)
            # else:
            #     action = np.argmax(Q[state_index(state, mx)])
            
            new_state, reward, done, info = env.step(action)
            # action2 = choose_action(new_state, Q, mx)
            # Sarsa
            # Q[state_index(state, mx), action] += alpha * (reward + gamma * Q[state_index(new_state, mx), action2] - Q[state_index(state, mx), action])
            rw += reward
            Q[state_index(state, mx), action] += alpha * (reward + gamma * np.max(Q[state_index(new_state, mx)]) - Q[state_index(state, mx), action])
            state = new_state
        
        recompensas.append(rw)
        history.append(info['time'])

    return heatmap, recompensas

def state_index(state, mx):
    return state[0] + mx * state[1]

def run(show=False, vmx=None, vmy=None, startx=None, starty=None, p1=None):
    start = time.time()
    p = Pontos()
    mx = p.limiar + 1
    my = p.limiar + 1

    # print("1")
    if startx == None:
        env = MazeEnv(mx, my, p.xs, p.ys, p.xt, p.yt, p.capaX, p.capaY, p.limiar)
    else:
        env = MazeEnv(mx, my, startx, starty, p.xt, p.yt, vmx, vmy, p.limiar)
    # print("2")
    # env.render()    
    env.reset()

    Q = np.random.rand(mx * my, 4)  # 4 acoes possiveis

    heatmap, recompensas = history(mx, my, env, Q)
    # show_heatmap(mx, my, heatmap, env)
    # cruz(mx, my, env, Q)
    # setas(mx, my, env, Q)

    state = env.reset()
    done = False

    while not done:
        # if np.random.rand() <= epsilon:
        #     action = np.random.randint(4)
        # else:
        #     action = np.argmax(Q[state_index(state, mx)])
        action = np.argmax(Q[state_index(state, mx)])
        
        new_state, _, done, _ = env.step(action)
        state = new_state

    plt1, px, py = env.render()
    
    xx, yy = diminuir_pontos(px, py, p.xobs, p.yobs)
    
    print(xx)
    
    curv = bSpline.B_spline(xx, yy)
    xnew, ynew = curv.get_curv()
    
    xxx, yyy = simulate_points(xnew[-1], p.xt, ynew[-1], p.yt)

    xnew = np.concatenate((xnew, xxx, [p.xt]), axis=0)
    ynew = np.concatenate((ynew, yyy, [p.yt]), axis=0)
    # plt.plot(xnew, ynew)
    # plt.show()
    
    # if show:    
    #     plt1.show()

    distancia = distancia_rota(px, py)
    
    # plt.plot(recompensas)
    # plt.show()

    return distancia, time.time()-start, xnew, ynew

if __name__ == "__main__":
    run()