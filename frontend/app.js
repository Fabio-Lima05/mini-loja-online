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

carregarClientes();