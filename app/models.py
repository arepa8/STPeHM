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
    elements = db.relationship('InstitutionElement', backref='institution',
                                lazy='dynamic')

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return '<Institution name: %r>' % (self.name)

class InstitutionElement(db.Model):
    __tablename__ = 'InstitutionElement'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    institution_id = db.Column(db.Integer, db.ForeignKey('Institution.id'))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<InstitutionElement name: %r>' % (self.name)


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

class DoctorProfile(db.Model):
    __tablename__ = 'DoctorProfile'
    id = db.Column(db.Integer,primary_key = True)
    ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    
    sex = db.Column(db.String(10))
    date_of_birth = db.Column(db.Date)
    marital_status = db.Column(db.String(15))
    telephone = db.Column(db.String(15))
    address = db.Column(db.String(100))

    habilities = db.Column(db.String(500))
    pregrade = db.Column(db.String(100))
    postgrade = db.Column(db.String(100))
    experience =db.Column(db.String(500))
    courses = db.Column(db.String(500))
    publications = db.Column(db.String(500))
    awards = db.Column(db.String(500))

    def __init__(self, ci_user, sex, date_of_birth, marital_status, telephone, address,
        habilities, pregrade, postgrade, experience, courses, publications, awards):
        self.ci_user = ci_user

        self.sex = sex
        self.date_of_birth = date_of_birth
        self.marital_status = marital_status
        self.telephone = telephone
        self.address = address

        self.habilities = habilities
        self.pregrade = pregrade
        self.postgrade = postgrade
        self.experience = experience
        self.courses = courses
        self.publications = publications
        self.awards = awards

    def __repr__(self):
        return '<DoctorProfile ci_user = %r>' % (self.ci_user)

class Doctor_Ability(db.Model):
    __tablename__ = 'DoctorAbility'
    id = db.Column(db.Integer, primary_key=True)
    ci_doctor = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    ability = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(100))

    def __init__(self, ci_doctor, ability, description):
        self.ci_doctor = ci_doctor
        self.ability = ability
        self.description = description

class Doctor_Publication(db.Model):
    __tablename__ = 'DoctorPublication'

    id = db.Column(db.Integer, primary_key=True)
    ci_doctor = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    publication = db.Column(db.String(500), nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.String(100))
    
    def __init__(self, ci_doctor, publication, date, description):
        self.ci_doctor = ci_doctor
        self.publication = publication
        self.date = date
        self.description = description

class Doctor_Study(db.Model):
    __tablename__ = 'DoctorStudy'

    id = db.Column(db.Integer, primary_key=True)
    ci_doctor = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    study = db.Column(db.String(500), nullable=False)
    date_of_graduation = db.Column(db.Date)
    description = db.Column(db.String(100))
    institution = db.Column(db.String(500), nullable=False)

    def __init__(self, ci_doctor, study, date_of_graduation, description, institution):
        self.ci_doctor = ci_doctor
        self.study = study
        self.date_of_graduation = date_of_graduation
        self.description = description
        self.institution = institution

class Doctor_Award(db.Model):
    __tablename__ = 'DoctorAward'

    id = db.Column(db.Integer, primary_key=True)
    ci_doctor = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    award = db.Column(db.String(500), nullable=False)
    date = db.Column(db.Date)
    institution = db.Column(db.String(500), nullable=False)

    def __init__(self, ci_doctor, award, date, institution):
        self.ci_doctor = ci_doctor
        self.award = award
        self.date = date
        self.institution = institution
        
class Doctor_Event(db.Model):
    __tablename__ = 'DoctorEvent'

    id = db.Column(db.Integer, primary_key=True)
    ci_doctor = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    event = db.Column(db.String(500), nullable=False)
    date = db.Column(db.Date)
    institution = db.Column(db.String(500), nullable=False)
    description =db.Column(db.String(100))

    def __init__(self, ci_doctor, event, date, institution, description):
        slef.ci_doctor = ci_doctor
        self.event = event
        self.institution = institution
        self.description = description
        
class Doctor_Experience(db.Model):
    __tablename__ = 'DoctorExperience'

    id = db.Column(db.Integer, primary_key=True)
    ci_doctor = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    experience = db.Column(db.String(500), nullable=False)
    date_of_start = db.Column(db.Date)
    date_of_finish = db.Column(db.Date)
    institution = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(100))

    def __init__(self, ci_doctor, experience, date_of_start, date_of_finish, institution, description):
        self.ci_doctor = ci_doctor
        self.experience = experience
        self.date_of_start = date_of_start
        self.date_of_finish = date_of_finish
        self.institution = institution
        self.description = description

class PatientProfile(db.Model):
    __tablename__ = 'PatientProfile'
    id = db.Column(db.Integer,primary_key = True)
    ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
    
    sex = db.Column(db.String(10))
    date_of_birth = db.Column(db.Date)
    marital_status = db.Column(db.String(15))
    telephone = db.Column(db.String(15))
    address = db.Column(db.String(100))
    
    heigth = db.Column(db.String(15))
    weigth =  db.Column(db.String(15))
    blood_type = db.Column(db.String(2))
    diabetic = db.Column(db.String(1))
    allergies = db.Column(db.String(500))
    emergency_contact = db.Column(db.String(100))
    emergency_number = db.Column(db.String(15))
    comments =  db.Column(db.String(500))

    def __init__(self, ci_user, sex, date_of_birth, marital_status, telephone, address,
        heigth, weigth, blood_type, diabetic, allergies, emergency_contact, emergency_number,comments):
        self.ci_user = ci_user

        self.sex = sex
        self.date_of_birth = date_of_birth
        self.marital_status = marital_status
        self.telephone = telephone
        self.address = address

        self.heigth = heigth
        self.weigth = weigth
        self.blood_type = blood_type
        self.diabetic = diabetic
        self.allergies = allergies
        self.emergency_contact = emergency_contact
        self.emergency_number = emergency_number
        self.comments = comments

    def __repr__(self):
        return '<PatientProfile ci_user = %r>' % (self.ci_user)


if __name__ == '__main__':
	manager.run()
db.create_all()  # Creamos la base de datos
