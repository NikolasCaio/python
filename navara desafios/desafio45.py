from time import sleep
from random import randint


itens = ('Pedra','Papel','Tesoura')
opcao = ('Suas opcoes')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')

jogador = int(input('Qual e sua jogada? '))
computador = randint(1, 3)


print('JO')
sleep(1)
print('KENNN')
sleep(1)
print('PO!!')
sleep(1)

print('-='*11)
print('Computador jogou {}'.format(itens[computador - 1]))

print('Jogador jogou {}'.format(itens[jogador - 1]))
print('-='*11)



if computador == 1: #computador jogou pedra
    if jogador == 1:
        print('Cagou!')
    elif jogador == 2:
        print('Tomei gap')
    elif jogador == 3:
        print('Vai pra casa, nub!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #computador jogou papel
    if jogador == 1:
        print('Tomei gap')
    elif jogador == 2:
        print('Cagou!')
    elif jogador == 3:
        print('Vai pra casa, nub!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 3: #computador jogou tesoura
    if jogador == 1:
        print('Tomei gap')
    elif jogador == 2:
        print('Vai pra casa, nub!')
    elif jogador == 3:
        print('Cagou!')
    else:
        print('JOGADA INVALIDA!')


    