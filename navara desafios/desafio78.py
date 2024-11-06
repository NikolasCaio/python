num = list()

while True:

    continuar = " "
    n = int(input('Digite um valor: '))

    if n not in num:
        num.append(n)
        print('Valor adicionado')
    else:
        print('Valor duplicado! n vou adicionar')

    while continuar not in "SN": 
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == "N":
        break


(num.sort(reverse=False))
print(f'Os valores digitado sao: {num}')
