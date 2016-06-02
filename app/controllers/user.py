import sys
sys.path.append('../')

from models import *

# Constantes
CONST_MAX_CI		= 999999999
CONST_MAX_USERNAME	= 50
CONST_MAX_PASSWORD	= 16
CONST_MAX_NAME_MAIL	= 255
CONST_MIN			= 1

class user():
	""" Controlador de User """

	def insertUser(self, ci, username, password, name, last_name, email,role):
		
		check_ci 		= (ci !=None) and (type(ci) == int)
		check_username	= (username !=None) and (type(username) == str)
		check_password	= (password!=None) and (type(password) == str) 
		check_name 		= (name !=None) and (type(name) == str)
		check_last_name = (last_name !=None) and (type(last_name) == str)
		check_email 	= (email !=None) and (type(email) == str) 

		if not(check_ci):
				return {'result':False, 'message':'Error en la cedula: Debe introducir un valor numerico' }

		if (check_ci and check_username and check_password and check_name and check_last_name and check_email):

			check_long_ci 		= CONST_MIN <= ci <= CONST_MAX_CI
			check_long_username = CONST_MIN <= len(username) <= CONST_MAX_USERNAME
			check_long_password = CONST_MIN <= len(password) <= CONST_MAX_PASSWORD
			check_long_name 	= CONST_MIN <= len(name) <= CONST_MAX_NAME_MAIL
			check_long_last_name= CONST_MIN <= len(last_name) <= CONST_MAX_NAME_MAIL
			check_long_email 	= CONST_MIN <= len(email) <= CONST_MAX_NAME_MAIL

			if not(check_long_ci):
				return {'result':False, 'message':'Error en la cedula: Debe intruducir un valor entre 1 y 999999999' }

			if not(check_long_username):
				return {'result':False, 'message':'Error en el nombre de usuario: Debe tener máximo 50 caracteres' }

			if not(check_long_password):
				return {'result':False, 'message':'Error en el contraseña: Debe tener máximo 16 caracteres' }

			if not(check_long_name):
				return {'result':False, 'message':'Error en el nombre: Debe tener máximo 255 caracteres' }

			if not(check_long_last_name):
				return {'result':False, 'message':'Error en el apellido: Debe tener máximo 255 caracteres' }

			if not(check_long_email):
				return {'result':False, 'message':'Error en el correo: Debe tener máximo 255 caracteres' }

			
			check_if_exist = User.query.filter_by(username=username).first()

			if check_if_exist != None:
				return {'result':False, 'message':'El nombre de usuario ya esta registrado' }

			check_if_exist = User.query.filter_by(ci=ci).first()

			if check_if_exist != None:
				return {'result':False, 'message':'La cedula ya esta registrada' }

			check_if_exist = User.query.filter_by(email=email).first()

			if check_if_exist != None:
				return {'result':False, 'message':'El correo electronico ya esta registrado' }

			else:
				
				new_user = User(ci,username,password,name,last_name,email,role)
				db.session.add(new_user)
				db.session.commit()
				return {'result':True, 'message':'Usted ha sido registrado exitosamente'}

		else :
			return {'result':False, 'message':'Asegurese de llenar todos los campos' }

		return  {'result':False, 'message':'Lo lamentamos! Ha ocurrido un error, intentelo mas tarde' }


	def getUser(self, username):
		
		check_if_exist = self.existUser(username)

		if (check_if_exist):
			result = User.query.filter_by(username=username).first()
			return result
		return []

	def getUserByCi(self, ci):
		
		check_if_exist = self.existUserCi(ci)

		if (check_if_exist):
			result = User.query.filter_by(ci=ci).first()
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
		check_if_exist = None
		if (check_username and check_long_username):
			check_if_exist = User.query.filter_by(username=username).first()

		return check_if_exist != None

	def existUserCi(self, ci):
		check_ci	= type(ci) == int
		check_long_ci = 0 <= ci <= CONST_MAX_CI
		check_if_exist = None
		if (check_ci and check_long_ci):
			check_if_exist = User.query.filter_by(ci=ci).first()

		return check_if_exist != None

	def updateUser(self,username, password, name, last_name, email, role):
		
		check_password	= (type(password) == str) 
		check_name 		= (name !=None) and (type(name) == str)
		check_last_name = (last_name !=None) and (type(last_name) == str)
		check_email 	= (email !=None) and (type(email) == str) 

		if (check_password and check_name and check_last_name and check_email):

			check_long_password = CONST_MIN <= len(password) <= CONST_MAX_PASSWORD
			check_long_name 	= CONST_MIN <= len(name) <= CONST_MAX_NAME_MAIL
			check_long_last_name= CONST_MIN <= len(last_name) <= CONST_MAX_NAME_MAIL
			check_long_email 	= CONST_MIN <= len(email) <= CONST_MAX_NAME_MAIL

			
			if not(check_long_password):
				return {'result':False, 'message':'Error en el contraseña: Debe tener máximo 16 caracteres' }

			if not(check_long_name):
				return {'result':False, 'message':'Error en el nombre: Debe tener máximo 255 caracteres' }

			if not(check_long_last_name):
				return {'result':False, 'message':'Error en el apellido: Debe tener máximo 255 caracteres' }

			if not(check_long_email):
				return {'result':False, 'message':'Error en el correo: Debe tener máximo 255 caracteres' }

			check_if_exist = self.existUser(username)

			if (check_if_exist):

				user = User.query.filter_by(username=username).first()
				user[0].password = password
				user[0].name 	 = name
				user[0].last_name= last_name
				user[0].email 	 = user.email
				user[0].role	 = role
				db.session.commit()
				return {'result':True, 'message':'Usuario actualizado exitosamente'}

		else :
			return {'result':False, 'message':'Asegurese de llenar todos los campos' }

		return  {'result':False, 'message':'Lo lamentamos! Ha ocurrido un error, intentelo mas tarde' }
