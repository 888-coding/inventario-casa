# Importing library
import sqlite3 as lite

# Creating connection
con = lite.connect("database.db")

# Inserting data to database
with con:
    dados = ['sofa', 'sala de estar', 'sofa comprado em loja casas bahia', 'Marca X', '28/05/1997', 600.0, 'xxxxxxxxx', 'c:imagem']
    cur = con.cursor()
    query = "INSERT INTO inventario(nome, local, descricao, marca, data_da_compra, valor_da_compra,serie, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(query, dados)
