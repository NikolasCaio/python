print('-='*20)
print('Analisador de Triangulos')
print('-='*20)
r1= float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triangulo!', end=" ")
    if r1 == r2 == r3:
        print('EQUILATERO!')
    if r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos acima n podem formar triangulo!')