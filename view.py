# Importing library
import sqlite3 as lite

# Creating connection
con = lite.connect("database.db")

# Inserir Dados
def inserir_dados(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra,serie, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

#Updating data from an id
def atualizar_dados(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id =?"
        cur.execute(query, i)
def deletar_dados(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query,i)

# Ver dados
def ver_dados():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario ORDER BY id ASC"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

# Ver item individual
def ver_item(id):
    ver_item = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_item.append(row)
    return ver_item
