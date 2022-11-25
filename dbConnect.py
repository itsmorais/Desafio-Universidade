from flask import Flask
from flaskext.mysql import MySQL

def db_connect():
  mysql = MySQL()
  app = Flask(__name__)
  mysql.init_app(app)


  app.config['MYSQL_DATABASE_HOST	'] = 'localhost'
  app.config['MYSQL_DATABASE_PORT'] = 3306
  app.config['MYSQL_DATABASE_USER'] = 'root'
  app.config['MYSQL_DATABASE_PASSWORD	'] = '1234'
  mysql = MySQL(app)

  conn = mysql.connect()
  cur = conn.cursor()
  return conn,cur








