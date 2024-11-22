import moeda

p = float(input('Digite o preco: RS'))
print(f'A metade de {p} e RS{moeda.metade(p)}')
print(f'O dobro de {p} e RS{moeda.dobro(p)}')
print(f'Aumentado 10% temos RS{moeda.aumentar(p, 10)}')
print(f'Diminuindo em 10% temos RS{moeda.diminuir(p, 10)}')