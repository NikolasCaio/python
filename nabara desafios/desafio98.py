from random import randint
from time import sleep

def sorteia(lista):
    print('SORTEANDO 5 VALORES DA LISTA', end=" ")
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(randint(1, 10))
        print(f'{n}', end=" ", flush=True)
        sleep(0.3)
    print('Pronto!')


def somarpar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somarpar(numeros)