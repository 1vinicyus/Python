import tkinter as tk
from tkinter import messagebox

# Perguntas do Quiz
perguntas = [
    {
        "pergunta": "Quem desenvolveu o jogo Grand Theft Auto (GTA)?",
        "opcoes": [
            "A) Rockstar Games",
            "B) Ubisoft",
            "C) Activision",
            "D) EA"
        ],
        "resposta": "A"
    },
    {
        "pergunta": "Quem criou a linguagem de programação C?",
        "opcoes": [
            "A) Ken Thompson",
            "B) Dennis Ritchie",
            "C) Bjarne Stroustrup",
            "D) Brian Kernighan"
        ],
        "resposta": "B"
    },
    {
        "pergunta": "Qual foi o primeiro console doméstico da Sony?",
        "opcoes": [
            "A) PlayStation 2",
            "B) PlayStation",
            "C) PS One",
            "D) PlayStation Prototype"
        ],
        "resposta": "B"
    },
    {
        "pergunta": "Quem é o criador do sistema operacional Linux?",
        "opcoes": [
            "A) Bill Gates",
            "B) Steve Jobs",
            "C) Mark Zuckerberg",
            "D) Linus Torvalds"
        ],
        "resposta": "D"
    },
    {
        "pergunta": "Em que linguagem foi criado o jogo Minecraft?",
        "opcoes": [
            "A) C++",
            "B) Python",
            "C) C#",
            "D) Java"
        ],
        "resposta": "D"
    }
]

indice = 0
pontuacao = 0


def verificar_resposta(escolha):
    global indice, pontuacao

    resposta_correta = perguntas[indice]["resposta"]

    if escolha == resposta_correta:
        pontuacao += 4
        messagebox.showinfo("Resultado", "✅ Resposta Correta!")
    else:
        pontuacao -= 2
        messagebox.showerror("Resultado", "❌ Resposta Incorreta!")

    indice += 1

    if indice < len(perguntas):
        mostrar_pergunta()
    else:
        finalizar_quiz()


def mostrar_pergunta():
    pergunta_atual = perguntas[indice]

    lbl_pergunta.config(text=pergunta_atual["pergunta"])

    btn_a.config(text=pergunta_atual["opcoes"][0])
    btn_b.config(text=pergunta_atual["opcoes"][1])
    btn_c.config(text=pergunta_atual["opcoes"][2])
    btn_d.config(text=pergunta_atual["opcoes"][3])

    lbl_pontos.config(text=f"Pontuação: {pontuacao}")


def finalizar_quiz():
    lbl_pergunta.config(
        text=f"Quiz Encerrado!\n\nPontuação Final: {pontuacao}"
    )

    btn_a.pack_forget()
    btn_b.pack_forget()
    btn_c.pack_forget()
    btn_d.pack_forget()

    lbl_pontos.config(
        text=f"Você terminou o quiz com {pontuacao} pontos!"
    )


def reiniciar():
    global indice, pontuacao

    indice = 0
    pontuacao = 0

    btn_a.pack(fill="x", pady=5)
    btn_b.pack(fill="x", pady=5)
    btn_c.pack(fill="x", pady=5)
    btn_d.pack(fill="x", pady=5)

    mostrar_pergunta()


# Janela
app = tk.Tk()
app.title("🎮 Quiz Tecnologia e Jogos")
app.geometry("700x450")
app.config(bg="#1e1e1e")

# Título
titulo = tk.Label(
    app,
    text="🎮 Quiz Tecnologia e Jogos",
    font=("Segoe UI", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
)
titulo.pack(pady=15)

# Pergunta
lbl_pergunta = tk.Label(
    app,
    text="",
    wraplength=600,
    font=("Segoe UI", 14),
    bg="#1e1e1e",
    fg="white"
)
lbl_pergunta.pack(pady=20)

# Frame dos botões
frame_botoes = tk.Frame(app, bg="#1e1e1e")
frame_botoes.pack(padx=20, fill="x")

btn_a = tk.Button(
    frame_botoes,
    command=lambda: verificar_resposta("A"),
    height=2,
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 11)
)

btn_b = tk.Button(
    frame_botoes,
    command=lambda: verificar_resposta("B"),
    height=2,
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 11)
)

btn_c = tk.Button(
    frame_botoes,
    command=lambda: verificar_resposta("C"),
    height=2,
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 11)
)

btn_d = tk.Button(
    frame_botoes,
    command=lambda: verificar_resposta("D"),
    height=2,
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 11)
)

btn_a.pack(fill="x", pady=5)
btn_b.pack(fill="x", pady=5)
btn_c.pack(fill="x", pady=5)
btn_d.pack(fill="x", pady=5)

# Pontuação
lbl_pontos = tk.Label(
    app,
    text="Pontuação: 0",
    font=("Segoe UI", 12, "bold"),
    bg="#1e1e1e",
    fg="#00ff7f"
)
lbl_pontos.pack(pady=10)

# Reiniciar
btn_reiniciar = tk.Button(
    app,
    text="🔄 Reiniciar",
    command=reiniciar,
    bg="#28a745",
    fg="white",
    font=("Segoe UI", 11, "bold")
)
btn_reiniciar.pack(pady=15)

mostrar_pergunta()

app.mainloop()