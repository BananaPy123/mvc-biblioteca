import MySQLdb

app = None

def init_app(flask_app):
    global app
    app = flask_app

def get_db():
    conexao = MySQLdb.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        passwd=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB']
    )
    cursor = conexao.cursor()
    return conexao, cursor
