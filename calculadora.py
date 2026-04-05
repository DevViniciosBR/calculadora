import tkinter as tk

# Função para clicar nos botões
def clicar(valor):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + str(valor))

# Limpar tudo
def limpar():
    entrada.delete(0, tk.END)

# Calcular resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Criar janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.configure(bg="#1e1e1e")

# Tela
entrada = tk.Entry(
    janela,
    font=("Arial", 20),
    bd=0,
    bg="#1e1e1e",
    fg="white",
    justify="right"
)
entrada.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Frame dos botões
frame = tk.Frame(janela, bg="#1e1e1e")
frame.pack()

# Estilo botão
def botao(texto, linha, coluna, comando, cor="#333", largura=5, altura=2):
    tk.Button(
        frame,
        text=texto,
        width=largura,
        height=altura,
        command=comando,
        bg=cor,
        fg="white",
        font=("Arial", 12),
        bd=0
    ).grid(row=linha, column=coluna, padx=5, pady=5)

# Linha 1
botao("C", 0, 0, limpar, "#ff3b30")
botao("(", 0, 1, lambda: clicar("("))
botao(")", 0, 2, lambda: clicar(")"))
botao("/", 0, 3, lambda: clicar("/"), "#ff9500")

# Linha 2
botao("7", 1, 0, lambda: clicar("7"))
botao("8", 1, 1, lambda: clicar("8"))
botao("9", 1, 2, lambda: clicar("9"))
botao("*", 1, 3, lambda: clicar("*"), "#ff9500")

# Linha 3
botao("4", 2, 0, lambda: clicar("4"))
botao("5", 2, 1, lambda: clicar("5"))
botao("6", 2, 2, lambda: clicar("6"))
botao("-", 2, 3, lambda: clicar("-"), "#ff9500")

# Linha 4
botao("1", 3, 0, lambda: clicar("1"))
botao("2", 3, 1, lambda: clicar("2"))
botao("3", 3, 2, lambda: clicar("3"))
botao("+", 3, 3, lambda: clicar("+"), "#ff9500")

# Linha 5
botao("0", 4, 0, lambda: clicar("0"))
botao(".", 4, 1, lambda: clicar("."))
botao("=", 4, 2, calcular, "#34c759", largura=12)

# Rodar app
janela.mainloop()