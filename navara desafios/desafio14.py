s = float(input('Qual e o salario do funcionario? '))
novo = s + (s*15/100)
print('O Funcionario que ganhava {:.2f} agora com 15%, de aumento vai ser de {:.2f} '.format(s, novo))