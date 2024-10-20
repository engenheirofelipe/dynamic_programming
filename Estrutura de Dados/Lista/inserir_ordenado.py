## cria uma lista com os números pares de 2 a 10
V = [i for i in range(2, 10 +2, 2)]

## desejo inserir o número 5 na lista V
x = 5

## faço a inserção do 5 no fim da lista
V.append(5)

## começo o processo de inserir no novo elemento na posição
## correta (usando o mesmo loop do insertion sort)
## o índice i marca o início de onde irei começar o processo
## de sobrescrever os elementos (vou mover os elementos da
## posição i-1 para i)
i = len(V) -2

## processo de deslocar os elementos da posição i-1 para i
while i >= 0 and V[i] > x:
    V[i+1] = V[i]
    i -= 1
V[i+1] = x

## mostro a lista após a inserção e o deslocamento dos elementos,
## que mantém a lista ordenada
print(V)
