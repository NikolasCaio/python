n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
Pri = "Primeiro"
Seg = 'Segundo'
if n1 > n2:
    print('O {} valor e maior'.format(Pri))
elif n1 < n2:
    print('O {} valor e maior'.format(Seg))
else:
    print('Os Dois valores Sao iguais.')