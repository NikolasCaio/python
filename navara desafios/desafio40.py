from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem q se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade 
    print('Voce ainda n tem 18 anos, ainda falta {} anos para se alistar'.format(saldo))
    ano = nasc + 18
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print(('Voce ja deveria ter se alistado a {} anos '.format(saldo)))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))