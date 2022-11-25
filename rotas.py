from flask import Blueprint, render_template,request,redirect,url_for
from dbConnect import db_connect
conn,cur = db_connect()

first_route = Blueprint("first_route", __name__,static_folder='static',template_folder='templates')
second_route = Blueprint("second_route", __name__,static_folder='static',template_folder='templates')
third_route = Blueprint("third_route", __name__,static_folder='static',template_folder='templates')

@first_route.route('/')
def home():
  return render_template('index.html')

@second_route.route('/sobre')
def sobre():
  return render_template('sobre.html')


@third_route.route('/contato',methods=(['GET','POST']))
def contato():
  if request.method == 'POST':
    email = request.form['email']
    descricao = request.form['descricao']
    assunto = request.form['assunto']
    try:
      cur.execute('use contato')
      cur.execute(''' INSERT INTO contatos(email,assunto,descricao) VALUES(%s,%s,%s)''',(email,assunto,descricao))
      conn.commit()
    except Exception as e:
      print("Problem inserting into db: " + str(e))

    return redirect(url_for('third_route.contato'))
  return render_template('contato.html')

