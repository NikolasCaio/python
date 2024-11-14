jogador = {}
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input(f'quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []

# Coleta os gols por partida e armazena na lista 'gols'
for c in range(jogador['partidas']):
    gols = int(input(f'Quantos gols na partida {c+1}? '))
    jogador['gols'].append(gols)

# Calcula o total de gols
jogador['total_de_gols'] = sum(jogador['gols'])
print('-='* 30)
print(jogador)
print('-='* 30)

# Exibe cada item do dicionário com descrição
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-=' * 30)

# Exibe o resumo das partidas e total de gols
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, gols in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {gols} gols.')
print(f'Foi um total de {jogador["total_de_gols"]} gols.')
