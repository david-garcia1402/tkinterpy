<<<<<<< HEAD
#importar o banco de dados SQLite
import sqlite3 as lite

#criando a conexão SQLite
con = lite.connect('Dados.db') #nome do banco de dados

#criando tabela
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT,'
                'data_da_compra DATE, valor_da_compra DECIMAL, n_serie TEXT, imagem TEXT)')

=======
#importar o banco de dados SQLite
import sqlite3 as lite

#criando a conexão SQLite
con = lite.connect('Dados.db') #nome do banco de dados

#criando tabela
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT,'
                'data_da_compra DATE, valor_da_compra DECIMAL, n_serie TEXT, imagem TEXT)')

>>>>>>> a2d40a8fa97ddd9659171b53b9bdcf0a19709ed3
