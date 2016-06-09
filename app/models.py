# -*- coding: utf-8 -*-.

# Se importan las librerias necesarias.
import os

from flask         import Flask
from flask.ext.script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import *

# Conexion con la base de datos.
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'apl.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Instancia de la aplicacion.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# Instancia de la base de datos.
db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Model
class User(db.Model):
    __tablename__ = 'User'

    ci = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(16))
    name = db.Column(db.String(255),nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False, unique=True)
    role    = db.Column(db.String(255), db.ForeignKey('Role.id'))
    #birthday = db.Column(db.DATE,nullable=False)
    #appointments = db.relationship('Appointment', backref='user', lazy='dynamic')


    def __init__(self,ci,username,password,name,last_name,email,role):
        self.ci = ci
        self.username = username
        self.password = password
        self.name = name
        self.last_name = last_name
        self.email = email  
        self.role = role  
        #self.birthday = birthday
	
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.username)


class Role(db.Model):
    __tablename__ = 'Role'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255),nullable=False,unique=True)
    users = db.relationship('User', backref='role_id', lazy='dynamic')

    def __init__(self,role_name):
        self.role_name = role_name
    
    def __repr__(self):
        return '<Role %r>' % (self.role_name)

class Appointment(db.Model):
    __tablename__ = 'Appointment'

    id = db.Column(db.Integer,primary_key = True)
    patient = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    doctor = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    date = db.Column(db.Date,nullable=False)
    description = db.Column(db.String(500),nullable=False)

    def __init__(self,patient,doctor,date,description):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.description = description

    def __repr__(self):
        return '<Appointment patient: %r, doctor: %r, date: %r>' % (self.patient, self.doctor, self.date)

class Institution(db.Model):
    __tablename__ = 'Institution'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255),nullable=False,unique=True)
    address = db.Column(db.String(255),nullable=False,unique=True)

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return '<Institution name: %r>' % (self.name)

class Specialization(db.Model):
    __tablename__ = 'Specialization'

    id = db.Column(db.Integer,primary_key = True)
    speciality = db.Column(db.String(255),nullable=False,unique=True)

    def __init__(self, speciality):
        self.speciality = speciality

    def __repr__(self):
        return '<Specialization %r>' % (self.speciality)

class Doctor_Specialization(db.Model):
    __tablename__ = 'Doctor_Specialization'

    id = db.Column(db.Integer,primary_key = True)
    doctor = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    speciality = db.Column(db.Integer, db.ForeignKey('Specialization.id'), nullable=False)

    def __init__(self, doctor, speciality):
        self.doctor = doctor
        self.speciality = speciality

    def __repr__(self):
        return '<Doctor_Specialization doctor: %r, speciality: %r>' % (self.doctor, self.speciality)

class Profile(object):
    __tablename__ = 'Profile'

    id = db.Column(db.Integer,primary_key = True)
    ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    name = db.Column(db.String(255),nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False, unique=True)
    id_institution = db.Column(db.Integer, db.ForeignKey('Institution.id'))

    def __init__(self, ci_user, name, last_name, email, id_institution, id_speciality):
        self.ci_user = ci_user
        self.name = name
        self.last_name = last_name
        self.email = email
        self.id_institution = id_institution

    def __repr__(self):
        return '<Profile ci_user = %r, name = %r, last_name = %r>' % (self.ci_user, self.name, self.last_name)

if __name__ == '__main__':
	manager.run()
db.create_all()  # Creamos la base de datos
