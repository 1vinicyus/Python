#Exercício 1: Laço for Básico
for i in range(1,3):
    print(i)

#Exercício 2: Laço while Básico   
contador = 1
while contador <=5:
    print(contador)
    contador+=1

#Exercício 3: Calcular Média com for
notas = [7.5, 8.0, 9.5, 6.0, 8.5]

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)

print("Média:", media)

#Exercício 4: Função range()
for num in range(1,11):
    resultado = 7*(num)
    print(f"7 * {num}: {resultado}")

#Exercício 5: Números Pares com range()   
for num in range(0,21, 2):
 print(num) 

#Exercício 6: Controle de Fluxo - break
lista  = [5,12, 8, 3, 15, 7]

for num in lista:
    if num >10:
        print(f"Número maior que 10 encontrado: ", num)
        break

#Exercício 7: Controle de Fluxo - continue
lista =  [-2, 5, -1, 8, -3, 10]

for num in lista:
    if num >0:
        print(f"Número maior que zero encontrado: ", num)

#Exercício 8: Iteração sobre Strings
texto = "Vinicyus"
vogais = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vogais:
        contador+=1

print("Quantidade de Vogais na palavra: ", contador)        

#Exercício 9: Sistema de Notas com Classificação

notas = [8.5, 6.0, 9.5, 7.0, 5.5]

for nota in notas:
    if nota >= 9.0:
        classificacao = "Excelente"
    elif nota >= 7.0:
        classificacao = "Bom"
    elif nota >= 5.0:
        classificacao = "Regular"
    else:
        classificacao = "Insuficiente"
    
    print(f"Nota {nota}: {classificacao}")

#Exercício 10: Calculadora de Estatísticas

numeros = [15, 8, 23, 4, 42, 11, 7, 19]

soma = 0
maior = numeros[0]
menor = numeros[0]
pares = 0
impares = 0

for num in numeros:
    soma += num

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

media = soma / len(numeros)

print("Soma:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)
