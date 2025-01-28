pessoa = {}
galera = list()
continuar = " "
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor digite apenas M ou F ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda S ou N')

    if continuar == 'N':
        break

print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'a media de idade e de {media:5.2f} anos')
print('As mulheres cadastradas foram ', end="")
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=" ")
print()
print(f'Lista de pessoas que estao acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end=" ")
        print()
print('<< ENCERRADO! >>')

