# -*- coding: utf-8 -*-.

# Se importan las librerias necesarias.
import os

from flask                 import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *

# Conexion con la base de datos.
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'apl.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Instancia de la aplicacion.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# Instancia de la base de datos.
db = SQLAlchemy(app)

# Model
class Blog(db.Model):
    __tablename__ = 'Blog'
    __mapper_args__ = dict(order_by="date desc")

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Unicode(255))
    author = db.Column(db.Unicode(255))
    date = db.Column(db.DateTime())
    content = db.Column(db.Text())

db.create_all()  # Creamos la base de datos