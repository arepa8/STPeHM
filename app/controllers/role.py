import sys
sys.path.append('app/')

from models import *

# Constantes
CONST_MIN_ID = 1
CONST_MAX_ID = sys.maxsize
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

	def updateRole(self, targte_id, role_name):
		check_target_id 	= type(check_target_id) == int
		check_long_target_id= CONST_MIN_ID <= target_id <= CONST_MAX_ID
		check_role_name 	= type(role_name) == str
		check_long_role_name= CONST_MIN_ROLE_NAME <= len(role_name) <= CONST_MAX_ROLE_NAME
		
		if (check_target_id and check_long_target_id and check_role_name and check_long_role_name):

			role = Role.query.filter_by(id=target_id).first()
			
			if (role != []):
				role[0].id 		 = target_id
				role[0].role_name= role_name
				db.session.commit()
				return True
		return False

	def deleteRole():
		pass

	def getRole(self, target_id):
		check_target_id = type(check_target_id) == int
		check_long_target_id = CONST_MIN_ID <= target_id <= CONST_MAX_ID

		if (check_target_id and check_long_target_id):
			role = Role.query.filter_by(id=target_id).first()
			return role 

