from datetime import date
atual = date.today().year
nasc = int(input('Informe sua data de nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('voce tendo {} anos voce e da classe mirim.'.format(idade))
elif idade <= 14:
    print('Voce tendo {} anos voce e da classe infantil.'.format(idade))
elif idade <= 19:
    print('Voce tendo {} anos voce e da classe junior.'.format(idade))
elif idade <= 25:
    print('Voce tendo {} anos voce e da classe Senior.'.format(idade))
else:
    print('voce tendo {} voce ja e da classe MASTER'.format(idade))

