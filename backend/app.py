from flask import Flask, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


def conectar_banco():
    conexao = sqlite3.connect("../database/loja.db")
    return conexao


@app.route("/")
def inicio():
    return "Servidor da Mini Loja Online funcionando"


@app.route("/clientes", methods=["GET", "POST"])
def gerenciar_clientes():

    if request.method == "GET":
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nome, email FROM clientes")
        dados = cursor.fetchall()

        clientes_formatados = []

        for cliente in dados:
            clientes_formatados.append({
                "id": cliente[0],
                "nome": cliente[1],
                "email": cliente[2]
            })

        conexao.close()

        return clientes_formatados


    if request.method == "POST":
        novo_cliente = request.get_json()

        nome = novo_cliente["nome"]
        email = novo_cliente["email"]

        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)",
            (nome, email)
        )

        conexao.commit()
        conexao.close()

        return novo_cliente
    
@app.route("/produtos", methods=["GET", "POST"])
def gerenciar_produtos():

     if request.method == "GET":
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id, nome, preco, estoque FROM produtos"
        )

        dados = cursor.fetchall()
        produtos_formatados = []

        for produto in dados:
            produtos_formatados.append({
                "id": produto[0],
                "nome": produto[1],
                "preco": produto[2],
                "estoque": produto[3]
            })

        conexao.close()

        return produtos_formatados

     if request.method == "POST":
        novo_produto = request.get_json()

        nome = novo_produto["nome"]
        preco = novo_produto["preco"]
        estoque = novo_produto["estoque"]

        if not nome:
         return {"erro": "O nome do produto é obrigatório"}, 400

        if preco <= 0:
         return {"erro": "O preço deve ser maior que zero"}, 400

        if estoque < 0:
         return {"erro": "O estoque não pode ser negativo"}, 400

        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO produtos (nome, preco, estoque)
            VALUES (?, ?, ?)
            """,
            (nome, preco, estoque)
        )

        conexao.commit()

        id_produto = cursor.lastrowid

        conexao.close()

        return {
            "id": id_produto,
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        }, 201
@app.route("/pedidos", methods=["GET", "POST"])
def gerenciar_pedidos():

    if request.method == "GET":
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id, cliente_id, produto_id, quantidade
            FROM pedidos
        """)

        dados = cursor.fetchall()
        pedidos_formatados = []

        for pedido in dados:
            pedidos_formatados.append({
                "id": pedido[0],
                "cliente_id": pedido[1],
                "produto_id": pedido[2],
                "quantidade": pedido[3]
            })

        conexao.close()

        return pedidos_formatados

    if request.method == "POST":
        novo_pedido = request.get_json()

        cliente_id = novo_pedido["cliente_id"]
        produto_id = novo_pedido["produto_id"]
        quantidade = novo_pedido["quantidade"]

        if quantidade <= 0:
            return {"erro": "A quantidade deve ser maior que zero"}, 400

        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO pedidos (cliente_id, produto_id, quantidade)
            VALUES (?, ?, ?)
            """,
            (cliente_id, produto_id, quantidade)
        )

        conexao.commit()

        id_pedido = cursor.lastrowid

        conexao.close()

        return {
            "id": id_pedido,
            "cliente_id": cliente_id,
            "produto_id": produto_id,
            "quantidade": quantidade
        }, 201

if __name__ == "__main__":
    app.run(debug=True)