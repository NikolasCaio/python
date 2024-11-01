tot18= toth = totm  = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    continuar = ' '

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        print('-'*30)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoa com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(F'E temos {totm} mulheres com menos de 20 anos')
