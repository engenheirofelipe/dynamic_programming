#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #


## Impotação de módulos - - - - - - - - - - - - - - - - - - - - - - - #
from typing import TextIO
from collections import deque


## Implementação de funções - - - - - - - - - - - - - - - - - - - - - #
def verifica_tags(documento: TextIO) -> bool:
    """
Recebe um documento html e retorna True se, para cada tag, existe uma
fecha tag correspondente. Caso contrário, retorna False.
    """

    P = deque()

    for linha in documento:
        ## procura por uma tag
        ## o find retorna o índice de onde foi encontrado o caractere
        ## '<' na string, caso o caractere não é encotrado, retorna -1
        j = linha.find('<')

        while j != -1:
            ## o segundo argumento indica o início da busca
            k = linha.find('>', j+1)
            
            if k == -1:
                ## -1 indica que a tag não foi escrita de forma correta
                return False

            ## obtém tag sem os símbolos < e >
            tag = linha[j+1:k]

            if not tag.startswith('/'):
                ## se a tag não começa com o caractere '/', então ela
                ## é uma tag de aberta e deve ser inserida na pilha
                P.append(tag)

            else:
                ## note que se o else é executado, então a tag é uma
                ## tag de fechamento
                if len(P) == 0:
                    ## se a pilha estão vazia, então uma está faltando
                    ## alguma tag de abertura
                    return False

                ## aqui é feito tag[1:] pois a string da variável tag
                ## começa com o caractere '/'
                if tag[1:] != P.pop():
                    ## se as tags são distintas, então foi uma parte do
                    ## documento html foi aberto com p e fechado com
                    ## div, por exemplo
                    return False

            ## procura se há outra tag na linha
            ## se tiver, começa novamente o processo de verificação
            ## do contrário, vai para a próxima linha
            j = linha.find('<', k+1)

    ## se a pilha estiver vazia, então todas as tags abertas foram
    ## fechadas por suas tags correspondentes, caso contrário, há
    ## tags que não foram fechadas
    return len(P) == 0


## Script principal - - - - - - - - - - - - - - - - - - - - - - - - - #
if __name__ == "__main__":
    with open("teste.html") as documento:
        print(verifica_tags(documento))
