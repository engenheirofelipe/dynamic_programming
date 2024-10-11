#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

# Elimina os elementos da esquerda pra direita. fila.popleft()

# Adiciona os elementos da direita pra esquerda. Ou seja no final da fila


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
from collections import deque
from typing import Any


## Implementação de funções - - - - - - - - - - - - - - - - - - - - - #
def cria_lista_adj(V: list[int],
                   E: list[tuple]) -> list[Any]:
    """
Função que cria a lista de adjacências para vértice do grafo.
    """

    lista_adj = [[] for _ in range(len(V))]

    for vertice in V:
        for aresta in E:
            if vertice in aresta:
                if vertice == aresta[0]:
                    lista_adj[vertice].append(aresta[1])
                else:
                    lista_adj[vertice].append(aresta[0])

    return lista_adj


def busca_em_largura(V: list[int],
                     lista_adj: list[any],
                     v: int) -> None:
    """
Implementação iterativa da busca em lagura num grafo.
    """

    ## lista que serve para indicar se um vértice foi visitado ou não
    ## 0 significa que o vértice não foi visitado
    visitados = [0] * len(V)

    ## cria a fila que contém os vértices a serem vistados
    ## insere o vértice na fila, pois iremos começar a busca
    ## a partir desse vértice
    F = deque([v])

    while len(F) != 0:
        vertice = F.popleft()
        print(f'Visitando o vértice {vertice}')

        ## aqui começa a etapa de explorar os vizinhos de um vértice
        ## explorar significa: examinar um vértice não visitado e
        ## inserí-lo na fila
        for vizinho in lista_adj[vertice]:
            if visitados[vizinho] == 0:
                print(f'O vértice {vizinho} não foi visitado! '
                      f'Insere o vértice {vizinho} na fila.')
                F.append(vizinho)
                ## 1 indica que o vértice está sendo explorado
                visitados[vizinho] = 1

        ## depois de todos vizinhos serem explorados, marca o vértice
        ## como visitado
        ## 2 significa que o vértice já foi explorado
        visitados[vertice] = 2
        print(f'Terminei de visitar o vértice {vertice}', end='\n\n')


## Script principal - - - - - - - - - - - - - - - - - - - - - - - - - #
## estrutura do grafo
V = [i for i in range(5)]
E = [(1,2), (1,0), (2,0), (3,0), (2,4)]

## constrói a lista dos vizinhos de cada vértice
lista_adj = cria_lista_adj(V, E)

## faz a busca em largura
busca_em_largura(V, lista_adj, 0)
