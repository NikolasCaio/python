def conta_vogais(texto):
    vogais = "aeiouAEIOU"  # Lista de vogais (maiúsculas e minúsculas)
    contador = 0  # Inicializa o contador de vogais
    
    for letra in texto:  # Percorre cada letra do texto
        if letra in vogais:  # Verifica se a letra é uma vogal
            contador += 1  # Incrementa o contador
    
    return contador  # Retorna o número total de vogais

# Testando a função
print(conta_vogais("Programação"))  # Saída: 5
print(conta_vogais("Python"))       # Saída: 1
print(conta_vogais("ChatGPT"))      # Saída: 2
