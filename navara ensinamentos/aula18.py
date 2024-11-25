try:
    a = int(input('Numerodor: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Nao e possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu n informar os dados!')
else:
    print(f'O resultado e {r:.1f}')
finally:
    print('Volte sempre, muito obrigado!')