frase = str(input('Digite uma palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f'O inverso de {junto} e {inverso}')
if inverso == junto:
    print('temos um palindromo!!')
else:
    print('A frase digitada nao e um palindromo')