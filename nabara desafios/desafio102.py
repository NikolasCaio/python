def leiaint(frase):
    ok = False
    valor = 0
    while True:
        n = str(input(frase))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! digite um numero inteiro valido\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar numero {n}')