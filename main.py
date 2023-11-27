# Main
# Trabalhar com grafica

# Importar bibliotecas
from tkinter import *
from tkinter import Tk, StringVar, ttk

##  Pillow
from PIL import Image, ImageTk

## Importando Tkcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Cores
co0 = "#2e2d2b"  # preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # verde
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # - verde

# Criando Janela
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style()
style.theme_use("clam")

# Criando frames

frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=1, padx=0, stick=NSEW)

# Trabalhando no frame Cima ============================================
# Abrindo Imagem
app_img = Image.open('inventario.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Inventário Doméstico', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Trabalhando no frame Meio ============================================

#  Criando entradas
l_nome = Label(frameMeio, text='Nome', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130,y=11)

l_local = Label(frameMeio, text='Sala/Área', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130,y=41)

l_descricao = Label(frameMeio, text='Descrição', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130,y=71)

l_modelo = Label(frameMeio, text='Marca/Modelo', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_modelo.place(x=10, y=100)
e_modelo = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_modelo.place(x=130,y=101)

l_cal = Label(frameMeio, text='Data da compra', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, background='darkblue',bordwidth=2, year=2023)
e_cal.place(x=130,y=131)

l_valor = Label(frameMeio, text='Valor da compra', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130,y=161)

l_serial = Label(frameMeio, text='Número de série', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serial.place(x=10, y=190)
e_serial = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serial.place(x=130,y=191)


janela.mainloop()