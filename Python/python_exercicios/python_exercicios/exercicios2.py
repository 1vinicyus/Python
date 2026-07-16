#Estruturas de Dados

#Listas: criação, indexação (positiva/negativa), slicing [ : ], métodos (append, remove, pop, sort, len)
#Tuplas: imutabilidade, quando usar no lugar de listas
#Dicionários: pares chave-valor, keys(), values(), items(), adicionar/remover
#Sets: elementos únicos, operações de conjunto (união, interseção, diferença)

#Checkpoint: mini projeto que combine lista + dicionário (ex: agenda de contatos)

#1. Lista de compras
#Crie uma lista vazia. Adicione 5 itens com append(). Remova um item específico. No final, exiba a lista ordenada alfabeticamente.
#compras = []

#compras.append("Arroz")
#compras.append("Feijão")
#compras.append("Carne de Frango")
#compras.append("Café")
#compras.append("Leite")

#print(f"Lista sem itens removidos: {compras}")

#compras.remove("Carne de Frango")
#compras.sort

#print(f"Lista com um item removido: {compras}")

#2. Filtro de pares
#Dada a lista numeros = [3, 8, 15, 22, 7, 40, 11], crie uma nova lista contendo apenas os números pares (sem usar filter(), use um for).
#numeros = [3, 8, 15, 22, 7, 0, 11]

#pares = []

#for numero in numeros:
#    if numero % 2 == 0:
#       pares.append(numero)

#print(f"Lista Original: {numeros}")
#print(f"Lista de Pares: {pares}") 

#3. Maior e menor sem max()/min()
#Dada uma lista de números, descubra o maior e o menor valor sem usar max() ou min() — percorra a lista comparando manualmente.
#lista1 = [1,3,5]
#lista2 = [0, 1,5,7]

#listao = lista1 + lista2

#maior = listao [0]
#menor = listao [0]

#for numero in listao:
#    if numero > maior:
#        maior = numero

#    if numero < menor:
#        menor = numero

#print(f"Menor número: {menor}")
#print(f"Maior númeor: {maior}")   

#4. Troca com tupla
#Crie duas variáveis a = 5 e b = 10. Troque os valores entre elas usando uma tupla 
#a = 5
#b = 10

#a, b = b,a

#print(f"{a} e {b}")

#5. Agenda de idades
#Crie um dicionário vazio. Peça ao usuário 3 nomes e idades, guardando no dicionário (nome: idade). No final, exiba todos os pares.
agenda = {}

for x in range(3):
    nome = input(f"Digite o nome da {x+1}° Pessoa: ")
    idade = int(input(f"Digite a idade da {x+1}° Pessoa"))

agenda[nome] = idade 

for nome, idade in agenda.items():
    print(f"{nome} e {idade} anos")


#6. Contador de palavras
#Peça uma frase ao usuário. Conte quantas vezes cada palavra aparece e guarde isso em um dicionário. Exiba o resultado.

#7. Remover duplicados
#Dada a lista [1, 2, 2, 3, 4, 4, 4, 5], use um set pra remover os números duplicados e exiba o resultado.