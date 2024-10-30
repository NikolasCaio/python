num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversao:')
print('[ 1 ] Converter para binario')
print('[ 2 ] Converter para octal')
print('[ 3 ] Converter para hexadecimal')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    print('{}, convertido para binario e igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{}, Convertido para octal e igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{}, Convertido para hexadecimal e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida, tente novamente com 1 ou 2 ou 3.')





