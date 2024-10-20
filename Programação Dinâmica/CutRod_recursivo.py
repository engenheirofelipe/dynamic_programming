#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
from numpy import inf


## Funções - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
def cut_rod(p: int, n: int) -> int:
    """
Implementação do algoritmo Cut-Rod(p,n) da Seção 15.1 do livro
Introduction to Algorithms da página 363
    """

    ## assuminos que r_0 é zero, por isso, quando n == 0, então
    ## retornamos 0
    if n == 0:
        return 0

    ## inicializamos o valor máximo de revenda com -inf pois queremos
    ## oter o valor ótimo
    q = - inf

    ## encontrar, recursivamente, o valor máximo de revenda
    for i in range(n):
        q = max(q, p[i] + cut_rod(p, n -i -1))

    return q


## Script principal - - - - - - - - - - - - - - - - - - - - - - - - - #
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(f'Valor máximo de revenda: {cut_rod(p, len(p))}')
