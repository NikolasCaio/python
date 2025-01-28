total = totmil = menor = cont = 0
barato = ''

while True:
    continuar = ' '
    print('-'*30)
    print('Loja do itstheNiko')
    print('-'*30)

    nome = str(input('Nome do produto: '))
    preco = float(input('Preco do produto: RS'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    print('-'*30)
    
    
        

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-'*30)
print('Fim do progama')
print('-'*30)
print(f'O total da compra foi RS{total}')
print(f'temos {totmil} produtos custando mais de RS1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')
