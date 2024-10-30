peso = float(input('Qual seu peso? (KG) '))
alt = float(input('Qual sua altura? (m) '))
imc = (peso / alt**2)
print('Seu imc e de {:.1f}'.format(imc,))
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade MORBIDAAAA!!!!!!'.format(imc))