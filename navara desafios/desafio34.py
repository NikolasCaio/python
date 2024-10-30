# Solicita ao usuário que insira três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Inicialmente, assumimos que o primeiro número é o menor e o maior
menor = num1
maior = num1

# Verifica se num2 é menor que o menor atual
if num2 < menor:
    menor = num2
# Verifica se num3 é menor que o menor atual
if num3 < menor:
    menor = num3

# Verifica se num2 é maior que o maior atual
if num2 > maior:
    maior = num2
# Verifica se num3 é maior que o maior atual
if num3 > maior:
    maior = num3

# Exibe o resultado
print(f"O menor número é {menor}.")
print(f"O maior número é {maior}.")
