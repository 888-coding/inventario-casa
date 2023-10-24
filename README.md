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
