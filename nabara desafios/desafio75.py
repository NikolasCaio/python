listagem = ('Lapis', 1.75,
             'Borracha', 2,
             'Caderno', 15.90,
             'Estojo', 25,
             'Transeferidor', 4.20,
             'Compasso', 9.99,
             'Mochila', 120.32,
             'Canetas', 22.30,
             'Livro', 34.90)
print('-'*30)
print('Listagem de precos')
print('-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:    
         print(f'{listagem[pos]:.<30}', end='')  
    else:
         print(f'RS{listagem[pos]:>7.2f}')