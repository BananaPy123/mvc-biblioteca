import requests
import hashlib
import re
from datetime import datetime, date, timedelta
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# =============================================
# CONFIGURAÇÕES DO APLICATIVO
# =============================================

# Configurações do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'hablasblabla123'  # SUBSTITUA POR UMA SENHA SEGURA!
app.config['MYSQL_DB'] = 'mvc'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Para retornar resultados como dicionários

# Configurações de segurança
app.config['SECRET_KEY'] = 'hablasblabla'  # SUBSTITUA!
app.config['SESSION_COOKIE_SECURE'] = True  # Envia cookies apenas sobre HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Previne acesso a cookies via JavaScript
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Proteção contra CSRF
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)  # Tempo de sessão
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Inicializa o MySQL
mysql = MySQL(app)

# Configura o rate limiting (limite de tentativas de acesso)
limiter = Limiter(app)
limiter.key_func = get_remote_address
limiter.default_limits = ["200 per day", "50 per hour"]

# =============================================
# FUNÇÕES AUXILIARES
# =============================================

def login_required(f):
    """Decorador para proteger rotas que requerem login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash("Por favor, faça login para acessar esta página", "error")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def professor_required(f):
    """Decorador para garantir que apenas professores possam acessar"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in') or session.get('user_role') != 'professor':
            flash("Acesso restrito a professores", "error")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def validar_email(email):
    """Valida o formato do email"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validar_senha(senha):
    """Valida a força da senha (mínimo 8 caracteres)"""
    return len(senha) >= 8

def registrar_acesso(user_id, ip):
    """Registra um acesso bem-sucedido no sistema"""
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO acessos (user_id, ip, sucesso) VALUES (%s, %s, %s)",
            (user_id, ip, True)
        )
        mysql.connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao registrar acesso: {e}")

def registrar_tentativa_login(email, ip, sucesso):
    """Registra tentativas de login (sucesso ou falha)"""
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO tentativas_login (email, ip, sucesso) VALUES (%s, %s, %s)",
            (email, ip, sucesso)
        )
        mysql.connection.commit()
        cursor.close()
    except Exception as e:
        print(f"Erro ao registrar tentativa de login: {e}")

# =============================================
# ROTAS DE AUTENTICAÇÃO
# =============================================

@app.route("/")
def index():
    """Página inicial"""
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
@limiter.limit("5 per minute")  # Limita a 5 tentativas por minuto
def login():
    """Rota de login com todas as proteções de segurança"""
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '')
        
        # Validação básica
        if not email or not senha:
            flash("Por favor, preencha todos os campos", "error")
            return render_template('login.html')
            
        if not validar_email(email):
            flash("Formato de email inválido", "error")
            return render_template('login.html')
            
        # Verificar se o usuário existe e é professor
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("""
                SELECT id_professor, nome, email, senha 
                FROM professores 
                WHERE email = %s
                LIMIT 1
            """, (email,))
            professor = cursor.fetchone()
            cursor.close()
            
            if professor and check_password_hash(professor['senha'], senha):
                # Iniciar sessão segura
                session.clear()
                session['user_id'] = professor['id_professor']
                session['user_email'] = professor['email']
                session['user_role'] = 'professor'
                session['logged_in'] = True
                session['_fresh'] = True  # Sessão fresca
                
                # Registrar o login
                registrar_acesso(professor['id_professor'], request.remote_addr)
                
                next_page = request.args.get('next')
                return redirect(next_page or url_for('home'))
            else:
                # Logar tentativa fracassada
                registrar_tentativa_login(email, request.remote_addr, False)
                flash("Credenciais inválidas ou você não tem permissão para acessar", "error")
        
        except Exception as e:
            print(f"Erro durante o login: {e}")
            flash("Ocorreu um erro durante o login. Por favor, tente novamente.", "error")
    
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    """Rota para logout seguro"""
    session.clear()
    flash("Você foi desconectado com sucesso", "success")
    return redirect(url_for('index'))

# =============================================
# ROTAS DE CADASTRO
# =============================================

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """Rota para cadastro de novos professores"""
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        cpf = request.form.get('cpf', '').strip()
        senha = request.form.get('senha', '')
        
        # Validações
        if not all([nome, email, cpf, senha]):
            flash("Por favor, preencha todos os campos", "error")
            return render_template('cadastro.html')
            
        if not validar_email(email):
            flash("Formato de email inválido", "error")
            return render_template('cadastro.html')
            
        if not validar_senha(senha):
            flash("A senha deve ter pelo menos 8 caracteres", "error")
            return render_template('cadastro.html')
            
        try:
            senha_hash = generate_password_hash(senha, method='pbkdf2:sha256')
            cursor = mysql.connection.cursor()
            
            # Verifica se email já existe
            cursor.execute("SELECT id_professor FROM professores WHERE email = %s", (email,))
            if cursor.fetchone():
                flash("Este email já está cadastrado", "error")
                return render_template('cadastro.html')
                
            # Insere novo professor
            cursor.execute(
                'INSERT INTO professores (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)',
                (nome, email, cpf, senha_hash)
            )
            mysql.connection.commit()
            cursor.close()
            
            flash("Cadastro realizado com sucesso! Por favor, faça login.", "success")
            return redirect(url_for('login'))
            
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
            flash("Ocorreu um erro ao cadastrar. Por favor, tente novamente.", "error")
            
    return render_template('cadastro.html')

# =============================================
# ROTAS PRIVADAS (APENAS PARA PROFESSORES LOGADOS)
# =============================================

@app.route("/home")
@login_required
@professor_required
def home():
    """Página inicial após login"""
    return render_template('home.html')

@app.route("/cadastrar_aluno", methods=['GET', 'POST'])
@login_required
@professor_required
def cadastrar_aluno():
    """Rota para cadastro de alunos"""
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        serie = request.form.get('serie', '').strip()
        email = request.form.get('email', '').strip()
        senha = request.form.get('senha', '')
        
        # Validações
        if not all([nome, serie, email, senha]):
            flash("Por favor, preencha todos os campos", "error")
            return render_template('cadastrar_aluno.html')
            
        if not validar_email(email):
            flash("Formato de email inválido", "error")
            return render_template('cadastrar_aluno.html')
            
        try:
            senha_hash = generate_password_hash(senha, method='pbkdf2:sha256')
            cursor = mysql.connection.cursor()
            
            # Verifica se email já existe
            cursor.execute("SELECT id_aluno FROM alunos WHERE email = %s", (email,))
            if cursor.fetchone():
                flash("Este email já está cadastrado", "error")
                return render_template('cadastrar_aluno.html')
                
            # Insere novo aluno
            cursor.execute(
                'INSERT INTO alunos (nome, serie, email, senha) VALUES (%s, %s, %s, %s)',
                (nome, serie, email, senha_hash)
            )
            mysql.connection.commit()
            cursor.close()
            
            flash("Aluno cadastrado com sucesso!", "success")
            return redirect(url_for('cadastrar_aluno'))
            
        except Exception as e:
            print(f"Erro ao cadastrar aluno: {e}")
            flash("Ocorreu um erro ao cadastrar o aluno. Por favor, tente novamente.", "error")
            
    return render_template('cadastrar_aluno.html')

# =============================================
# ROTAS PARA LIVROS
# =============================================

@app.route("/buscar_livro", methods=['GET', 'POST'])
@login_required
@professor_required
def buscar_livro_google():
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        
        if not titulo:
            flash("Por favor, informe um título para busca", "error")
            return render_template('resultado_livro.html')
        
        url = f"https://www.googleapis.com/books/v1/volumes?q={titulo}"
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()
            
            if 'items' in dados:
                livro_info = dados['items'][0]['volumeInfo']
                isbn = next(
                    (isbn['identifier'] for isbn in livro_info.get('industryIdentifiers', []) 
                    if isbn['type'] == 'ISBN_13'
                ), 'Sem ISBN')
                
                livro = {
                    'titulo': livro_info.get('title', 'Sem título'),
                    'autor': ', '.join(livro_info.get('authors', ['Desconhecido'])),
                    'data': livro_info.get('publishedDate', ''),
                    'isbn': isbn,
                    'descricao': livro_info.get('description', 'Sem descrição disponível'),
                    'imagem': livro_info.get('imageLinks', {}).get('thumbnail', ''),
                    'link': livro_info.get('infoLink', '')
                }
                return render_template('resultado_livro.html', livro=livro)
        
        flash("Livro não encontrado", "error")
    
    return render_template('resultado_livro.html')

# =============================================
# ROTAS PARA LISTAGENS
# =============================================

@app.route('/lista_alunos')
@login_required
@professor_required
def lista_alunos():
    """Lista todos os alunos cadastrados"""
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id_aluno, nome, email, serie FROM alunos ORDER BY nome')
        alunos = cursor.fetchall()
        cursor.close()
        return render_template('lista_alunos.html', alunos=alunos)
    except mysql.connection.Error as e:
        print(f"Erro de banco de dados ao listar alunos: {e}")
        flash("Erro de conexão com o banco de dados. Tente novamente.", "error")
        return render_template('lista_alunos.html', alunos=[])  # Retorna lista vazia
    except Exception as e:
        print(f"Erro inesperado ao listar alunos: {e}")
        flash("Ocorreu um erro inesperado. Contate o administrador.", "error")
        return render_template('lista_alunos.html', alunos=[])  # Mantém na mesma página

@app.route('/lista_livros')
@login_required
@professor_required
def lista_livros():
    """Lista todos os livros cadastrados"""
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id_livro, titulo, autor FROM livros ORDER BY titulo')
        livros = cursor.fetchall()
        cursor.close()
        return render_template('lista_livros.html', livros=livros)
    except mysql.connection.Error as e:
        print(f"Erro de banco de dados ao listar livros: {e}")
        flash("Erro de conexão com o banco de dados. Tente novamente.", "error")
        return render_template('lista_livros.html', livros=[])
    except Exception as e:
        print(f"Erro inesperado ao listar livros: {e}")
        flash("Ocorreu um erro inesperado. Contate o administrador.", "error")
        return render_template('lista_livros.html', livros=[])

# =============================================
# ROTAS PARA EDIÇÃO E EXCLUSÃO
# =============================================

@app.route('/editar_aluno/<int:id_aluno>', methods=['GET', 'POST'])
@login_required
@professor_required
def editar_aluno(id_aluno):
    """Edita informações de um aluno"""
    try:
        cursor = mysql.connection.cursor()
        
        if request.method == 'POST':
            novo_nome = request.form.get('nome', '').strip()
            novo_email = request.form.get('email', '').strip()
            nova_serie = request.form.get('serie', '').strip()
            
            if not all([novo_nome, novo_email, nova_serie]):
                flash("Por favor, preencha todos os campos", "error")
                return redirect(url_for('editar_aluno', id_aluno=id_aluno))
                
            cursor.execute(
                'UPDATE alunos SET nome = %s, email = %s, serie = %s WHERE id_aluno = %s',
                (novo_nome, novo_email, nova_serie, id_aluno)
            )
            mysql.connection.commit()
            flash("Aluno atualizado com sucesso!", "success")
            return redirect(url_for('lista_alunos'))
            
        cursor.execute('SELECT id_aluno, nome, email, serie FROM alunos WHERE id_aluno = %s', (id_aluno,))
        aluno = cursor.fetchone()
        cursor.close()
        
        if not aluno:
            flash("Aluno não encontrado", "error")
            return redirect(url_for('lista_alunos'))
            
        return render_template('editar_aluno.html', aluno=aluno)
        
    except Exception as e:
        print(f"Erro ao editar aluno: {e}")
        flash("Ocorreu um erro ao editar o aluno", "error")
        return redirect(url_for('lista_alunos'))

@app.route('/deletar_aluno/<int:id_aluno>')
@login_required
@professor_required
def deletar_aluno(id_aluno):
    """Remove um aluno do sistema"""
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM alunos WHERE id_aluno = %s', (id_aluno,))
        mysql.connection.commit()
        cursor.close()
        flash("Aluno removido com sucesso", "success")
    except Exception as e:
        print(f"Erro ao deletar aluno: {e}")
        flash("Ocorreu um erro ao remover o aluno", "error")
    return redirect(url_for('lista_alunos'))

# =============================================
# ROTAS PARA EMPRÉSTIMOS
# =============================================

@app.route("/emprestimos", methods=['GET', 'POST'])
@login_required
@professor_required
def emprestimos():
    """Gerencia empréstimos de livros"""
    try:
        cursor = mysql.connection.cursor()
        
        if request.method == 'POST':
            id_aluno = request.form.get('aluno')
            id_livro = request.form.get('livro')
            data_devolucao_str = request.form.get('data_devolucao', '').strip()
            
            if not id_aluno or not id_livro:
                flash("Por favor, selecione um aluno e um livro", "error")
                return redirect(url_for('emprestimos'))
                
            data_emprestimo = date.today()
            data_devolucao = None
            
            if data_devolucao_str:
                try:
                    data_devolucao = datetime.strptime(data_devolucao_str, '%Y-%m-%d').date()
                except ValueError:
                    flash("Formato de data inválido", "error")
                    return redirect(url_for('emprestimos'))
            
            cursor.execute("""
                INSERT INTO emprestimos 
                (id_aluno, id_livro, data_emprestimo, data_devolucao, devolvido) 
                VALUES (%s, %s, %s, %s, %s)
            """, (id_aluno, id_livro, data_emprestimo, data_devolucao, data_devolucao is not None))
            
            mysql.connection.commit()
            flash("Empréstimo registrado com sucesso!", "success")
            return redirect(url_for('emprestimos'))
        
        # Para GET requests
        cursor.execute("SELECT id_aluno, nome FROM alunos ORDER BY nome")
        alunos = cursor.fetchall()
        
        cursor.execute("SELECT id_livro, titulo FROM livros WHERE id_livro NOT IN (SELECT id_livro FROM emprestimos WHERE devolvido = FALSE) ORDER BY titulo")
        livros = cursor.fetchall()
        
        cursor.close()
        return render_template('emprestimos.html', alunos=alunos, livros=livros)
        
    except Exception as e:
        print(f"Erro em empréstimos: {e}")
        flash("Ocorreu um erro ao processar o empréstimo", "error")
        return redirect(url_for('emprestimos'))
    
@app.route('/lista_emprestimos')
@login_required
@professor_required
def lista_emprestimos():
    """Lista todos os empréstimos com opções de filtro"""
    try:
        filtro = request.args.get('filtro', 'todos')
        pesquisa = request.args.get('pesquisa', '').strip()
        
        cursor = mysql.connection.cursor()
        query = """
            SELECT 
                e.id_emprestimos,
                a.nome as aluno_nome,
                l.titulo as livro_titulo,
                e.data_emprestimo,
                e.data_devolucao,
                e.devolvido,
                DATEDIFF(IFNULL(e.data_devolucao, CURDATE()), e.data_emprestimo) as dias_emprestado
            FROM emprestimos e
            JOIN alunos a ON e.id_aluno = a.id_aluno
            JOIN livros l ON e.id_livro = l.id_livro
        """
        conditions = []
        params = []
        
        if filtro == 'ativos':
            conditions.append("e.devolvido = FALSE")
        elif filtro == 'finalizados':
            conditions.append("e.devolvido = TRUE")
        
        if pesquisa:
            conditions.append("(a.nome LIKE %s OR l.titulo LIKE %s)")
            params.extend([f"%{pesquisa}%", f"%{pesquisa}%"])
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        query += " ORDER BY e.data_emprestimo DESC"
        
        cursor.execute(query, params)
        emprestimos = cursor.fetchall()
        
        for emp in emprestimos:
            emp['status'] = "Devolvido" if emp['devolvido'] else "Em empréstimo"
            if not emp['devolvido'] and emp['dias_emprestado'] > 14:
                emp['atraso'] = emp['dias_emprestado'] - 14
                emp['status'] = f"Em atraso ({emp['atraso']} dias)"
            else:
                emp['atraso'] = 0
        
        cursor.close()
        return render_template('lista_emprestimos.html', emprestimos=emprestimos, filtro_atual=filtro, pesquisa_atual=pesquisa)
    
    except mysql.connection.Error as e:
        print(f"Erro de banco de dados ao listar empréstimos: {e}")
        flash("Erro de conexão com o banco de dados. Tente novamente.", "error")
        return render_template('lista_emprestimos.html', emprestimos=[], filtro_atual=filtro, pesquisa_atual=pesquisa)
    except Exception as e:
        print(f"Erro inesperado ao listar empréstimos: {e}")
        flash("Ocorreu um erro inesperado. Contate o administrador.", "error")
        return render_template('lista_emprestimos.html', emprestimos=[], filtro_atual=filtro, pesquisa_atual=pesquisa)
    
@app.route('/cadastrar_livro', methods=['POST'])
@login_required
@professor_required
def cadastrar_livro():
    """Rota para cadastrar um novo livro no sistema"""
    try:
        titulo = request.form.get('titulo', '').strip()
        autor = request.form.get('autor', '').strip()
        isbn = request.form.get('isbn', '').strip()
        descricao = request.form.get('descricao', '').strip()
        capa = request.form.get('capa', '')
        data_publicacao = request.form.get('data_publicacao', '')

        print(f"Dados recebidos para cadastro:\nTítulo: {titulo}\nAutor: {autor}\nISBN: {isbn}")

        if not all([titulo, autor]):
            flash("Título e autor são obrigatórios", "error")
            return redirect(url_for('buscar_livro_google'))

        cursor = mysql.connection.cursor()
        
        try:
            # Verifica se livro já existe pelo ISBN (se fornecido)
            if isbn and isbn != 'Sem ISBN':
                cursor.execute("SELECT id_livro FROM livros WHERE isbn = %s", (isbn,))
                if cursor.fetchone():
                    flash("Um livro com este ISBN já está cadastrado", "error")
                    return redirect(url_for('buscar_livro_google'))

            # Insere novo livro com tratamento explícito de NULL
            cursor.execute(
                """INSERT INTO livros 
                (titulo, autor, isbn, descricao, capa, data_publicacao) 
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (
                    titulo, 
                    autor, 
                    isbn if isbn and isbn != 'Sem ISBN' else None, 
                    descricao if descricao and descricao != 'Sem descrição disponível' else None,
                    capa if capa else None, 
                    data_publicacao if data_publicacao else None
                )
            )
            mysql.connection.commit()
            
            # Verificação adicional
            cursor.execute("SELECT * FROM livros WHERE id_livro = LAST_INSERT_ID()")
            livro_inserido = cursor.fetchone()
            print("Livro inserido:", livro_inserido)
            
            if not livro_inserido:
                raise Exception("O livro não foi persistido no banco de dados")
            
            flash("Livro cadastrado com sucesso!", "success")
            return redirect(url_for('lista_livros'))
            
        except Exception as e:
            mysql.connection.rollback()
            raise e
            
        finally:
            cursor.close()
            
    except Exception as e:
        print(f"Erro ao cadastrar livro: {str(e)}")
        flash(f"Ocorreu um erro ao cadastrar o livro: {str(e)}", "error")
        return redirect(url_for('buscar_livro_google'))


