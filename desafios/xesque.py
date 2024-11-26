def exibir_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

# Exibir menu dentro de um loop
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "5":  # Condição para sair
        print("Encerrando o programa...")
        break
    else:
        print(f"Você escolheu a opção {opcao}.")
