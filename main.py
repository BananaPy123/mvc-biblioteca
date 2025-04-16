import hashlib
from flask import Flask, render_template, request, redirect, url_for, request, flash
from utils.db import init_app, get_db
from models.livros import buscar_livro_google


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hablasblabla123'
app.config['MYSQL_DB'] = 'mvc'
app.config['SECRET_KEY'] = 'hablasblabla'

init_app(app)


#função pra colocar os dados do cadasto no banco de dados
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

#função pra pegar os dados no banco de dados e processar o login
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
    except ValueError as e:
        flash(str(e))
        return None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

#função pra fazer o login
def login_professor():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            senha = request.form.get('senha')
    
            usuario = verificar_login(email, senha)
        
            if usuario:
                print("Login feito.")
                return redirect(url_for('home'))
            else:
                # Login falhou, email ou senha incorretos
                return render_template('login.html', erro="Email ou senha incorretos!")
            
        except Exception as e:
            print(f"Email ou Senha incorretos: {e}")
            return render_template('login.html', erro="email ou senha incorretos!")

    return render_template('login.html')

def cadastro_alunos(nome, serie, email, senha_md5):
        conexao = None
        cursor = None
        
        try:
            conexao, cursor = get_db()
            cursor.execute('INSERT INTO alunos (nome, serie, email, senha) VALUES (%s, %s, %s, %s)', (nome, serie, email, senha_md5))
            conexao.commit()
            print("ALUNO CADASTRADO COM SUCESSO!")
        except Exception as e:
            print(f"ERRO AO CADASTRAR ALUNO: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
        return redirect(url_for('cadastrar_aluno'))

def cadastro_livros(titulo, autor, data_publicacao, isbn, descricao, capa):
    conexao = None
    cursor = None
    
    try:
        conexao, cursor = get_db()
        cursor.execute('INSERT INTO livros (titulo, autor, data_publicacao, isbn, descricao, capa) VALUES (%s, %s, %s, %s, %s, %s)', (titulo, autor, data_publicacao, isbn, descricao, capa))
        conexao.commit()
        print("LIVRO CADASTRADO COM SUCESSO!")
        flash("Livro cadastrado com sucesso!")
    except Exception as e:
        print(f"ERRO AO CADASTRAR LIVRO: {e}")
        flash(str(f"Erro ao cadastrar livro: {e}"))
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
#rotas
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    #aqui chamei a função declarada na linha 54
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

        #aqui chamei a função declarada na linha 17
        cadastrar_professor(nome, email, cpf, senha_md5)

        #redirecionar pra página de login se o cadastro for realizado
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
        autor = request.form.get('autor')
        data_publicacao = request.form.get('data_publicacao')
        isbn = request.form.get('isbn')
        descricao = request.form.get('descricao')
        capa = request.form.get('capa')
        
        cadastro_livros(titulo, autor, data_publicacao, isbn, descricao, capa)
    return render_template('busca_livro.html', livro=livro)


@app.route("/cadastrar_aluno", methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        nome = request.form.get('nome')
        serie = request.form.get('serie')
        email = request.form.get('email')
        senha = request.form.get('senha')
        senha_md5 = hashlib.md5(senha.encode()).hexdigest()
        
        cadastro_alunos(nome, serie, email, senha_md5)
    return render_template('cadastrar_aluno.html')

@app.route('/lista_alunos')
def lista_alunos():
    conexao = None
    cursor = None
    
    conexao, cursor = get_db()
    cursor.execute('SELECT nome, email FROM alunos')
    informacoes = cursor.fetchall()
    cursor.close()
    conexao.close()
    
    return render_template('lista_alunos.html', alunos=informacoes)

@app.route('/deletar_aluno/<email>')
def deletar_aluno(email):
    conexao, cursor = get_db()
    cursor.execute('DELETE FROM alunos WHERE email = %s', (email,))
    conexao.commit()
    cursor.close()
    conexao.close()
    
    return redirect(url_for('lista_alunos'))
    
@app.route('/editar_aluno/<email>', methods=['GET', 'POST'])
def editar_aluno(email):
    conexao, cursor = get_db()

    if request.method == 'POST':
        novo_nome = request.form['nome']
        novo_email = request.form['email']
        cursor.execute('UPDATE alunos SET nome = %s, email = %s WHERE email = %s', (novo_nome, novo_email, email))
        conexao.commit()
        cursor.close()
        conexao.close()
        return redirect(url_for('lista_alunos'))
    
    cursor.execute('SELECT nome, email FROM alunos WHERE email = %s', (email,))
    aluno = cursor.fetchone()
    cursor.close()
    conexao.close()
    
    return render_template('editar_aluno.html', aluno=aluno)


@app.route('/lista_livros')
def lista_livros():
    conexao, cursor = get_db()
    cursor.execute('SELECT id_livro, titulo, autor FROM livros')
    livros = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('lista_livros.html', livros=livros)


@app.route('/deletar_livro/<int:id_livro>')
def deletar_livro(id_livro):
    conexao, cursor = get_db()
    cursor.execute('DELETE FROM livros WHERE id_livro = %s', (id_livro,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect(url_for('lista_livros'))


@app.route('/editar_livro/<int:id_livro>', methods=['GET', 'POST'])
def editar_livro(id_livro):
    conexao, cursor = get_db()

    if request.method == 'POST':
        novo_titulo = request.form['titulo']
        novo_autor = request.form['autor']
        cursor.execute('UPDATE livros SET titulo = %s, autor = %s WHERE id_livro = %s', (novo_titulo, novo_autor, id_livro))
        conexao.commit()
        cursor.close()
        conexao.close()
        return redirect(url_for('lista_livros'))

    cursor.execute('SELECT titulo, autor FROM livros WHERE id_livro = %s', (id_livro,))
    livro = cursor.fetchone()
    cursor.close()
    conexao.close()
    return render_template('editar_livro.html', livros=livro)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
