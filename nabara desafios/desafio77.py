num = list()
for cont in range(0, 5):
    num.append(int(input(f'Digite um valor para posicao {cont}: ')))
    #if cont == 0:
     #   max = min = num[cont]
    #else:
      #  if num[cont] > max:
      #      max = num[cont]
      #  if num[cont] < min:
       #     min = num[cont]
print(f'Voce digitou os valores {num} ')
print(f'O maior valor digitado foi {max(num)} nas posicoes: ', end=" ")
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}... ', end="")
print()
print(f'O menor valor digitado foi {min(num)} nas posicoes: ', end=" ")
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}... ', end="")
print()
