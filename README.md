# README.md

## Aprendendo sobre python com Sqlite3 

Aprendizado 1:

- Bibliotecas : sqlite3 

Aprendizado 2:

As sequências de operações para mexer com bando de dados é:

1. Importar a biblioteca conforme o modelo de banco de dados que será utilizado.

2. Abrir uma conexão.

3. Abrir um cursor.

4. Executar o cursor.

Aprendizado 3:

Para os dados puxados pelo query, tem que criar um variável array, e grava no array fazendo append utilizando:
    
    rows = cur.fetchall()
    for row in rows:
        variavel_array.append(row)

O comando 'fetchall()' significa trazer tudo.

Aprendizado 4:

Aprendi que dentro de um def (função), quando tem a função de mostrar, tem que ter o 'return'

Aprendizado 5:

Para criar o aplicativo de programa em Python, deve-se usar a biblioteca "tkinter".

    from tkinter import *
    from tkinter import Tk, StringVar, ttk

Aprendizado 6:

Para mexer com imagens no programa em Python, deve-se usar a biblioteca "pillow", ou "PIL".

    from PIL import Image, ImageTk

Aprendizado 7:

Para mexer com calendário tem a biblioteca seguinte : tkcalendar

    from tkcalendar import Calendar, DateEntry

Aprendizado 8:

Existe o componente messagebox , que trabalha com janela pop-up.  Dentro da biblioteca tkinter.

    from tkinter import Tk, StringVar, ttk, messagebox

