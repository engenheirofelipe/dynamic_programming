#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Impotação de módulos - - - - - - - - - - - - - - - - - - - - - - - #
import typing
from collections import deque


## Implementação de funções - - - - - - - - - - - - - - - - - - - - - #
def verifica_delimitadores(expressao: str) -> bool:
    """
Recebe uma expressão e retorna True se a expressão foi escrita de forma
correta, do contrário, retorna False.
    """

    ## cria os delimitadores que abrem e fecham uma expressão
    delim_abre = '({['
    delim_fecha = ')}]'

    ## cria a pilha que irá armazenar os delimitadores que abrem uma
    ## expressão
    P = deque()

    for letra in expressao:
        ## empilha os delimitadores que abrem uma expressão
        if letra in delim_abre:
            P.append(letra)

        ## parte que verifica se para uma delimitador que abre tem
        ## um que fecha
        elif letra in delim_fecha:
            ## se a pilha está vazia, isso signfica que está faltando um
            ## delimitador que abre
            if len(P) == 0:
                return False

            ## se os delimitadores não são compatíveis, ( ), [ ], ou
            ## { }, então a expressão não está escrita da forma correta
            if delim_fecha.index(letra) != delim_abre.index(P.pop()):
                return False

    ## duas situações podem ocorrer ao terminar o for
    ## (1) a pilha está vazia, isso significa que tinhamos um ( [ {
    ##     correspondente para cada ) ] }, portanto a expressão está
    ##     correta
    ## (2) a pilha não está vazia, então há algum ( [ { que não foi
    ##     fechado e, portanto, a expressão está incorreta
    return len(P) == 0


## Script principal - - - - - - - - - - - - - - - - - - - - - - - - - #
if __name__ == "__main__":
## expressão escrita de forma correta
#    expressao = "( )(( )){([( )])}"
## expressão escrita de forma incorreta
    expressao = ")(( )){([( )])}"
    print(verifica_delimitadores(expressao))
