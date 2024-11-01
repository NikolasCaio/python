from datetime import date
atual = date.today().year

for c in range(1,8):
    nasc = int(input(f'Em que ano a {c} Pessoa nasceu? '))
    idade = atual - nasc
    if idade >=18:
        print(f'A {c} pessoa tendo {idade} anos ja e de maior')
    else:
        print(f'A {c} pessoa tendo {idade} anos ainda nao e de maior.')