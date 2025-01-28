#number = int(input("Digite um número de 0 a 9999: "))


#unidade = number % 10
#dezena = (number // 10) % 10
#centena = (number // 100) % 10
#milhar = (number // 1000) % 10


#print(f"unidade: {unidade}")
#print(f"dezena: {dezena}")
#print(f"centena: {centena}")
#print(f"milhar: {milhar}")


num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))