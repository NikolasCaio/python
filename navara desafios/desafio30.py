from colorama import Fore
velocidade = float(input('Velocidade do carro em km/h: '))

limite = 80
multa_por_km = 7.00

if velocidade > limite:
    # Calcula a multa
    excesso = velocidade - limite#80
    multa = excesso * multa_por_km#7.00
    print(Fore.RED, 'Voce foi multado niwba! o valor da multa e de {:.2f}RS.'.format(multa),Fore.RESET)
else:
    print(Fore.GREEN, 'Voce ta chilling!',Fore.RESET)