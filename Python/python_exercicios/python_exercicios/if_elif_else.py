#Exercício 1: Estrutura if Básica
idade = 20

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("VocÊ é menor de idade!")

#Exercício 2: Estrutura if-else        
num= 17

if num % 2 == 0:
   print("Par!")
else:
   print("Impár!") 
    
#Exercício 3: Estrutura if-elif-else
nota = 8.5

if nota >= 9.0:
    print("Execelente!")
elif nota >= 7.0:
    print("Bom!") 

elif nota >=5.0:
    print("Regular")
else:
    print("Insuficiente")    

#Exercício 4: Operadores Lógicos   
idade = 20
carteira = True

if idade >=20 and carteira:
    print("Você pode dirigir pela ciade")
else: 
    print("Não pode dirigir!")    

#Exercício 5: Condições Aninhadas - Sistema de Aprovação
nota = 8.5
aprovado = False

if nota >= 7.0:
    print("Aprovado")
    
    if nota >= 9.0:
        print("Excelente")
    elif nota >= 8.0:
        print("Muito bom")
else:
    print("Reprovado")
    
    if nota >= 5.0:
        print("Pode recuperar")
    else:
        print("Reprovado sem recuperação")

#Exercício 6: Sistema de Desconto
valor_compra = 150

if valor_compra >=200:
    desconto = 0.20
elif valor_compra >=100:
    desconto = 0.10
elif valor_compra >=50:
    desconto = 0.05
else:
    desconto = 0

valor_final = valor_compra - (valor_compra*desconto)
print(f"Valor final da compra: R${valor_final:.2f}")

#Exercício 7: Sistema de Votação
anos = 17

if anos <16:
    print("Não pode votar")
elif anos >70:
    print("Voto Opicional")
elif anos == 16 or 17:
        print("Voto Opicional")
else: 
    print("Voto obrigatório!")     

#Exercício 8: Sistema de Frete com Condições Aninhadas   
distancia = 150
peso = 12
cliente_vip = True

if distancia <50:
    frete  = 10.00
elif distancia > 200:
    frete = 20.00
else:
    frete = 15.00

    if peso > 10:
        frete += 5.00

        if cliente_vip == True:
            frete *= 0.90
print(f"Valor total; R$ {frete:.2f}")

#Exercício 9: Projeto Integrado - Sistema de Empréstimo
salario = 3.500
restricoes = False
tempo = 3

if restricoes == True:
 print("CPF inválido, você foi negado!")

if salario>=3.000:
     print("Aprovado")
elif salario <2.000:
     print("Negado!")
else: 
     print("Analise especial")         

if tempo > 2:
    print("Aumentou sua chance de aprovação, pois vocÊ tem mais de 2 anos na empresa!!")