import sqlite3

conexao = sqlite3.connect("../database/loja.db")

cursor = conexao.cursor()

# Cria a tabela de clientes, caso ainda não exista.
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Cria a tabela de produtos, caso ainda não exista.
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK (preco >= 0),
    estoque INTEGER NOT NULL CHECK (estoque >= 0)
)
""")
# Cria a tabela de pedidos, caso ainda não exista.
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0)
)
""")

conexao.commit()
conexao.close()


print("Tabelas clientes, produtos e pedidos verificadas ou criadas com sucesso.")
