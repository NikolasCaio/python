def verificar_primo(n):
    if n <= 1:  # Números menores ou iguais a 1 não são primos
        return False
    for i in range(2, n):  # Tenta dividir n por todos os números de 2 até n-1
        if n % i == 0:  # Se n for divisível por algum número, não é primo
            return False
    return True  # Se não encontrar divisores, o número é primo

# Teste a função
print(verificar_primo(7))  # Saída: True
print(verificar_primo(10))  # Saída: False
print(verificar_primo(13))  # Saída: True

