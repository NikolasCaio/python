
while True:
    n1 = int(input('Numero que voce quer a tabuada: '))
    print('='*30)
    if n1 < 0:
        break
    for tabuada in range(1,11):
        print(f'{n1} x {tabuada:2} = {n1*tabuada}')
    print('='*30)
print('Num ta tendo nao nub') 
        
    

