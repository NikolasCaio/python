galera = list()
dado = list()
totmai = totmenor = 0
for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade',)
        totmai += 1
    else:
        print(f'{p[0]} e menor de idade')
        totmenor += 1

print(f'Temos {totmai} maiores e {totmenor} menores de idade')