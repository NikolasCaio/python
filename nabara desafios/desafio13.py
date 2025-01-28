preco = float(input('Preco do Produto: '))
novo = preco - (preco*5/100)
print('O valor do produto sendo {:.2f}, vai custar {:.2f} com 5%, de desconto'.format(preco, novo))