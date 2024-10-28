frase = input('Digite uma frase: ').strip().upper()
print('A letra a aparece {} na frase.'.format(frase.count('A')))
print('A Primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A ultima letra a apareceu na posicao {}'.format(frase.rfind('A')+1))