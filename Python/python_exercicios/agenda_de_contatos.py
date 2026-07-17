contatos = {
    "nome": [],
    "telefone": [],
    "idade": []
}

def adc_contatos():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    idade = int(input("Idade: "))

    contatos["nome"].append(nome)
    contatos["telefone"].append(telefone)
    contatos["idade"].append(idade)


num = 0

while num != 5:
    print("\n===== Agenda =====")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Remover contato")
    print("4 - Buscar contato")
    print("5 - Sair")

    num = int(input("Escolha: "))

    if num == 1:
        adc_contatos()

    elif num == 2:
        print(contatos)

    elif num == 5:
        print("Programa encerrado.")