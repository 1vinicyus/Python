import random #biblioteca randomica
import string #biblioteca de stings

def password_generator(len_pass): #len_pass = comprimento 
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options  #"@ + 5 + a" 
   
    password_user = "" #zerando a variavel

    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user += digit  

    return password_user

choice_user = input("Quantos digitos deseja ter na Senha?")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada inválida")
    quit()    

response = password_generator(len_pass = choice_user)
print(f"Senha gerada: {response}")
