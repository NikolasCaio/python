matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for c in range(0, 3):
        matriz[linha][c] = int(input(f'Digite um valor para [{linha}, {c}]: '))
print('-='* 30)
for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]}]', end=" ")
        if matriz[linha][c] % 2 == 0:
            spar += matriz[linha][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares e {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna e de {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]