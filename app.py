from flask import Flask
from dbConnect import db_connect
from createDB import Create
from rotas import first_route,second_route,third_route
app = Flask(__name__)

conn,cur = db_connect()

app.register_blueprint(first_route,url_prefix='/')
app.register_blueprint(second_route,url_prefix='/sobre')
app.register_blueprint(third_route,url_prefix='/contato')



app.run(debug=True)