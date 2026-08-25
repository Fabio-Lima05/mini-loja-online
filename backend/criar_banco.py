import sqlite3

conexao = sqlite3.connect("../database/loja.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso")