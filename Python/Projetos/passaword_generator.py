import tkinter as tk
from tkinter import messagebox
import random
import string

# Função para gerar senha
def password_generator(len_pass):
    caracteres = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    return "".join(random.choice(caracteres) for _ in range(len_pass))


# Botão gerar senha
def gerar_senha():
    tamanho = entrada_tamanho.get()

    if not tamanho.isdigit():
        messagebox.showerror("Erro", "Digite apenas números!")
        return

    tamanho = int(tamanho)

    if tamanho < 4 or tamanho > 100:
        messagebox.showwarning(
            "Aviso",
            "Escolha um tamanho entre 4 e 100 caracteres."
        )
        return

    senha = password_generator(tamanho)

    resultado.delete(0, tk.END)
    resultado.insert(0, senha)


# Botão copiar
def copiar_senha():
    senha = resultado.get()

    if senha:
        app.clipboard_clear()
        app.clipboard_append(senha)
        app.update()
        messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")


# Janela
app = tk.Tk()
app.title("🔐 Gerador de Senhas")
app.geometry("450x250")
app.configure(bg="#1e1e1e")

# Título
titulo = tk.Label(
    app,
    text="Gerador de Senhas",
    font=("Segoe UI", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
)
titulo.pack(pady=10)

# Label tamanho
label = tk.Label(
    app,
    text="Quantidade de caracteres:",
    font=("Segoe UI", 10),
    bg="#1e1e1e",
    fg="white"
)
label.pack()

# Entrada tamanho
entrada_tamanho = tk.Entry(
    app,
    justify="center",
    font=("Segoe UI", 11)
)
entrada_tamanho.pack(pady=5)

# Botão gerar
btn_gerar = tk.Button(
    app,
    text="Gerar Senha",
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=gerar_senha
)
btn_gerar.pack(pady=10)

# Campo da senha
resultado = tk.Entry(
    app,
    font=("Consolas", 12),
    justify="center",
    width=35
)
resultado.pack(pady=5)

btn_copiar = tk.Button(
    app,
    text="📋 Copiar",
    bg="#28A745",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    command=copiar_senha
)
btn_copiar.pack(pady=10)

app.mainloop()