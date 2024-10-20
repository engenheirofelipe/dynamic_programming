#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
from collections import namedtuple
from typing import Any


## Funções - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
def seletor_atividades(atividades: list[Any]) -> list[Any]:
    """
Recebe uma lista de atividades e retorna uma lista com a maior
quantidade de atividades compatíveis (problema de seleção de
atividades).
    """

    ## ordena a lista de atividades em ordem crescente usando o fim
    atividades_ordenada = sorted(atividades,
                                 key=lambda atividade: atividade.fim)

    ## assume que a primeira atividade é o primeiro elemento da lista
    ## das atividades selecionadas (resposta do problema)
    atividades_selecionadas = [atividades_ordenada[0]]
    k = 0

    for i in range(1, len(atividades_ordenada)):
        ## encontra a primeira atividade compatível e a coloca na lista
        ## de atividades selecionadas
        if atividades_ordenada[i].comeco >= atividades_ordenada[k].fim:
            atividades_selecionadas.append(atividades_ordenada[i])
            k = i

    return atividades_selecionadas


## Script principal - - - - - - - - - - - - - - - - - - - - - - - - - #
## gera a entrada para o problema de selação de atividades
Atividade = namedtuple("Atividade", "comeco fim")
comecos = [1,3,0,5,3,5,6,8,8,2,12]
fins = [4,5,6,7,9,9,10,11,12,14,16]
atividades = [Atividade(comeco, fim) \
              for comeco, fim in zip(comecos, fins)]
print(seletor_atividades(atividades))
