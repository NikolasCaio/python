from functools import total_ordering


print("-="*20)
print('Loja do itstheNiko')
print("-="*20)
prod = float(input('Preco do produto: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] a vista cartao')
print('[ 3 ] 2x no cartao')
print('[ 4 ] 3x ou mais no cartao')
opcao = int(input('Qual vai ser a opcao? '))
if opcao == 1:
    total = prod - (prod * 10 / 100)
elif opcao == 2:
    total = prod - (prod * 5 / 100) 
elif opcao == 3:
    total = prod - (prod / 2)
    print('Sua compra sera parcelada em 2 vezes de {:.2f} SEM JUROS'.format(total))
elif opcao == 4:
    total = prod + (prod * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    (print('Sua compra sera parcelada em {} vezes de {:.2f}RS COM JUROS'.format(totparc, parcela)))
else:
    total = prod
    print('OPCAO INVALIDA de pagamento. tente novamente!')
print('Sua compra de {:.2f}RS vai custar {:.2f}RS'.format(prod, total))