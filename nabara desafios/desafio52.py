frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
#for letra in range(len(junto) - 1, -1, -1):
#    inverso += junto[letra]
print(f'O inverso de {junto} e {inverso}')
if inverso == junto:
    print('temos um palindromo!!')
else:
    print('A frase digitada nao e um palindromo')