from dbConnect import db_connect

conn,cur = db_connect()

def Create():
	cur.execute('CREATE DATABASE IF NOT EXISTS CONTATO;')
	conn.commit()
	cur.execute('USE contato')
	cur.execute('''CREATE TABLE IF NOT EXISTS contatos(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(50),
    assunto varchar(100),
    descricao varchar(500)
);''')
	conn.commit()
	cur.close()
	return 'Database chamado and Table chamados Created!'

Create()








