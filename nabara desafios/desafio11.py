# Entrada do valor em reais
real = float(input('Quanto dinheiro você tem em reais (R$)? '))

# Conversão para dólares (usando a taxa de 5.70)
dolar = real / 5.70

print('Com R${:.2f}, você pode comprar US${:.2f}.'.format(real, dolar))