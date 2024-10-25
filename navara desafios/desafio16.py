dias = int(input('Quantos Dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar e de RS{:.2f}'.format(pago))