cont = ('zero', 'um', 'dois', 'tres', 'quatro',
    'cinco', 'seis', 'sete','oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze','dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('tente novamente. ', end='')
print(f'Voce digitou o numero {cont[n]}')