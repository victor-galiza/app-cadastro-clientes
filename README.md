# Projeto de Portfólio: Sistema de Cadastro de Clientes

Este é um projeto de portfólio que explora a integração entre front-end, back-end e banco de dados em uma aplicação web full-stack. Ele foi construído para ser um estudo de caso prático de um sistema de cadastro de clientes, demonstrando um fluxo completo de desenvolvimento.

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)
![Tecnologia](https://img.shields.io/badge/Front--end-HTML%20%26%20TailwindCSS-blue)
![Tecnologia](https://img.shields.io/badge/Back--end-Python%20%26%20Flask-orange)
![Tecnologia](https://img.shields.io/badge/Database-SQLite-lightgrey)

## 📝 Sobre o Projeto

A aplicação é um sistema simples de **CRUD** (**C**reate, **R**ead, **U**pdate, **D**elete) para gerenciar informações de clientes. O objetivo principal foi criar um fluxo completo e funcional: desde a captura de dados em um formulário web, passando pelo processamento no servidor, até o armazenamento e a manipulação dessas informações em um banco de dados.

O design da aplicação é moderno, com um tema escuro e responsivo, focado em proporcionar uma experiência de usuário agradável e intuitiva.

## ✨ Funcionalidades

-   **Cadastro de Clientes:** Adicionar novos clientes ao banco de dados através de um formulário intuitivo.
-   **Visualização de Clientes:** Listar todos os clientes cadastrados em uma tabela organizada.
-   **Atualização de Dados:** Editar as informações de um cliente existente.
-   **Exclusão de Clientes:** Remover um cliente do banco de dados de forma permanente.

## 🚀 Tecnologias e Ferramentas

Este projeto foi construído com as seguintes tecnologias:

-   **Front-end:**
    -   `HTML5`: Para a estrutura semântica das páginas.
    -   `Tailwind CSS`: Para a estilização de um design moderno, escuro e responsivo, utilizado via CDN.

-   **Back-end:**
    -   `Python 3`: Linguagem de programação principal.
    -   `Flask`: Micro-framework web para criar o servidor e gerenciar as rotas da API.

-   **Banco de Dados:**
    -   `SQLite`: Banco de dados relacional leve e de fácil configuração, ideal para desenvolvimento e prototipagem.

-   **Ferramenta de Design:**
    -   A interface de usuário (UI) da aplicação foi criada com o auxílio de uma ferramenta de Inteligência Artificial (IA), que ajudou a otimizar o design e o layout.

## 📂 Estrutura de Diretórios

O projeto está organizado da seguinte forma para garantir a separação de responsabilidades:

```text
/Cadastro Clientes
|-- database/
|   `-- clientes.db
|-- templates/
|   |-- index.html
|   |-- clientes.html
|   `-- atualizar.html
|-- app.py
|-- .gitignore
`-- README.md
``` 

## 💻 Como Executar o Projeto Localmente

Para executar este projeto em sua máquina local, siga os passos abaixo:

**Pré-requisitos:**
* **Python 3** instalado.
* **Flask** instalado. Caso não tenha, instale com o comando:
    ```bash
    pip install Flask
    ```

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/victor-galiza/app-cadastro-clientes.git
    ```

2.  **Crie a estrutura de pastas:**
    Certifique-se de que a estrutura de diretórios esteja como a descrita acima. Crie a pasta `database` na raiz do projeto. O arquivo `clientes.db` será criado automaticamente quando a aplicação for iniciada pela primeira vez.

3.  **Execute a aplicação Flask:**
    Abra o terminal na raiz do projeto e execute o seguinte comando:
    ```bash
    python app.py
    ```

4.  **Acesse no navegador:**
    Abra seu navegador e acesse o endereço `http://127.0.0.1:5000`. A página de cadastro de clientes será exibida.

## 🔐 Considerações de Desenvolvimento

Este projeto foi construído com algumas boas práticas em mente:

-   **Segurança:** O back-end utiliza **instruções preparadas** (`?`) para a inserção e atualização de dados, garantindo proteção contra ataques de **SQL Injection**.
-   **Organização:** A estrutura de diretórios separa os arquivos de front-end (`templates`) e back-end (`app.py`), o que é essencial para a manutenibilidade de projetos maiores.
-   **Controle de Versão:** O uso do arquivo `.gitignore` assegura que arquivos temporários e o banco de dados local não sejam enviados para o repositório.

## 💡 Próximos Passos

A aplicação atual é ideal para um ambiente de desenvolvimento e aprendizado. Para um ambiente de produção (online e público), os seguintes passos seriam necessários para aumentar a segurança e a robustez:

-   **Autenticação e Autorização:** Adicionar um sistema de login e registro para que apenas usuários autorizados possam acessar e modificar os dados.
-   **Banco de Dados de Produção:** Migrar do SQLite para um sistema de gerenciamento de banco de dados mais robusto e escalável, como **PostgreSQL** ou **MySQL**, que são mais adequados para o acesso de múltiplos usuários simultâneos.
-   **Testes:** Implementar testes de unidade e integração para garantir que a aplicação funcione corretamente sob diferentes cenários e após futuras modificações.
-   **Validação de Dados:** Adicionar validações mais robustas tanto no front-end (com JavaScript) quanto no back-end para garantir a integridade dos dados.

## ✍️ Autor

**Victor Galiza**

&copy; 2025 - Todos os direitos reservados.
