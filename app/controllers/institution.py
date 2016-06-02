import sys
sys.path.append('app/')

from models import *

# Constantes

CONST_MIN_LENGTH = 1
CONST_MAX_LENGTH = 255

class institution():
	""" Controlador de Institution """ 

	def insertInstitution(self, name, address):
		check_name 		= (name != None) and (type(name) == str)
		check_address	= (address != None) and (type(address) == str)
		if check_name and check_address:
			check_len_name 		= CONST_MIN_LENGTH <= len(name) <= CONST_MAX_LENGTH
			check_len_address	= CONST_MIN_LENGTH <= len(address) <= CONST_MAX_LENGTH
			if check_len_name and check_len_address:
				check_if_name_exists = Institution.query.filter_by(name=name).first()
				check_if_address_exists = Institution.query.filter_by(address=address).first()
				if not(check_if_name_exists or check_if_address_exists):
					new_i = Institution(name, address)
					db.session.add(new_i)
					db.session.commit()
					return True
				else:
					return ('El nombre y la dirección deben ser únicos.')
		return False

	def modifyInstitution(self, id, name, address):
		check_name 		= (name != None) and (type(name) == str)
		check_address	= (address != None) and (type(address) == str)
		if check_name and check_address:
			check_len_name 		= CONST_MIN_LENGTH <= len(name) <= CONST_MAX_LENGTH
			check_len_address	= CONST_MIN_LENGTH <= len(address) <= CONST_MAX_LENGTH
			if check_len_name and check_len_address:
				check_if_name_exists = None
				check_if_address_exists = None
				i = Institution.query.filter_by(id=id).first()
				if (i.name != name):
					check_if_name_exists = Institution.query.filter_by(name=name).first()
				if (i.address != address):
					check_if_address_exists = Institution.query.filter_by(address=address).first()
				if not(check_if_name_exists or check_if_address_exists):
					i.name = name
					i.address = address
					db.session.commit()
					return True
				else:
					return ('El nombre y la dirección no pueden ser duplicados.')
		return False

	def deleteInstitution(self, id):
		check_id = (id != None) and type(id) == int
		if check_id:
			i = Institution.query.filter_by(id=id).first()
			if i:
				db.session.delete(i)
				db.session.commit()
				return True
		return False

	def getInstitutionByName(self, name):
		check_name 		= (name != None) and (type(name) == str)
		if check_name:
			i = Institution.query.filter_by(name=name).first()
			return i 
		return None

	def getInstitutionByName(self, id):
		check_id 		= (id != None) and (type(id) == int)
		if check_id:
			i = Institution.query.filter_by(id=id).first()
			return i 
		return None

	def getAllInstitutions(self):
		return Institution.query.all()