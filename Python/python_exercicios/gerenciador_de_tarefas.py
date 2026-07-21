tarefas = []

#1 
def adc_tarefas():
    descricao = input("Descrição da Tarefa: ")
    prioridade = input("Prioridade da Tarefa (alta, média, baixa): ")

    ticket = {
        "descrição": descricao,
        "prioridade": prioridade,
        "status": "pendente" #definido como pendente
    }
    tarefas.append(ticket)
#--------------------------------------------   
#3
def check_tarefa():
    check = input("Qual Tarefa deseja Concluir?\n")

    for ticket in tarefas:
        if check == ticket['status']:
            pass
    

#--------------------------------------------   
#4
#--------------------------------------------   
#5
#--------------------------------------------   
    num = 0
    while num != 6:
        print("=== Gerenciados de Tarefas ===\n")
        print("1 - Adicionar Tarefas\n")
        print("2 - Listar Tarefas\n")
        print("3 - Marcar Tarefa como Concluída\n")
        print("4 - Remover Tarefa\n")
        print("5 - Buscar tarefa por Descrição\n")
        print("6 - Sair")
        num = int(input("Digite a opção que deseja (1-6): \n"))
        if num == 1:
          adc_tarefas()
    
        if num == 2:
            for ticket in tarefas:
                print(f"Descrição: {ticket['descrição']}")
                print(f"Prioridade: {ticket['prioridade']}")
                print(f"Status: {ticket['status']}")

        if num == 3: 
          check_tarefa()         
          