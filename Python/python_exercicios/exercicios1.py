#Fundamentos 

#Variáveis e tipos (int, float, str)
#input() / print() / f-strings
#Operadores aritméticos e de comparação
#Condicionais (if/elif/else)
#Laços (for, while), range()


#1. Olá, mundo com variável
#Crie uma variável com seu nome e faça o programa exibir "Olá, [seu nome]! Bem-vindo ao Python."
nome = "Vinicyus"
print(f"Olá, {nome} Bem Vindo ao Python!")

#2. Calculadora de idade
#Peça ao usuário o ano de nascimento (input()) e calcule a idade aproximada dele, exibindo o resultado.

ano_nascimento= int(input("Olá, qual seu ano de nascimento?"))

print(f"Você tem {2026 - ano_nascimento} anos!")

#3. Área do retângulo
#Peça a largura e a altura de um retângulo e calcule a área.
base = int(input ("Informe o tamanho da base do retângulo: "))
altura = int(input("Informe a altura do retângulo: "))

print(f"A área total do retângulo é de: {base * altura}")

#4. Par ou ímpar
#Peça um número ao usuário e informe se ele é par ou ímpar.
num = int(input("Digite um número: "))

if num %2 == 0:
    print("O número é Par")
else:
    print("O número é Ímpar") 

#5. Maior de três
#Peça três números e informe qual é o maior deles.
num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))
num3 = int(input("Digite o 3° número: "))

maior = max(num1, num2, num3)

print(f"{maior} é o maior número")

#6. Contador de 1 a 10
#Use um for para exibir os números de 1 a 10.
import random
for x in range(10):
   print(random.randint(1,100))

#7. Tabuada
#Peça um número e exiba a tabuada dele (de 1 a 10), usando um for.
num = int(input("Informe um número: "))
for x in range(1,11):
    print(f"{num} x {x} = {x*num}")

#8. Soma de uma lista
#Crie uma lista com 5 números e calcule a soma de todos eles (pode usar sum() ou um for com acumulador).
import random

soma = 0

for x in range(5):
    numero = random.randint(1, 100)
    print(f"{x + 1}° número: {numero}")
    soma += numero

print(f"A soma de todos os números é: {soma}")


#9. Contador de vogais
#Peça uma palavra ao usuário e conte quantas vogais ela tem.
palavra = input("Digite uma palavra: ")
vogais = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        vogais += 1

print(f"A palavra '{palavra}' possui {vogais} vogais!")

#10. Conversor de temperatura
#Peça uma temperatura em Celsius e converta para Fahrenheit (fórmula: F = C × 9/5 + 32).
temp = float(input("Informe a temperatura em Celsius: "))
graus = (temp *9)/5 + 32

print(f"{graus} em Fahrenheit")