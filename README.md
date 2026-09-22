# Mini Loja Online

Projeto desenvolvido para estudar os fundamentos de uma aplicação web organizada em três camadas: interface, servidor e banco de dados.

## Objetivos

- Compreender como o front-end se comunica com o back-end.
- Criar uma API utilizando Python e Flask.
- Armazenar informações em um banco de dados SQLite.
- Trabalhar com cadastro e consulta de clientes, produtos e pedidos.
- Utilizar Docker para executar o back-end em contêiner.
- Praticar controle de versão com Git e GitHub.

## Funcionalidades

- Cadastro de clientes.
- Listagem de clientes.
- Cadastro de produtos.
- Listagem de produtos.
- Validação de nome, preço e estoque.
- Cadastro de pedidos.
- Listagem de pedidos.
- Persistência dos dados em SQLite.
- Comunicação entre front-end e back-end utilizando HTTP e JSON.

## Tecnologias utilizadas

- Python
- Flask
- Flask-CORS
- SQLite
- HTML
- CSS
- JavaScript
- Docker
- Git
- GitHub

## Organização do projeto

- `frontend/`: interface da aplicação.
- `backend/`: API Flask e arquivos do back-end.
- `database/`: banco de dados SQLite.

## Arquivos principais

- `frontend/index.html`: página principal.
- `frontend/app.js`: lógica JavaScript da interface.
- `frontend/style.css`: estilos da aplicação.
- `backend/app.py`: servidor Flask e rotas da API.
- `backend/criar_banco.py`: criação das tabelas do banco.
- `backend/Dockerfile`: configuração da imagem Docker.
- `backend/requirements.txt`: dependências do back-end.

## Estrutura da aplicação

```text
Navegador
   ↓
HTML + CSS + JavaScript
   ↓ HTTP / JSON
Flask
   ↓ SQL
SQLite