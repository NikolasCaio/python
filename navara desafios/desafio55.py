somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomedomaisvelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'------ {p} PESSOA --------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomedomaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media da idade do grupo e de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomedomaisvelho}')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos.')