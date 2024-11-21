def Par(n=0):
    if n% 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um numero: '))
if(Par(num)):
    print('e par')
else:
    print('nao e par')