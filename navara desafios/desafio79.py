lista = list()
for n in range(0, 5):
    num = int(input('Digite um valor: '))
    if n == 0 or num > lista[-1]:
        lista.append(num)
    else: 
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(f'Os valores digitados em ordem fica {lista} ')
