def area(larg, comp):
    m = larg * comp
    print(f'A area de um terreno com {larg} de largura e {comp} de comprimento e de {m}')




print('Controle de terrenos')
print('-'* 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)