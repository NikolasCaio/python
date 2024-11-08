import random
from time import sleep

# Computador "pensa" em um número aleatório entre 0 e 10
nc = random.randint(0, 10)

print('Tente adivinhar o numero que eu to pensando entre 0 e 10: ')

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual e seu palpite? '))
    palpites += 1
    print('PROCESSANDO...')
    sleep(.5)
    if jogador == nc:
        acertou = True
    else:
        if jogador < nc:
            print('Mais... tente d novo ai nub.')
        elif jogador > nc:
            print('MENOS... ta tomando gap nub.')
print(f'Fez o basico! com {palpites} palpites')
    