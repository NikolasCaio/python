n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Salve')
print('Seu primeiro nome e {}'.format(nome[0]))
print('Seu segundo nome e {}'.format(nome[len(nome)-1]))
      