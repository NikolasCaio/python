casa = float(input('Valor da casa: RS'))
salario = float(input('Salario do comprador: RS'))
anos = int(input('Quantos anos financiando? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f}RS em {} anos '.format(casa, anos), end='')
print('A prestacao sera de RS{:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser concedido! ')
else:
    print('Emprestimo negado! ')