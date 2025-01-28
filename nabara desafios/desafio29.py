import random
from time import sleep

# Computador "pensa" em um número aleatório entre 0 e 5
nc = random.randint(0, 5)

nu = int(input('Tente adivinhar o numero que eu to pensando entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)

if nu == nc:
    print('Fez o basico!')
else:
    print('vai pra casa, nub, o numero escolhido pelo computador foi {} nao {}'.format(nc, nu))