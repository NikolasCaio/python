import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} e igual a {}'.format(num, math.floor(raiz))) #math.ceil para arredondar para cima e floor para baixo

#podendo usar from math import sqrt, (floor) ou (ceil)
#raiz = sqrt(num)
