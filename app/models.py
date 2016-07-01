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

	def __init__(self, ci_user, sex, date_of_birth, marital_status, telephone, address):
		self.ci_user = ci_user

		self.sex = sex
		self.date_of_birth = date_of_birth
		self.marital_status = marital_status
		self.telephone = telephone
		self.address = address


	def __repr__(self):
		return '<DoctorProfile ci_user = %r>' % (self.ci_user)


class DoctorStudies(db.Model):
	__tablename__ = 'DoctorStudies'
	id = db.Column(db.Integer,primary_key = True)
	ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
	title =  db.Column(db.String(500))
	date_of_graduation = db.Column(db.Date)
	description =  db.Column(db.String(500))
	institution =  db.Column(db.String(500))

	def __init__(self, ci_user, title, date_of_graduation, description, institution):
		self.ci_user = ci_user
		self.title = title
		self.date_of_graduation = date_of_graduation
		self.description = description
		self.institution = institution

	def __repr__(self):
		return '<Doctor_Studies doctor: %r, title: %r>' % (self.ci_user, self.title)

class DoctorAbilities(db.Model):
	__tablename__ = 'DoctorAbilities'
	id = db.Column(db.Integer,primary_key = True)
	ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)

	title =  db.Column(db.String(500))
	description =  db.Column(db.String(500))

	def __init__(self, ci_user, title, description):
		self.ci_user = ci_user
		self.title = title
		self.description = description

	def __repr__(self):
		return '<Doctor_Abilities doctor: %r, title: %r>' % (self.ci_user, self.title)

class DoctorExperiences(db.Model):
	__tablename__ = 'DoctorExperiences'
	id = db.Column(db.Integer,primary_key = True)
	ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)

	title =  db.Column(db.String(500))
	date_of_start = db.Column(db.Date)
	date_of_finish = db.Column(db.Date)
	description =  db.Column(db.String(500))
	institution =  db.Column(db.String(500))

	def __init__(self, ci_user, title, date_of_start,date_of_finish, description, institution):
		self.ci_user = ci_user
		self.title = title
		self.date_of_start = date_of_start
		self.date_of_finish = date_of_finish
		self.description = description
		self.institution = institution

	def __repr__(self):
		return '<Doctor_Experiences doctor: %r, title: %r>' % (self.ci_user, self.title)

class DoctorAwards(db.Model):
	__tablename__ = 'DoctorAwards'
	id = db.Column(db.Integer,primary_key = True)
	ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)

	title =  db.Column(db.String(500))
	date = db.Column(db.Date)
	institution =  db.Column(db.String(500))

	def __init__(self, ci_user, title, date, institution):
		self.ci_user = ci_user
		self.title = title
		self.date = date
		self.institution = institution

	def __repr__(self):
		return '<Doctor_Awards doctor: %r, title: %r>' % (self.ci_user, self.title)

class DoctorPublications(db.Model):
	__tablename__ = 'DoctorPublications'
	
	id = db.Column(db.Integer,primary_key=True)
	ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
	
	title = db.Column(db.String(100))
	authors = db.Column(db.String(100))
	description = db.Column(db.String(500))
	magazine = db.Column(db.String(100))
	number = db.Column(db.String(5))
	volume = db.Column(db.String(5))
	date = db.Column(db.Date)

	def __init__(self, ci_user, title, authors, description, magazine, number, volume, date):
		self.ci_user = ci_user
		self.title = title
		self.authors = authors
		self.description = description
		self.magazine = magazine
		self.number = number
		self.volume = volume
		self.date = date

	def __repr__(self):
		return '<Doctor_Publications doctor: %r, title: %r>' % (self.ci_user, self.title)

class DoctorEvents(db.Model):
	__tablename__ = 'DoctorEvents'
	id = db.Column(db.Integer,primary_key = True)
	ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)

	title =  db.Column(db.String(500))
	date = db.Column(db.Date)
	description =  db.Column(db.String(500))
	institution =  db.Column(db.String(500))

	def __init__(self, ci_user, title, date, description, institution):
		self.ci_user = ci_user
		self.title = title
		self.date = date
		self.description = description
		self.institution = institution

	def __repr__(self):
		return '<Doctor_Events doctor: %r, title: %r>' % (self.ci_user, self.title)

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

