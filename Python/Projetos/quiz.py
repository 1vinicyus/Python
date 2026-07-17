print("Seja Bem-Vindo ao Quiz sobre Tecnologia e Jogos!")
answer_user = input("Quer começar? (S/N): ").strip().lower()


if answer_user != "s":
    quit()

score = 0 
print("Começando....\n")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A)Rockstar Games\n (B)Ubisoft\n (C)Activision\n (D)EA\n")
answer_1 = input("Resposta: ")

if answer_1.lower() == "a":
    print("Correct!\n")
    score += 4
else: 
    print("Incorrect!\n")
    score -= 2   

print("Quem criou a linguagem de programação C? \n (A)Ken Thompson\n (B)Dennis Ritchie\n (C)Bjarne Stroustrup\n (D)Brian Kernighan\n")
answer_2 = input("Resposta: ")

if answer_2.lower() == "b":
    print("Correct!\n")
    score += 4
else: 
    print("Incorrect!\n")   
    score -= 2

print("Qual foi o primeiro console doméstico da Sony? \n (A)PlayStation 2\n (B)PlayStation \n (C)PS One\n (D)PlayStation Prototype\n")
answer_3 = input("Resposta: ")

if answer_3.lower() == "b":
    print("Correct!\n")
    score += 4
else: 
    print("Incorrect!\n")
    score -= 2
    
print("Quem é o criador do sistema operacional Linux?\n (A)Bill Gates \n (B)Steve Jobs\n (C)Mark Zuckerberg\n (D)Linus Torvalds\n")
answer_4 = input("Resposta: ")

if answer_4.lower() == "d":
    print("Correct!\n")
    score += 4
else: 
    print("Incorrect!\n")
    score -= 2 

print(" Em que linguagem foi criado o jogo Minecraft?\n (A)C++\n (B)Python\n (C)C#\n (D)Java \n")
answer_5 = input("Resposta: ")

if answer_5.lower() == "d":
    print("Correct!\n")
    score += 4
else: 
    print("Incorrect!\n")
    score -= 2

print(f"O Quiz acabou! \nSua pontuação final: {score}") 