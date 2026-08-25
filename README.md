\# Mini Loja Online



Projeto desenvolvido para estudar os fundamentos de uma aplicação web organizada em três camadas: interface, servidor e banco de dados.



\## Objetivos



\- Compreender como o front-end se comunica com o back-end.

\- Criar uma API utilizando Python e Flask.

\- Armazenar informações em um banco de dados SQLite.

\- Utilizar Docker para executar a aplicação em um contêiner.

\- Praticar controle de versão com Git e GitHub.



\## Tecnologias utilizadas



\- Python

\- Flask

\- Flask-CORS

\- SQLite

\- HTML

\- JavaScript

\- Docker

\- Git



\## Organização do projeto



\- `frontend/`: arquivos da interface da loja.

\- `backend/`: API, criação do banco e configuração do Docker.

\- `database/`: pasta destinada ao banco de dados SQLite.



\## Arquivos principais



\- `frontend/index.html`: página principal da aplicação.

\- `frontend/app.js`: código JavaScript da interface.

\- `backend/app.py`: servidor e rotas da API.

\- `backend/criar\_banco.py`: script de criação do banco de dados.

\- `backend/Dockerfile`: instruções para criar a imagem Docker.



\## Como executar



\### 1. Instalar as dependências



```powershell

pip install flask flask-cors

```



\### 2. Acessar a pasta do back-end



```powershell

cd backend

```



\### 3. Criar o banco de dados



```powershell

python criar\_banco.py

```



\### 4. Iniciar o servidor



```powershell

python app.py

```



A API utiliza a porta 5000:



```text

http://localhost:5000

```



\### 5. Iniciar o front-end



Abra outro terminal na pasta principal do projeto:



```powershell

cd frontend

```



```powershell

python -m http.server 5500

```



Acesse a aplicação pelo navegador:



```text

http://localhost:5500

```



\## Estado atual



Projeto em desenvolvimento para praticar programação, desenvolvimento web, banco de dados e Docker.



\## Autor



Fabio Lima



Estudante de Ciência da Computação.

