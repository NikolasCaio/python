import moeda

p = float(input('Digite o preco: RS '))
print(f'A metade de {moeda.moeda(p)} e de {(moeda.metade(p, True))}')
print(f'O dobro de {moeda.moeda(p)} e de {(moeda.dobro(p, True))}')
print(f'Aumentado 10% temos {(moeda.aumentar(p, 10, True))}')
print(f'Diminuindo em 10% {(moeda.diminuir(p, 10, True))}')