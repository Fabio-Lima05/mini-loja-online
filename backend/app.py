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


if __name__ == "__main__":
    app.run(debug=True)