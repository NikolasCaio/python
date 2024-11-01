menor = 0
maior = 0
for xesque in range(1,6):
    peso = float(input(f'Digite o peso da {xesque} pessoa: '))
    if xesque == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}KG')
print(f'O menor peso lido foi de {menor}KG')