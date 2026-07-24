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
    for check in tarefas:
        if check['descrição'] == descricao:
            print("Essa tarefa já existe")
            return
        
    tarefas.append(ticket)
    print("Tarefa adicionada!")

#--------------------------------------------   
#3
def check_tarefa():
    check= input("Qual Tarefa deseja Concluir? (digite a descrição)\n")

    for ticket in tarefas:
        if check == ticket['descrição']:
            ticket['status'] = "Concluída"
            print("Tarefa Concluída!")
            return
        
    print("Tarefa não encontrada!")
#--------------------------------------------   
#4
def remove_tarefa():
    remove = input("Qual tarefa deseja remover? (Digite a Descrição)")

    for ticket in tarefas:
        if remove == ticket['descrição']:
            tarefas.remove(ticket)
            print("Tarefa Removida")
            return
        
    print("Tarefa não encontrada!")
#--------------------------------------------   
#5
def busca():
    buscar = input("Qual tarefa deseja buscar? (Digite a Descrição)")

    for ticket in tarefas:
        if buscar == ticket['descrição']:
            print(f"Descrição: {ticket['descrição']}")
            print(f"Prioridade: {ticket['prioridade']}")
            print(f"Status: {ticket['status']}")
            return
    print("Tarefa não encontrada!")
#--------------------------------------------   
num = 0
while num != 6:
    print("=== Gerenciados de Tarefas ===\n")
    print("1 - Adicionar Tarefas")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Remover Tarefa")
    print("5 - Buscar tarefa por Descrição")
    print("6 - Sair")
    num = int(input("Digite a opção que deseja (1-6):"))
    if num == 1:
        adc_tarefas()   

    if num == 2:
        tarefas_con = []
        tarefas_pend = []
        for ticket in tarefas:
            if ticket['status'] == "Concluída":
                tarefas_con.append(ticket)
            else: 
                tarefas_pend.append(ticket)
           
        print("=== Tarefas Concluídas ===")
        for ticket in tarefas_con:
            print(ticket["descrição"])

        print("\n=== Tarefas Pendentes ===")
        for ticket in tarefas_pend:
            print(ticket["descrição"])
        if not tarefas: 
            print("Nenhuma tarefa Listada!")           

    if num == 3: 
        check_tarefa()

    if num == 4:
        remove_tarefa()

    if num == 5:
        busca()

    if num == 6: print("Programa Encerrado...")      