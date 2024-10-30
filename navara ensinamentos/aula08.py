nome = str(input('Qual e seu nome? '))
if nome == 'Nikolas':
    print('bala ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e comum')
elif nome in 'Ana Claudia Jessica juliana':
    print('Belo nome feminino')
else:
    print('Seu nome n e bala')
print('Tenha um bom dia {}!'.format(nome))
