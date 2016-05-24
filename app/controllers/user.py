import sys
sys.path.append('app/')

from models import *

# Constantes
CONST_MAX_CI		= 999999999
CONST_MAX_USERNAME	= 50
CONST_MAX_PASSWORD	= 16
CONST_MAX_NAME_MAIL	= 255
CONST_MIN			= 1

class user():
	""" Controlador de User """

	def insertUser(self, ci, username, password, name, last_name, email):
		
		check_ci 		= type(ci) == int
		check_username	= type(username) == str
		check_password	= type(password) == str 
		check_name 		= type(name) == str
		check_last_name = type(last_name) == str
		check_email 	= type(email) == str 

		if (check_ci and check_username and check_password and check_name and check_last_name and check_email):

			check_long_ci 		= CONST_MIN <= len(ci) <= CONST_MAX_CI
			check_long_username = CONST_MIN <= len(username) <= CONST_MAX_USERNAME
			check_long_password = CONST_MIN <= len(password) <= CONST_MAX_PASSWORD
			check_long_name 	= CONST_MIN <= len(name) <= CONST_MAX_NAME_MAIL
			check_long_last_name= CONST_MIN <= len(last_name) <= CONST_MAX_NAME_MAIL
			check_long_email 	= CONST_MIN <= len(email) <= CONST_MAX_NAME_MAIL

			if (check_long_ci and check_long_username and check_long_password and check_long_name and check_long_last_name and check_long_email):

				check_if_exist = User.query.filter_by(username=username).first()

				if check_if_exist != []:

					new_user = User(ci,username,password,name,last_name,email)
					db.session.add(new_user)
					db.session.commit()
					return True
		return False

	def getUser(self, username):
		
		check_if_exist = self.existUser(username)

		if (check_if_exist):
			result = User.query.filter_by(username=username).first()
			return result
		return []

	def deleteUser(self, username):
		
		check_username = (type(username) == str) and (CONST_MIN <= len(username) <= CONST_MAX_USERNAME)

		if check_username:
			check_if_exist = self.existUser(username)
			if check_if_exist:
				user = User.query.filter_by(username=username).first()
				db.session.delete(user)
				db.session.commit()
				return True
		return False

	def existUser(self, username):
		check_username	= type(username) == str
		check_long_username = CONST_MIN <= len(username) <= CONST_MAX_USERNAME

		if (check_username and check_long_username):
			check_if_exist = User.query.filter_by(username=username).first()

		return check_if_exist != []

	def updateUser(self, ci, username, password, name, last_name, email):
		check_ci 		= type(ci) == int
		check_username	= type(username) == str
		check_password	= type(password) == str 
		check_name 		= type(name) == str
		check_last_name = type(last_name) == str
		check_email 	= type(email) == str 

		if (check_ci and check_username and check_password and check_name and check_last_name and check_email):

			check_long_ci 		= CONST_MIN <= len(ci) <= CONST_MAX_CI
			check_long_username = CONST_MIN <= len(username) <= CONST_MAX_USERNAME
			check_long_password = CONST_MIN <= len(password) <= CONST_MAX_PASSWORD
			check_long_name 	= CONST_MIN <= len(name) <= CONST_MAX_NAME_MAIL
			check_long_last_name= CONST_MIN <= len(last_name) <= CONST_MAX_NAME_MAIL
			check_long_email 	= CONST_MIN <= len(email) <= CONST_MAX_NAME_MAIL

			if (check_long_ci and check_long_username and check_long_password and check_long_name and check_long_last_name and check_long_email):

				check_if_exist = self.existUser(username)

				if (check_if_exist):

					user = self.getUser(username)
					user.ci 		= ci
					user.usename 	= username
					user.password 	= password
					user.name 		= name
					user.last_name 	= last_name
					user.email 		= user.email
					db.session.commit()
					return True
		return False