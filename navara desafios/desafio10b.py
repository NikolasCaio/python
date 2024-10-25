n1 = int(input('Numero que voce quer a tabuada: '))

for tabuada in range(1,11):
    print('{} x {:2} = {}'.format(n1, tabuada, n1*tabuada))