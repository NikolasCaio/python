num = list()
pares = list()
impares = list()
while True:
    continuar = " "
    num.append(int(input('Digite um numero: ')))

    while continuar not in "SN": 
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == "N":
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='* 30)
print(f'A lista completa e {num}')
print(f'A lista de pares e {pares}')
print(f'A lista de impares e {impares}')