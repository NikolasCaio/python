ficha = list()
while True:
    continuar = " "
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    while continuar not in "SN": 
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == "N":
        break
print(f'{'No.':<4}{'NOME':<10}{'MEDIA':>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe!): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')