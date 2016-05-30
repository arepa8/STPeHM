import sys
sys.path.append('app/')

from models import *
import datetime

# Constantes
CONST_MIN			= 1
CONST_MAX_DESCR 	= 500
CONST_MAX_CI		= 999999999

class appointment():
	""" Controlador de Appointment """

	def insertAppointment(self,ciPatient,ciDoctor,date,description):
		check_ciPatient   = type(ciPatient)   == int
		check_ciDoctor    = type(ciDoctor)   == int
		#check_date		  = type(date) == datetime
		check_description = type(description) == str

		if check_ciPatient and check_ciDoctor and check_description:
			check_long_ciPatient = CONST_MIN <= ciPatient <= CONST_MAX_CI
			check_long_ciDoctor = CONST_MIN <= ciDoctor <= CONST_MAX_CI
			check_long_desc = CONST_MIN <= len(description) <= CONST_MAX_DESCR

			if check_long_ciPatient and check_long_ciDoctor and check_long_desc:
				new_a = Appointment(ciPatient,ciDoctor,date,description)
				db.session.add(new_a)
				db.session.commit()
				return True
		return False

	def modifyAppointment(self,id,date,description):
		check_description = type(description) == str

		if check_description:
			check_long_desc = CONST_MIN <= len(description) <= CONST_MAX_DESCR
			
			if check_long_desc:
				a = Appointment.query.filter_by(id = id).first()
				if a != None:
					a.date = date
					a.description = description
					db.session.commit()
					return True
		return False

	def deleteAppointment(self,id):
		check_id = type(id) == str

		if check_id:
			a = Appointment.query.filter_by(id =id).first()
			if a != None:
				db.session.delete(a)
				db.session.commit()
				return True
		return False

	def getAppointmentsByPatient(self,ci):
		check_ci = type(ci) == int and CONST_MIN <= ci <= CONST_MAX_CI

		if check_ci:
			appointments = Appointment.query.filter_by(patient=ci).all()
			return appointments
		return False

	def getAppointmentsByDoctor(self,ci):
		check_ci = type(ci) == int and CONST_MIN <= ci <= CONST_MAX_CI

		if check_ci:
			appointments = Appointment.query.filter_by(doctor=ci).all()
			return appointments
		return False
