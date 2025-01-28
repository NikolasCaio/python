print('='*20)
print('gerador de pa')
print('='*20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    cont += 1
print('')