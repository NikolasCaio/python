def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um numero inteiro valido!\033[m ')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um numero inteiro valido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n


num = leiaint('Digite um inteiro: ')
num2 = leiafloat('Digite um real: ')
print(f'O valor inteiro foi {num} e o real foi {num2}')

