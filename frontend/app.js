function cadastrarCliente() {
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;

    if (nome === "") {
    alert("O nome não pode ficar vazio");
    return;
    }

    if (email === "") {
    alert("O email não pode ficar vazio");
    return;
    }

    if (!email.includes("@")) {
    alert("O email é invalido, faça direito");
    return;
    }

    if (!email.includes(".")) {
    alert("O email deve conter um '.', repita ");
    return;

    }

   const cliente = {
    nome,
    email
    };

    fetch("http://127.0.0.1:5000/clientes", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(cliente)
})
.then(resposta => resposta.json())
.then(dados => {
    console.log(dados);
      alert("Cliente cadastrado com sucesso!");
});
    

    console.log(cliente);
    
};

function carregarClientes() {
    fetch("http://127.0.0.1:5000/clientes")
        .then(resposta => resposta.json())
        .then(clientes => {
            const lista = document.getElementById("lista-clientes");

            lista.innerHTML = "";

            clientes.forEach(cliente => {
                const item = document.createElement("li");

                item.textContent = cliente.nome + " - " + cliente.email;

                lista.appendChild(item);
            });
        });
}

function carregarProdutos() {
    fetch("http://127.0.0.1:5000/produtos")
        .then(resposta => resposta.json())
        .then(produtos => {
            const lista = document.getElementById("lista-produtos");

            lista.innerHTML = "";

            produtos.forEach(produto => {
                const item = document.createElement("li");

                item.textContent =
                    produto.nome +
                    " - €" +
                    produto.preco +
                    " - estoque: " +
                    produto.estoque;

                lista.appendChild(item);
            });
        });
}

function cadastrarPedido() {
    const clienteId = document.getElementById("pedido-cliente").value;
    const produtoId = document.getElementById("pedido-produto").value;
    const quantidade = document.getElementById("pedido-quantidade").value;

    if (clienteId === "" || produtoId === "" || quantidade === "") {
        alert("Preencha todos os campos do pedido");
        return;
    }

    if (Number(quantidade) <= 0) {
        alert("A quantidade deve ser maior que zero");
        return;
    }

    const pedido = {
        cliente_id: Number(clienteId),
        produto_id: Number(produtoId),
        quantidade: Number(quantidade)
    };

    fetch("http://127.0.0.1:5000/pedidos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(pedido)
    })
    .then(resposta => {
        return resposta.json().then(dados => {
            if (!resposta.ok) {
                throw new Error(dados.erro);
            }

            return dados;
        });
    })
    .then(dados => {
        alert("Pedido realizado com sucesso!");

        document.getElementById("pedido-cliente").value = "";
        document.getElementById("pedido-produto").value = "";
        document.getElementById("pedido-quantidade").value = "";

        carregarPedidos();
    })
    .catch(erro => {
        alert(erro.message);
    });
}

function carregarPedidos() {
    fetch("http://127.0.0.1:5000/pedidos")
        .then(resposta => resposta.json())
        .then(pedidos => {
            const lista = document.getElementById("lista-pedidos");
            lista.innerHTML = "";

            pedidos.forEach(pedido => {
                const item = document.createElement("li");

                item.textContent =
                    "Pedido #" + pedido.id +
                    " - Cliente: " + pedido.cliente_id +
                    " - Produto: " + pedido.produto_id +
                    " - Quantidade: " + pedido.quantidade;

                lista.appendChild(item);
            });
        });
}

function cadastrarProduto() {
    const nome = document.getElementById("produto-nome").value;
    const preco = document.getElementById("produto-preco").value;
    const estoque = document.getElementById("produto-estoque").value;

    if (nome === "") {
    alert("O nome do produto não pode ficar vazio, por favor insira algo");
    return;
}

if (preco === "" || Number(preco) <= 0) {
    alert("O preço deve ser maior que zero");
    return;
}

if (estoque === "" || Number(estoque) < 0) {
    alert("O estoque não pode ser negativo");
    return;
}

    const produto = {
        nome: nome,
        preco: Number(preco),
        estoque: Number(estoque)
    };

    fetch("http://127.0.0.1:5000/produtos", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(produto)
    })
    .then(resposta => resposta.json())
    .then(dados => {
        console.log(dados);
        alert("Produto cadastrado com sucesso!");

        document.getElementById("produto-nome").value = "";
document.getElementById("produto-preco").value = "";
document.getElementById("produto-estoque").value = "";

        carregarProdutos();
    });
}

carregarClientes();
carregarProdutos();
carregarPedidos();