times = (
    'Flamengo', 'Palmeiras', 'Fluminense', 'Atlético-MG', 'Internacional',
    'São Paulo', 'Grêmio', 'Corinthians', 'Athletico-PR', 'Botafogo',
    'Santos', 'Fortaleza', 'América-MG', 'Bahia', 'Cruzeiro',
    'Vasco da Gama', 'Cuiabá', 'Goiás', 'Coritiba', 'Red Bull Bragantino'
)
print('-='*15)
print(f'Lista de times do brasileirao em outubro em 2023: {times}')
print('-='*15)
print(f'Os 5 primeiros sao {times[0:5]}')
print('-='*15)
print(f'Os quatros ultimos colocados sao {times[16:20]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'O Corinthians esta na {times.index("Corinthians")+1} posicao')
