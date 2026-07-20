contatos = []

def adc_contatos():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    idade = int(input("Idade: "))

    user = {
    "nome": nome,
    "telefone": telefone,
    "idade": idade
}
    contatos.append(user)
#---------------------------------------------    
def remove():
    nome = input("Nome do contato: ")

    for user in contatos:
        if user["nome"] == nome:
            contatos.remove(user)
            print("Contato removido!")
            return

    print("Contato não encontrado.")
#---------------------------------------------
def busca():
    nome_busca = input("Nome do contato que deseja buscar: ")

    for user in contatos:
        if user["nome"] == nome_busca:
            print(f"Nome: {user['nome']}")
            print(f"Telefone: {user['telefone']}")
            print(f"Idade: {user['idade']} anos")
            return

    print("Contato não encontrado!")
#---------------------------------------------
num = 0

while num != 5:
    print("\n===== Agenda de Contatos=====")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Remover contato")
    print("4 - Buscar contato")
    print("5 - Sair")

    num = int(input("Escolha: "))

    if num == 1:
        adc_contatos()

    elif num == 2:
        if not contatos:
            print("Sem lista de contatos!")
        else:
            for user in contatos:
                print(f"Nome: {user['nome']}")
                print(f"Telefone: {user['telefone']}")
                print(f"Idade: {user['idade']} anos")
                
    elif num == 3:
        remove()   

    elif num == 4:
        busca()

    elif num == 5:
        print("Programa encerrado.")