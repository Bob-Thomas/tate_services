from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/darwin'
# app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)