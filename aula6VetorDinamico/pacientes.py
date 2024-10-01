## lista em que seus elementos representam dados na forma
## (quarto, paciente)
P = [(101, 'João'), (201, 'Pedro'), (105, 'José'), (101, 'Maria')]

## nosso objetivo é encontrar dois pacientes que estão no mesmo quarto
## iremos usar um join (banco de dados) para fazer isso
## a lista D irá armazenar a combinação dois elementos distintos de P
## tais que possuem o mesmo número do quarto
D = []

## usamos um for aninhado para obter todas as combinações dois
## a dois dos elementos de P
for paciente1 in P:
    for paciente2 in P:
        ## if para selecionar apenas a combinção de dois elementos
        ## que estão no mesmo quarto (paciente1[0] == paciente2[0]) e
        ## e são pacientes distintos (paciente1[1] != paciente2[1])
        if paciente1[0] == paciente2[0] and\
           paciente1[1] != paciente2[1]:

            ## if que serve para evitar de adcionar um elemento mais
            ## de uma vez
            if len(D) == 0:
                D.append([paciente1, paciente2])
            else:
                for d in D:
                    if paciente1 not in d:
                        D.append([paciente1, paciente2])
print(D)