@app.route('/editar_livro/<int:id_livro>', methods=['GET', 'POST'])
@login_required
@professor_required
def editar_livro(id_livro):
    """Edita informações de um livro"""
    try:
        cursor = mysql.connection.cursor()
        
        if request.method == 'POST':
            titulo = request.form.get('titulo', '').strip()
            autor = request.form.get('autor', '').strip()
            isbn = request.form.get('isbn', '').strip()
            descricao = request.form.get('descricao', '').strip()
            
            if not all([titulo, autor]):
                flash("Título e autor são obrigatórios", "error")
                return redirect(url_for('editar_livro', id_livro=id_livro))
                
            cursor.execute(
                """UPDATE livros SET 
                titulo = %s, 
                autor = %s, 
                isbn = %s, 
                descricao = %s 
                WHERE id_livro = %s""",
                (titulo, autor, isbn if isbn else None, descricao if descricao else None, id_livro)
            )
            mysql.connection.commit()
            flash("Livro atualizado com sucesso!", "success")
            return redirect(url_for('lista_livros'))
            
        # Para GET request
        cursor.execute('SELECT * FROM livros WHERE id_livro = %s', (id_livro,))
        livro = cursor.fetchone()
        cursor.close()
        
        if not livro:
            flash("Livro não encontrado", "error")
            return redirect(url_for('lista_livros'))
            
        return render_template('editar_livro.html', livro=livro)
        
    except Exception as e:
        print(f"Erro ao editar livro: {e}")
        flash("Ocorreu um erro ao editar o livro", "error")
        return redirect(url_for('lista_livros'))

@app.route('/deletar_livro/<int:id_livro>')
@login_required
@professor_required
def deletar_livro(id_livro):
    """Remove um livro do sistema"""
    try:
        cursor = mysql.connection.cursor()
        
        # Verifica se o livro está em algum empréstimo ativo
        cursor.execute('SELECT 1 FROM emprestimos WHERE id_livro = %s AND devolvido = FALSE', (id_livro,))
        if cursor.fetchone():
            flash("Não é possível deletar: livro está emprestado", "error")
            return redirect(url_for('lista_livros'))
            
        cursor.execute('DELETE FROM livros WHERE id_livro = %s', (id_livro,))
        mysql.connection.commit()
        cursor.close()
        flash("Livro removido com sucesso", "success")
    except Exception as e:
        print(f"Erro ao deletar livro: {e}")
        flash("Ocorreu um erro ao remover o livro", "error")
    return redirect(url_for('lista_livros'))
# =============================================
# CONFIGURAÇÕES FINAIS
# =============================================

@app.after_request
def add_security_headers(response):
    """Adiciona headers de segurança em todas as respostas"""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    