import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog

CATEGORIAS = {
    "Imagens":    [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"],
    "PDFs":       [".pdf"],
    "Planilhas":  [".xlsx", ".xls", ".csv", ".ods"],
    "Documentos": [".doc", ".docx", ".txt", ".rtf"],
    "Vídeos":     [".mp4", ".mkv", ".avi", ".mov"],
    "Áudios":     [".mp3", ".wav", ".ogg", ".flac"],
    "Compactados":[".zip", ".rar", ".7z"],
}

root = tk.Tk()
root.title("Organizador de Pastas")
root.geometry("400x220")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

caminho = tk.StringVar()
status = tk.StringVar(value="Nenhuma pasta selecionada.")

def selecionar():
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    if pasta:
        caminho.set(pasta)
        nome = os.path.basename(pasta) or pasta
        status.set(f"📁  {nome}")
        btn_org.config(state="normal")

def organizar():
    pasta = caminho.get()
    btn_org.config(state="disabled", text="Organizando...")
    status.set("Aguarde...")

    def _run():
        movidos = 0
        for arquivo in os.listdir(pasta):
            caminho_arq = os.path.join(pasta, arquivo)
            if not os.path.isfile(caminho_arq):
                continue
            _, ext = os.path.splitext(arquivo)
            for cat, exts in CATEGORIAS.items():
                if ext.lower() in exts:
                    dest = os.path.join(pasta, cat)
                    os.makedirs(dest, exist_ok=True)
                    destino = os.path.join(dest, arquivo)
                    if os.path.exists(destino):
                        base, e = os.path.splitext(arquivo)
                        n = 1
                        while os.path.exists(os.path.join(dest, f"{base}_{n}{e}")):
                            n += 1
                        destino = os.path.join(dest, f"{base}_{n}{e}")
                    shutil.move(caminho_arq, destino)
                    movidos += 1
                    break
        status.set(f"✅  {movidos} arquivo(s) organizado(s)!")
        btn_org.config(state="normal", text="Organizar")

    threading.Thread(target=_run, daemon=True).start()

tk.Label(root, text="Organizador de Pastas", bg="#f5f5f5",
         font=("Segoe UI", 13, "bold")).pack(pady=(18, 2))

tk.Label(root, text="Organiza arquivos em subpastas por tipo.", bg="#f5f5f5",
         fg="#777", font=("Segoe UI", 9)).pack()

tk.Frame(root, bg="#ddd", height=1).pack(fill="x", padx=20, pady=12)

tk.Button(root, text="📂  Selecionar Pasta", command=selecionar,
          font=("Segoe UI", 10), relief="flat", bg="#7f77dd", fg="white",
          padx=12, pady=6, cursor="hand2",
          activebackground="#534AB7", activeforeground="white").pack()

tk.Label(root, textvariable=status, bg="#f5f5f5", fg="#444",
         font=("Segoe UI", 9), wraplength=340).pack(pady=10)

btn_org = tk.Button(root, text="Organizar", command=organizar, state="disabled",
                    font=("Segoe UI", 10, "bold"), relief="flat",
                    bg="#5dcaa5", fg="#0a2a1e", padx=14, pady=6, cursor="hand2",
                    activebackground="#1D9E75", activeforeground="white")
btn_org.pack()

root.mainloop()