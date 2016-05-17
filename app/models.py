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
class User(db.Model):
    __tablename__ = 'User'

    ci = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False)
    #birthday = db.Column(db.DATE,nullable=False)

    def __init__(self,ci,name,last_name,email):
        self.ci = ci
        self.name = name
        self.last_name = last_name
        self.email = email
        #self.birthday = birthday

db.create_all()  # Creamos la base de datos