class FamilyBackground(db.Model):
	__tablename__ = 'FamilyBackground'
	id = db.Column(db.Integer,primary_key = True)
	ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)

	asthma = db.Column(db.Boolean)	
	cancer = db.Column(db.Boolean)	
	heartdisease = db.Column(db.Boolean)	
	diabetes = db.Column(db.Boolean)	
	liverdisease = db.Column(db.Boolean)	
	hypertension = db.Column(db.Boolean)
	other = db.Column(db.String(500))

	def __init__(self,ci_user,asthma,cancer,heartdisease,diabetes,liverdisease,hypertension,other):
		self.ci_user = ci_user
		self.asthma = asthma
		self.cancer = cancer
		self.heartdisease = heartdisease
		self.diabetes = diabetes
		self.liverdisease = liverdisease
		self.hypertension = hypertension
		self.other = other

	def __repr__(self):
		return '<FamilyBackground ci_user = %r>' % (self.ci_user)

class PathologicalBackground(db.Model):
	__tablename__ = 'PathologicalBackground'

	id = db.Column(db.Integer,primary_key = True)
	ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)

	current_condition = db.Column(db.String(500))
	surgical_history = db.Column(db.String(500))
	transfusional_history = db.Column(db.String(500))
	allergies = db.Column(db.String(500))
	traumatic_history = db.Column(db.String(500))
	hospitalizations = db.Column(db.String(500))
	addictions = db.Column(db.String(500))
	other = db.Column(db.String(500))

	def __init__(self,ci_user,current_condition,surgical_history,transfusional_history,allergies,traumatic_history,hospitalizations,addictions,other):

		self.ci_user = ci_user
		self.current_condition = current_condition
		self.surgical_history = surgical_history
		self.transfusional_history = transfusional_history
		self.allergies = allergies
		self.traumatic_history = traumatic_history
		self.hospitalizations = hospitalizations
		self.addictions = addictions
		self.other = other

	def __repr__(self):
		return '<PathologicalBackground ci_user = %r>' % (self.ci_user)

class NonPathologicalBackground(db.Model):
	__tablename__ = 'NonPathologicalBackground'

	id = db.Column(db.Integer,primary_key = True)
	ci_user = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)

	defecation = db.Column(db.String(100))
	toothbrushing = db.Column(db.String(100))
	cigarrettes = db.Column(db.String(100))
	years = db.Column(db.String(100))
	beverages = db.Column(db.String(100))
	frecuency = db.Column(db.String(100))
	physical_activity = db.Column(db.String(500))
	frecuency2 = db.Column(db.String(100))
	other = db.Column(db.String(500))

	def __init__(self,ci_user,defecation,toothbrushing,cigarrettes,years,beverages,frecuency,physical_activity,frecuency2,other):
		self.ci_user=ci_user
		self.defecation=defecation
		self.toothbrushing=toothbrushing
		self.cigarrettes=cigarrettes
		self.years=years
		self.beverages=beverages
		self.frecuency=frecuency
		self.physical_activity = physical_activity
		self.frecuency2=frecuency2
		self.other=other

	def __repr__(self):
		return '<NonPathologicalBackground ci_user = %r>' % (self.ci_user)


class PatientConsultation(db.Model):
	__tablename__ = 'PatientConsultation'
	id = db.Column(db.Integer,primary_key = True)
	ci_patient = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
	ci_doctor = db.Column(db.Integer, db.ForeignKey('User.ci'), nullable=False)
	name_doctor = db.Column(db.String(500)) 
	date = db.Column(db.Date,nullable=False)
	motive = db.Column(db.String(500))
	symptoms = db.Column(db.String(500))

	def __init__(self,ci_patient,ci_doctor,name_doctor,date,motive,symptoms):
		self.ci_patient=ci_patient
		self.ci_doctor=ci_doctor
		self.name_doctor=name_doctor
		self.date=date
		self.motive=motive
		self.symptoms=symptoms

	def __repr__(self):
		return '<PatientConsultation ci_patient = %r ci_doctor = %r>' % (self.ci_patient,self.ci_doctor)


if __name__ == '__main__':
	manager.run()
db.create_all()  # Creamos la base de datos
