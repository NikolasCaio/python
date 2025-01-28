print('='*20)
print('gerador de pa')
print('='*20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostra a mais? '))
print(f'Progressao finalizada com {total} termos mostrados')
