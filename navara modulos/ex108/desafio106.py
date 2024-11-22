import moeda

p = float(input('Digite o preco: RS '))
print(f'A metade de {moeda.moeda(p)} e de {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} e de {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo em 10% {moeda.moeda(moeda.diminuir(p, 10))}')