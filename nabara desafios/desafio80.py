num = list()

while True:
    continuar = " "
    n = int(input('Digite um valor: '))

    if n not in num:
        num.append(n)
        print('Valor adicionado')
    else:
        print('Repetido n, niuba')

    while continuar not in "SN":
        continuar = str(input('Quer continuar [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Essa lista tem {len(num)} numeros')
(num.sort(reverse=True))
print(f'em ordem decrescente fica {num}')

if 5 in num:
    print('O valor 5 foi digitado.')

else:
    print('O valor 5 nao foi digitado!')
