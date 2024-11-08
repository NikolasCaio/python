temp = []
princ = []
max = min = 0
while True:
    continuar = " "
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        max = min = temp[1]
    else:
        if temp[1] > max:
            max = temp[1]
        if temp[1] < min:
            min = temp[1]
    princ.append(temp[:])
    temp.clear()
    while continuar not in "SN": 
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == "N":
        break
print('-='* 30)
print(f'Os dados foram {princ}')
print(f'Ao todo voce cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {max}kg. maior peso de ', end=" ")
for p in princ:
    if p[1] == max:
        print(f'{p[0]}', end=" ")
print()
print(f'O menor peso foi de {min}kg, menor peso de ', end=" ")
for p in princ:
    if p[1] == min:
        print(f'{p[0]}', end=" ")
print()
print('-='* 30)