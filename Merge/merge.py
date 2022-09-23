from array import array
import random

def merge(array, aux, esquerda, meio, direita):

    for k in range(esquerda, direita + 1):
        aux[k] = array[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            array[k] = aux[j]
            j += 1
        elif j > direita:
            array[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            array[k] = aux[j]
            j += 1
        else:
            array[k] = aux[i]
            i += 1


def mergesort(array, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2

    #Aqui vai ser ordenado a primeira parte do arranjo
    mergesort(array, aux, esquerda, meio)

    #Aqui vai ser ordenado a segunda parte do arranjo.
    mergesort(array, aux, meio + 1, direita)

    #Aqui vai ser ordenado a terceira parte do arranjo
    merge(array, aux, esquerda, meio, direita)


# Testa o algoritmo.
Vetor = [80, -20, -5, 8, 9, 10, 12, 13]
print("Arranjo não ordenado: ", Vetor)
aux = [0] * len(Vetor)
mergesort(Vetor, aux, 0, len(Vetor) - 1)
print("Arranjo ordenado:", Vetor)