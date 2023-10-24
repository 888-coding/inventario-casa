# Importing library
import sqlite3 as lite

# Creating connection
con = lite.connect("database.db")

# Inserting data to database
def inserir_dados():
    with con:
        dados = ['armario', 'quarto', 'comprado na casas bahia', 'Marca Y', '31/05/2000', 1600.0, 'xxxxxxxxx', 'c:imagem']
        cur = con.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra,serie, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, dados)

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
        print(ver_dados)
