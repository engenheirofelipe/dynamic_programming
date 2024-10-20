#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
from numpy import inf


## Funções - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
def cut_rod_iterativo(p: int, n: int) -> int:
    """
Implementação do algoritmo Bottom-Up-Cut-Rod(p,n) da Seção 15.1 do livro
Introduction to Algorithms da página 366
    """

    ## r é um array que irá armazenar os maiores valores de revenda de
    ## acordo com o tamanho dos subproblemas, ou seja, r[0] contém o
    ## maior valor de revenda para um bastão de comprimento 0,
    ## r[1] contém o maior valor de revenda para um bastão de
    ## comprimento 1 e assim por diante
    r = [None] * (n +1)
    r[0] = 0

    ## o índice j começa no 1, porque o índice 0 contém o caso
    ## base (r_0 = 0, um bastão de comprimento 0)
    for j in range(1, n+1):
        q = -inf

        ## o índice i vai até o valor j, pois j indice o tamanho do
        ## maior subproblema resolvido até o momento
        for i in range(j):
            ## esse print serve apenas para mostrar os tamanhos dos
            ## subproblemas
            ## print(f'i: {i} \t j-i-1: {j -i -1}')
            q = max(q, p[i] + r[j -i -1])

        ## esse print serve apenas para mostrar os tamanhos dos
        ## subproblemas
        ## print("")
        r[j] = q

    return r[n]


def cut_rod_estendido(p: int, n: int) -> tuple:
    """
Implementação do algoritmo Bottom-Up-Cut-Rod(p,n) da Seção 15.1 do livro
Introduction to Algorithms da página 366
    """

    ## r é um array que irá armazenar os maiores valores de revenda de
    ## acordo com o tamanho dos subproblemas, ou seja, r[0] contém o
    ## maior valor de revenda para um bastão de comprimento 0,
    ## r[1] contém o maior valor de revenda para um bastão de
    ## comprimento 1 e assim por diante
    r = [None] * (n +1)
    r[0] = 0

    ## o array s serve para guardar o tamanho da divisão que resulta
    ## no maior valor de revenda
    s = [None] * (n +1)

    ## o índice j começa no 1, porque o índice 0 contém o caso
    ## base (r_0 = 0, um bastão de comprimento 0)
    for j in range(1, n+1):
        q = -inf

        ## o índice i vai até o valor j, pois j indice o tamanho do
        ## maior subproblema resolvido até o momento
        for i in range(j):
            ## esse print serve apenas para mostrar os tamanhos dos
            ## subproblemas
            ## print(f'i: {i} \t j-i-1: {j -i -1}')
            if q < p[i] + r[j -i -1]:
                q = p[i] + r[j -i -1]
                ## guarda o tamanho da divisão que dera um valor de
                ## revenda maior do que a solução corrente
                s[j] = i +1

        ## esse print serve apenas para mostrar os tamanhos dos
        ## subproblemas
        ## print("")
        r[j] = q

    return r,s


def imprime_cut_rod(p: list, n: int) -> None:

    r, s = cut_rod_estendido(p, n)
    i = n
    print(f'Maior valor de revenda: {r[i]}')

    while i > 0:
        print(s[i], end=' ')
        i = i - s[i]

    print(end='\n')


## Script principal - - - - - - - - - - - - - - - - - - - - - - - - - #
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# print(f'Valor máximo de revenda: {cut_rod_iterativo(p, len(p))}')
imprime_cut_rod(p, len(p))
