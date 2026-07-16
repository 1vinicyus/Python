#Todos os desafios foram criados pelo Claude através de um prompt
#desafio 1 
#nome = "Vinicyus"

#print(f"Olá, {nome}")

#desafio 2
#idade = int(input("Olá, qual seu ano de nascimento?"))

#print(f"Você tem {2026 - idade} anos!")

#desafios 3
#base = int(input ("Informe o tamanho da base do retângulo: "))
#altura = int(input("Informe a altura do retângelo: "))

#print(f"A área total do retângulo é de: {base * altura}")

#desafio 4
#num = int(input("Digite um número: "))

#if num %2 == 0:
 #print("O número é Par")
#else:
# print("O número é Impár") 

#desafio 5
#num1 = int(input("Digite o 1° número: "))
#num2 = int(input("Digite o 2° número: "))
#num3 = int(input("Digite o 3° número: "))

#maior = max(num1, num2, num3)

#print(f"{maior} é o maior número")

#desafio 6
#import random
#for int in range(10):
#   print(random.randint(1,100))

#desafio 7
#num = int(input("Informe um número: "))
#for x in range(1,11):
#    print(f"{num} x {x} = {x*num}")

#desafio 8
#import random

#soma = 0

#for x in range(5):
#   numero = random.randint(1, 100)
#    print(f"{x + 1}° número: {numero}")

#    soma += numero

#print(f"A soma de todos os números é: {soma}")


#desafio 9
palavra = input("Digite uma palavra: ")
vogais = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        vogais += 1

print(f"A palavra {palavra} possui {vogais} vogais!")

#desafio 10
#temp = int(input("Informe a temperatura em Celsius: "))
#graus = (temp *9)/5 + 32

#print(f"{graus} em Fahrenheit")