from time import sleep

viagem = float(input('Qual foi a distancia da viagem em kms? '))
print('voce esta prestes a comecar uma viagem de {}km/h'.format(viagem))
print('Processando o preco da passagem...')
sleep(2)


# Calcula o preço da passagem com base na distância
if viagem <=200:
    preco = viagem * 0.50 # R$0,50 por Km para viagens de até 200 Km
else:
    preco = viagem * 0.45 # R$0,45 por Km para viagens mais longas
print('O preco da sua passagem e de {:.2f}RS'.format(preco))
