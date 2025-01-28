from time import sleep  # Importa a função sleep para pausar a execução

# Solicita ao usuário dois números inteiros
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0  # Inicializa a variável opcao

# Inicia um loop que continuará até que a opção seja 5
while opcao != 5:
    # Exibe o menu de opções
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do progama''')
    
    # Solicita ao usuário que escolha uma opção
    opcao = int(input('>>>>>>> Qual e sua opcao? '))
    
    # Se a opção for 1, realiza a soma
    if opcao == 1:
        soma = n1 + n2  # Calcula a soma
        print(f'A soma entre {n1} e {n2} e {soma}')  # Exibe o resultado
        
    # Se a opção for 2, realiza a multiplicação
    elif opcao == 2:
        m = n1 * n2  # Calcula a multiplicação
        print(f'A multiplicao de {n1} e {n2} e igual a {m}')  # Exibe o resultado
        
    # Se a opção for 3, determina o maior número
    elif opcao == 3:
        if n1 > n2:  # Verifica qual número é maior
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor e {maior}')  # Exibe o maior número
        
    # Se a opção for 4, solicita novos números
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))  # Solicita o primeiro número
        n2 = int(input('Segundo valor: '))  # Solicita o segundo número
        
    # Se a opção for 5, finaliza o programa
    elif opcao == 5:
        print('Finalizando...')  # Mensagem de finalização
        sleep(1)  # Pausa por 1 segundo antes de sair
        
    # Se a opção não for válida
    else:
        print('OPCAO INVALIDA! TENTE NOVAMENTE')  # Mensagem de erro
        
    print('=-=' * 10)  # Exibe uma linha separadora

# Mensagem final após sair do loop
print('Fim do progama, Volte nunca')
