#from math import factorial
#fato = int(input('Calcular seu fatorial: '))
#f = factorial(fato)
#print(f'O fatorial de {fato} e {f}')


fato = int(input('Calcular seu fatorial: '))
c = fato
f = 1
print(f'Calculando {fato}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print('x' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f' {f}')