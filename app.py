from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
# O caminho para o banco de dados deve ser ajustado para onde o arquivo está
# Por exemplo, se estiver na mesma pasta que o app.py, use 'clientes.db'
DATABASE = './database/clientes.db'

# Função para conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # Permite acesso aos dados por nome da coluna
    return conn

# Inicializa o banco de dados, criando a tabela se ela não existir
def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()

# Rota para exibir o formulário HTML (Página inicial)
@app.route('/')
def home():
    return render_template('index.html')

# Rota para processar os dados do formulário e salvar no banco de dados
@app.route('/cadastrar', methods=['POST'])
def cadastrar_cliente():
    try:
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        email = request.form['email']
        
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO clientes (name, age, gender, email) VALUES (?, ?, ?, ?)
            ''', (name, age, gender, email))
            conn.commit()

        return redirect(url_for('ver_clientes'))

    except Exception as e:
        return f"Ocorreu um erro: {e}", 500

# Rota para exibir a lista de clientes (LER)
@app.route('/clientes')
def ver_clientes():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
    return render_template('clientes.html', clientes=clientes)

# Rota para DELETAR um cliente
@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_cliente(id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
        conn.commit()
    return redirect(url_for('ver_clientes'))

# Rota para exibir o formulário de ATUALIZAÇÃO
@app.route('/atualizar/<int:id>', methods=['GET'])
def pagina_atualizar_cliente(id):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
        cliente = cursor.fetchone()
    if cliente is None:
        return "Cliente não encontrado.", 404
    return render_template('atualizar.html', cliente=cliente)

# Rota para processar a ATUALIZAÇÃO do cliente
@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar_cliente(id):
    try:
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        email = request.form['email']

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE clientes SET name = ?, age = ?, gender = ?, email = ? WHERE id = ?
            ''', (name, age, gender, email, id))
            conn.commit()
        
        return redirect(url_for('ver_clientes'))

    except Exception as e:
        return f"Ocorreu um erro: {e}", 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
