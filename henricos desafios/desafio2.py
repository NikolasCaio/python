def calcular_variacao(n_inicial, n_final ):
    #Calcula a variacao
    variacao = ((n_final - n_inicial) / n_inicial) * 100
    print(f'A variacao foi de {variacao:.2f}%')
    return variacao

(calcular_variacao(100, 200))
(calcular_variacao(100, 50))
