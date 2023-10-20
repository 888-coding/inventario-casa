import sqlite3 as lite
con = lite.connect("database.db")
with con:
    cur = con.execute()
    query = "CREATE TABLE inventario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)"
    cur.execute(query)


