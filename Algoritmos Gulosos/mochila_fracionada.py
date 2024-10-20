#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Importação de módulos - - - - - - - - - - - - - - - - - - - - - - -#
from collections import namedtuple
from typing import Any


## Funções - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
def mochila_fracionado(peso_maximo: float,
                       itens: list[Any]) -> list[Any]:
    """
Implementação de um algortimo guloso para resolver o prolema da mochila
em que é permitido selecionar uma porção de um item.
    """

    itens_selecionados = []

    ## ordena os itens em ordem decrescente do valor/peso
    ## (custo benefício de selecionar um item)
    itens.sort(key=lambda item: (item.valor / item.peso), reverse=True)

    peso_permitido = peso_maximo
    i = 0

    while i < len(itens) and peso_permitido > 0:
        if itens[i].peso <= peso_permitido:
            ## adiciono a solução o item propriamente dito e
            ## a porção dele (nesse caso é 1 = 100%)
            itens_selecionados.append((itens[i], 1))
            peso_permitido = peso_permitido - itens[i].peso

        else:
            ## se um item ultrapassa o limite de peso, então
            ## guarda o item propriamente dito e a porção
            ## que cabe
            itens_selecionados.append((itens[i],
                                      peso_permitido/itens[i].peso))
            ## isso indica que todo o espaço disponível foi utilizado
            ## e não posso adicionar mais itens
            peso_permitido = 0

        i += 1

    return itens_selecionados


def imprime_itens(itens: list[Any]) -> None:

    print("Itens na mochila:")
    valor_final = 0

    for item, peso in itens:
        print(f'Valor: {item.valor}\tPeso: {item.peso}'
              f'\t {peso * 100:.2f}%')
        valor_final += item.valor * peso

    print(f'Valor total dos itens: {valor_final}')


## Script principal - - - - - - - - - - - - - - - - - - - - - - - - - #
## constrói uma instância do problem da mochila
Item = namedtuple("Item", "valor peso")
valores = [ 4, 2, 10, 1, 2]
pesos =   [12, 1, 4,  1, 2]
itens = [Item(valor, peso) for valor, peso in zip(valores, pesos)]
peso_maximo = 15

itens_selecionados = mochila_fracionado(peso_maximo, itens)
imprime_itens(itens_selecionados)
