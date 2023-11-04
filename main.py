# Main
# Trabalhar com grafica

# Importar bibliotecas
from tkinter import *
from tkinter import Tk, StringVar, ttk

# Cores
co9 = "#e9edf5"

# Criando Janela
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style()
style.theme_use("clam")

# Criando frames


janela.mainloop()