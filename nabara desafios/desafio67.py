from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' ' 
    while  tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. total de {total}', end= '')
    print('DEU PAR' if total % 2 == 0 else '  DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce cagou!')
            v += 1
        else:
            print('Voce tomou gap, nub!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce cagou!')
            v += 1
        else:
            print('Voce tomou gap, nub!')
            break
    print('Vamos jogar novamente...')
print(f'Game over! voce defecou {v} vezes') 
