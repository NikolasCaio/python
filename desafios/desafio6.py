def exibir_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Remover Tarefa")
    print("5. Sair")

def adicionar_tarefa(tarefas):  # Padronizado o nome da função
    titulo = input("Digite o título da tarefa: ")
    if titulo in tarefas:
        print("Essa tarefa já existe!")
    else:
        tarefas[titulo] = "pendente"
        print(f"Tarefa '{titulo}' adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nTarefas:")
        for titulo, status in tarefas.items():
            print(f"- {titulo} ({status})")

def marcar_concluida(tarefas):
    titulo = input("Digite o título da tarefa a marcar como concluída: ")
    if titulo in tarefas:
        tarefas[titulo] = "concluída"
        print(f"Tarefa '{titulo}' marcada como concluída!")
    else:
        print("Tarefa não encontrada!")

def remover_tarefa(tarefas):
    titulo = input("Digite o título da tarefa a remover: ")
    if titulo in tarefas:
        del tarefas[titulo]
        print(f"Tarefa '{titulo}' removida com sucesso!")
    else:
        print("Tarefa não encontrada!")

# Programa principal
tarefas = {}
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")  # Valor será uma string

    if opcao == "1":
        adicionar_tarefa(tarefas)
    elif opcao == "2":
        listar_tarefas(tarefas)
    elif opcao == "3":
        marcar_concluida(tarefas)
    elif opcao == "4":
        remover_tarefa(tarefas)
    elif opcao == "5":
        print("Encerrando o programa... Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
