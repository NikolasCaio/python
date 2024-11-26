n1 = float(input('Digite o Primeiro numero: '))     
n2 = float(input('Digite o Segundo numero: '))
n3 = float(input('Digite o Terceiro numero: ')) 

if n1 >= n2 and n3:
    print(f'{n1} e maior')
elif n2 >= n1 and n3:
    print(f'{n2} e maior')
else:
    print(f'{n3} e maior')