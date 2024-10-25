n1 = float(input('Primeira nota do aluno '))
n2 = float(input('Segunda nota do aluno '))
# botando o () para dar preferencia a conta de +
s= (n1 + n2) / 2
print('A media entre {} e {} e igual a {:.1f}'.format(n1, n2, s))