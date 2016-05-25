import sys
sys.path.append('app/')

from models import *

# Constantes
CONST_MIN_ROLE_NAME = 0
CONST_MAX_ROLE_NAME	= 255

class role():
	""" Controlador de Role """

	def createRole(self, new_id, role_name):
		check_role_name = type(role_name) == str
		
		if (check_role_name):

			check_long_role_name= CONST_MIN_ROLE_NAME <= len(role_name) <= CONST_MAX_ROLE_NAME

			if (check_long_role_name):
				
				check_if_exist = Role.query.filter_by(role_name=role_name).first()

				if (check_if_exist != []):

					new_role = Role(role_name)
					db.session.add(new_role)
					db.session.commit()
					return True
		return False

	def assingRole():
		pass

	def updateRole():
		pass

	def deleteRole():
		pass

	def getRole():
		pass
