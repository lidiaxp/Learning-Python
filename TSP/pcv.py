#!/usr/bin/env python3
from sys import maxsize
from itertools import permutations
import string
import random
import time
import math

class ponto:
    def __init__(self, nome, coordenadas):
        self.nome = nome
        self.coordenadas = coordenadas
        self.descricao = '{} - {}'.format(nome, coordenadas)

class ContinueI(Exception):
            pass

continue_i = ContinueI()

# Cria lista aleatória de pontos
def cria_pontos(qtd_pontos):
    pontos = []
    x = [0.75, 7, 3, 4, 6, 7]
    y = [0.5, 0.5, 1, 3, 2, 7]
    nome_ponto = 0
    for indice in range(len(x)):
        novo_ponto = ponto(
            string.ascii_uppercase[nome_ponto],
            (x[indice], y[indice])
        )
        nome_ponto += 1
        pontos.append(novo_ponto)
        print(novo_ponto.descricao)

    return pontos

# Calcula a distancia entre 2 pontos
def distancia(ponto1,ponto2):
    return math.sqrt((ponto2.coordenadas[0] - ponto1.coordenadas[0])**2 + (ponto2.coordenadas[1] - ponto1.coordenadas[1])**2)

# Troca indice por nome do ponto para exibição
def processa_menor_caminho(menor_caminho):
    caminho = []
    for ponto in menor_caminho:
        caminho.append(pontos[ponto].nome)
    return caminho

def PCV(pontos, ponto_inicial):

    def igual_ponto_inicial(ponto):
        return ponto != ponto_inicial

    # Guarda todas as pontos menos a inicial
    pontos_sem_inicial = list(filter(igual_ponto_inicial , range(len(pontos))))

    # Cria todos os possíveis caminhos sem o ponto inicial
    caminhos = list(permutations(pontos_sem_inicial))

    print('\nCaminhos possíveis: {}'.format(len(caminhos)))

    # Inicia o peso do menor caminho com um valor muito alto
    peso_menor_caminho = maxsize

    # Calcula o custo de cada caminho
    for caminho in caminhos:
        # Armazena o valor do caminho atual
        peso_caminho_atual = 0

        # Calcula o custo do caminho atual
        ponto_atual = ponto_inicial

        try:
            for ponto in caminho:
                peso_caminho_atual += distancia(pontos[ponto_atual], pontos[ponto])
                if peso_caminho_atual > peso_menor_caminho:
                    raise continue_i
                ponto_atual = ponto
        except ContinueI:
            continue
        
        peso_caminho_atual += distancia(pontos[ponto_atual], pontos[ponto_inicial])

        # Atualiza o menor caminho
        if (peso_caminho_atual < peso_menor_caminho):
            peso_menor_caminho = peso_caminho_atual
            menor_caminho = list(caminho)

    menor_caminho.insert(0, ponto_inicial)
    menor_caminho.append(ponto_inicial)
    # Troca os indices pelos nomes dos pontos
    menor_caminho = processa_menor_caminho(menor_caminho)

    return [menor_caminho, peso_menor_caminho]

if __name__ == "__main__":

    while True:
        qtd_pontos = 1 # int(input('Digite a quantidade de pontos que deseja (ou 0 para sair): '))

        if (qtd_pontos > 0):
            pontos = cria_pontos(qtd_pontos)

            ponto_inicial = "A" # input('Digite o ponto inicial:').upper()

            for indice in range(qtd_pontos):
                if (pontos[indice].nome == ponto_inicial):
                    ponto_inicial = indice
                    break

            if (not isinstance(ponto_inicial, int)):
                continue

            inicio = time.time()

            resultado = PCV(pontos, ponto_inicial)

            fim = time.time()

            print('Caminho mais curto: {}\nDistância: {:.2f}'.format(resultado[0], resultado[1]))
            print('Tempo de execução(em segundos): {}\n\n'.format((fim - inicio)))
            break
        else:
            break