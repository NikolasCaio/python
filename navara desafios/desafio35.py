salario = float(input('qual o salario q tu ganha? '))

if salario > 1250:
    aumento = 10
    salario2 = salario  * 1.10
else:
   aumento = 15
   salario2 = salario * 1.15
print('O salario q ganha com aumento de {}%, e de{:.2f}'.format(aumento,salario2))


