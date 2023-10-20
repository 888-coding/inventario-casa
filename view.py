# Importing library
import sqlite3 as lite

# Creating connection
con = lite.connect("database")

# Inserting data to database
with con:
    dados = []
    cur = con.cursor()
    query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra,serie, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(query, dados)
