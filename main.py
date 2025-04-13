import hashlib
from flask import Flask, render_template, request, redirect, url_for, request
from utils.db import init_app, get_db
from models.livros import buscar_livro_google
from flask_login import LoginManager

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hablasblabla123'
app.config['MYSQL_DB'] = 'mvc'

init_app(app)
lm = LoginManager()

def cadastrar_professor(nome, email, cpf, senha_md5):
    conexao = None
    cursor = None
    try:
        print("___tentando conectar...___")
        conexao, cursor = get_db()
        print("___conectado.___")
        cursor.execute('INSERT INTO professores (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)', (nome, email, cpf, senha_md5))
        conexao.commit()
        print("___cadastro realizado com sucesso.___")
    except Exception as e: 
        print(f"Erro ao cadastrar: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def verificar_login(email, senha):
    conexao = None
    cursor = None
    try:
        conexao, cursor = get_db()
        senha_md5 = hashlib.md5(senha.encode()).hexdigest()
        cursor.execute("SELECT * FROM professores WHERE email = %s AND senha = %s", (email, senha_md5))
        return cursor.fetchone()       
    except Exception as e:
        print(f"Erro ao logar: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def login_professor():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = verificar_login(email, senha)

        if usuario:
            print("Login feito.")
            return redirect(url_for('home'))
        else:
            print("Email ou Senha incorretos")
            return render_template('login.html', erro="email ou senha incorretos!")

    return render_template('login.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return login_professor()

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        print("Funcionando!")
        nome = request.form.get('nome')
        email = request.form.get('email')
        cpf = request.form.get('cpf')
        senha = request.form.get('senha')
        senha_md5 = hashlib.md5(senha.encode()).hexdigest()

        cadastrar_professor(nome, email, cpf, senha_md5)

        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/buscar_livro", methods=['GET', 'POST'])
def buscar_livro():
    livro = None
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        livro = buscar_livro_google(titulo)
    return render_template('busca_livro.html', livro=livro)

if __name__ == '__main__':
    app.run(debug=True)
