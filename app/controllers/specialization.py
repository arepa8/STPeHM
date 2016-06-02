import sys
sys.path.append('app/')

from models import *

# Constantes

CONST_MIN_LENGTH = 1
CONST_MAX_LENGTH = 255

class specialization():
	""" Controlador de Specialization """
	def insertSpecialization(self, speciality):
		check_speciality = (speciality != None) and (type(speciality) == str)
		if check_speciality:
			check_len_speciality = CONST_MIN_LENGTH <= len(speciality) <= CONST_MAX_LENGTH
			if check_len_speciality:
				check_if_exists = Specialization.query.filter_by(speciality=speciality).first()
				if not(check_if_exists):
					s = Specialization(speciality)
					db.session.add(s)
					db.session.commit()
					return True
		return False

	def modifySpecialization(self, id, speciality):
		check_speciality = (speciality != None) and (type(speciality) == str)
		if check_speciality:
			check_len_speciality = CONST_MIN_LENGTH <= len(speciality) <= CONST_MAX_LENGTH
			if check_len_speciality:
				check_if_exists = Specialization.query.filter_by(speciality=speciality).first()
				if not(check_if_exists):
					s = Specialization.query.filter_by(id=id).first()
					s.speciality = speciality
					db.session.commit()
					return True
		return False

	def deleteSpecialization(self, id):
		check_id = (id != None) and (type(id) == int)
		if check_id:
			s = Specialization.query.filter_by(id=id).first()
			if s:
				db.session.delete(s)
				db.session.commit()
				return True
		return False

	def getSpecializationByID(self, id):
		check_id 		= (id != None) and (type(id) == int)
		if check_id:
			s = Specialization.query.filter_by(id=id).first()
			return s
		return None

	def getSpecializationBySpeciality(self, speciality):
		check_id 		= (id != None) and (type(id) == int)
		if check_id:
			s = Specialization.query.filter_by(speciality=speciality).first()
			return s
		return None

	def getAllSpecializations(self):
		return Specialization.query.all()