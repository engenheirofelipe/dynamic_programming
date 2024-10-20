#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
from numpy import inf


## Funções - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
def cut_rod_memoizado(p: int, n: int) -> int:
    """
Implementação do algoritmo Memoizado-Cut-Rod(p,n, r) da Seção 15.1
do livro Introduction to Algorithms da página 365
    """

    ## o array r irá armazenar os valores de revenda já calculados
    ## criamos um array com n+1 elementos, pois queremos salvar os
    ## casos base (um para cada tamanho)
    r = [-inf] * (n +1)
    return cut_rod_memoizado_aux(p, n, r)


def cut_rod_memoizado_aux(p, n, r):
    """
Implementação do algoritmo Memoizado-Cut-Rod-Aux(p,n, r) da Seção 15.1
do livro Introduction to Algorithms da página 365
    """

    ## caso o valor de revenda já tenha sido calculado, então retorna
    ## o valor de r[n] e não o computa novamente
    if r[n] >= 0:
        return r[n]

    ## caso base: valor de revenda de um bastão de comprimento 0 é 0
    if n == 0:
        q = 0

    ## computa recursivamente o melhor valor de revenda
    else:
        q = - inf
        for i in range(n):
            q = max(q, p[i] + cut_rod_memoizado_aux(p, n-i -1, r))

    r[n] = q
    return q


## Script principal - - - - - - - - - - - - - - - - - - - - - - - - - #
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(f'Valor máximo de revenda: {cut_rod_memoizado(p, len(p))}')
