n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto e {} \n e a divisao e {:1f}  \n' .format(s, m, d), end=' ')
print('Divisao inteira {} e potencia {}'.format(di, e))