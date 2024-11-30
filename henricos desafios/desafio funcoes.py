informacao_inserida = ['Ferrari', '50000', '49010-000', 2024]


informacao_recebida_correta = ['FERRARI', 'R$ 50.000,00', '49010000', 2024]
informacao_recebida_incorreta = ['FERRARI', 'R$ 100.000,00', '49010000', 2023]

def vereficar_valores(informacao1, informacao2):
    if informacao1[0].upper() == informacao2[0].upper():
        modelo = True
    else:
        modelo = False
    if informacao1[1] == informacao2[1].replace('R$ ', '').replace('.','').split(',')[0]:
        preco = True
    else:
        preco = False
    if informacao1[2].replace('-', '') == informacao2[2]:
        cep = True
    else:
        cep = False
    if informacao1[3] == informacao2[3]:
        ano = True
    else:
        ano = False
    if modelo and preco and cep and ano == True:
        return True
    else:
        return False
        
    
    
    return informacao1 == informacao2











resultado_certo = vereficar_valores(informacao1= informacao_inserida, informacao2= informacao_recebida_correta)
resultado_incerto = vereficar_valores(informacao1= informacao_inserida, informacao2= informacao_recebida_incorreta)

print(resultado_certo) # Deve devolver True
print(resultado_incerto) # Deve devolver False






# Comparar se o nome do carro voltou corretamente

'''
carro_inserido = 'Ferrari'
carro_recebido_correto = 'Ferrari modelo 1234 abc pedro pedro pedro                            '
carro_recebido_incorreto = 'Pegeout'

def verificar_nome_carro(carro1: str, carro2: str):
    if carro1.upper().strip().split()[0] == carro2.upper().strip().split()[0]:
        print('Correto')
    else:
        print('Incorreto')

verificar_nome_carro(carro_inserido, carro_recebido_incorreto)
verificar_nome_carro(carro_inserido, carro_recebido_correto)'''