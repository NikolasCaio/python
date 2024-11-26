try:
    # Receber os dois números do usuário
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    
    # Solicitar a operação desejada
    operacao = input('Escolha uma operação (+, -, *, /): ')

    # Verificar qual operação foi escolhida
    if operacao == '+':
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {soma}')
    elif operacao == '-':
        subtracao = n1 - n2
        print(f'A subtração de {n1} - {n2} é igual a {subtracao}')
    elif operacao == '*':
        mult = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é igual a {mult}')
    elif operacao == '/':
        if n2 == 0:  # Verificar se o divisor é zero
            print('Erro: divisão por zero não é permitida!')
        else:
            div = n1 / n2
            print(f'A divisão de {n1} por {n2} é igual a {div}')
    else:
        # Caso o usuário insira uma operação inválida
        print('Operação inválida! Escolha entre +, -, *, /.')

except ValueError:
    # Caso o usuário digite algo que não seja um número
    print('Erro: Por favor, insira números válidos.')
    