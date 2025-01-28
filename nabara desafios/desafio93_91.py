time = []

while True:
    jogador = {}
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []

    # Coleta os gols por partida e armazena na lista 'gols'
    for c in range(jogador['partidas']):
        gols = int(input(f'Quantos gols na partida {c + 1}? '))
        jogador['gols'].append(gols)

    # Calcula o total de gols
    jogador['total_de_gols'] = sum(jogador['gols'])
    time.append(jogador.copy())

    # Pergunta ao usuário se deseja continuar
    while True:
        continuar = str(input('Quer adicionar outro jogador? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break

print('-=' * 30)

# Exibe um resumo de todos os jogadores
print('Resumo do Time:')
for idx, jogador in enumerate(time):
    print(f"{idx + 1} - Nome: {jogador['nome']}, Total de Gols: {jogador['total_de_gols']}, Partidas: {jogador['partidas']}")

print('-=' * 30)

# Sistema de visualização de detalhes de cada jogador
while True:
    opcao = int(input('Digite o número do jogador para ver detalhes (0 para sair): '))
    if opcao == 0:
        break
    if 1 <= opcao <= len(time):
        jogador = time[opcao - 1]
        print(f'\n--- Detalhes do jogador {jogador["nome"]} ---')
        print(f'Nome: {jogador["nome"]}')
        print(f'Total de partidas: {jogador["partidas"]}')
        print(f'Total de gols: {jogador["total_de_gols"]}')
        print('Aproveitamento por partida:')
        for i, gols in enumerate(jogador['gols']):
            print(f'    => Na partida {i + 1}, fez {gols} gols.')
        print('-=' * 30)
    else:
        print('ERRO! Jogador não encontrado. Digite um número válido.')

print('<< ENCERRADO >>')
