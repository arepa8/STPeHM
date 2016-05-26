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

	def insertAppointment(self,ci,date,description):
		check_ci 		  = type(ci)   == int
		#check_date		  = type(date) == datetime
		check_description = type(description) == str

		if check_ci and check_description:
			check_long_ci = CONST_MIN <= ci <= CONST_MAX_CI
			check_long_desc = CONST_MIN <= len(description) <= CONST_MAX_DESCR

			if check_long_ci and check_long_desc:
				new_a = Appointment(ci,date,description)
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

	def getAppointments(self,ci):
		check_ci = type(ci) == int and CONST_MIN <= ci <= CONST_MAX_CI

		if check_ci:
			appointments = Appointment.query.filter_by(user=ci).all()
			return appointments
		return False


