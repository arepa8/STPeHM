import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from user import *
from role import *

class TestUser(unittest.TestCase):

  ###########################################      
  #         Pruebas para insertUser         #
  ###########################################

  #se prueba funcionalidad sin asserts
	def testInsertUser(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
	#se prueba funcionalidad con assert
	def testInsertUserTrue(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertTrue(result['result'])
	#pruebas sobre ci#
	def testInsertCInotNumeric(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser('12345678','user','pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertCItooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(1000000000,'user','pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertCInull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(None,'user','pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertCIalredyExists(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(666666,'user1','pass1','name1','last1','test1@gmail.com','rol')
		result = user_controller.insertUser(666666,'user2','pass2','name2','last2','test2@gmail.com','rol')
		user_controller.deleteUser('user1')
		user_controller.deleteUser('user2')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
		#pruebas sobre username#
	def testInsertUsernameNotStr(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,1,'pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertUsernameTooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'ImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlong','pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertUsernameNoLenght(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'','pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertUsernameNull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,None,'pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertUsernameAlreadyExists(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(666666,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.insertUser(6666666,'user','pass2','name2','last2','test2@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	#pruebas sobre correo#
	def testInsertMailNotStr(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','name','last',1,'rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertMailTooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','name','last','ImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'Imtoodamnlong@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertMailNoLenght(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','name','last','','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertMailNull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','name','last',None,'rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertMailAlreadyExists(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(666666,'user1','pass1','name1','last1','test@gmail.com','rol')
		result = user_controller.insertUser(6666666,'user2','pass2','name2','last2','test@gmail.com','rol')
		user_controller.deleteUser('user1')
		user_controller.deleteUser('user2')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	#pruebas sobre password#
	def testInsertPasswordNotStr(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user',1,'name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertPasswordTooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','Imtoodamnloooooong','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertPasswordNoLenght(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertPasswordNull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user',None,'name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	#pruebas sobre name#
	def testInsertNameNotStr(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass',1,'last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertNameTooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','ImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'Imtoodamnloooooooooooooooo','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertNameNoLenght(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertNameNull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass',None,'last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	#pruebas sobre last_name#
	def testInsertLastNameNotStr(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','name',1,'test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertLastNameTooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','name','ImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'Imtoodamnloooooooooooooooo','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertLastNameNoLenght(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','name','','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
	def testInsertLastNameNull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(666666,'user','pass','name',None,'test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result['result'])
  ###########################################      
  #         Pruebas para existUser         #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testExistUser(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		user_controller.existUser('user')
	#se prueba funcionalidad con asserts
	def testExistUserTrue(self): #exists
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.existUser('user')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertTrue(result)
	def testExistUserFalse(self): #do not exists
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.existUser('user666')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result)
  ###########################################      
  #         Pruebas para existUserCi        #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testExistUserCi(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		user_controller.existUserCi(12345678)
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
	#se prueba funcionalidad con asserts
	def testExistUserCiTrue(self): #exists
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.existUserCi(12345678)
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertTrue(result)
	def testExistUserCiFalse(self): #do not exists
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.existUserCi(666666)
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result)
	def testExistUserCiNotValidArgument(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.existUser('12345678')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result)
  ###########################################      
  #         Pruebas para getUser           #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetUser(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		user_controller.getUser('user')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
	#se prueba funcionalidad con asserts
	def testGetUserTrue(self): #exists get it
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.getUser('user')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertEqual(result.username,'user')
	def testGetUserFalse(self): #dont exists return empty list
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.getUser('user666')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertEqual(result,[])
  ###########################################      
  #         Pruebas para getUserByCi          #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetUserByCi(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		user_controller.getUserByCi(12345678)
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
	#se prueba funcionalidad con asserts
	def testGetUserCiTrue(self): #exists get it
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.getUserByCi(12345678)
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertEqual(result.username,'user')
	def testGetUserFalse(self): #dont exists return empty list
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.getUserByCi(666666)
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertEqual(result,[])
  ###########################################      
  #         Pruebas para deleteUser         #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testDeleteUser(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
	#se prueba funcionalidad con asserts
	def testDeleteUserTrue(self): #exists delete it
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.deleteUser('user')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertTrue(result)
	def testDeleteUserFalse(self): #dont exists dont delete
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		result = user_controller.deleteUser('user666')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		self.assertFalse(result)
  ###########################################      
  #         Pruebas para updateUser         #
  ###########################################

  #se prueba funcionalidad sin asserts
	def testUpdateUser(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		user_controller.updateUser('user','pass1','name1','last1','test1@gmail.com','rol2')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
	#se prueba funcionalidad con assert
	def testUpdateUserTrue(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result =user_controller.updateUser('user','pass1','name1','last1','test1@gmail.com','rol2')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertTrue(result['result'])
	#pruebas sobre correo#
	def testUpdateUserMailNotStr(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result =user_controller.updateUser('user','pass1','name1','last1',1,'rol2')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserMailTooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass','name','last','ImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'Imtoodamnlong@gmail.com','rol2')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserMailNoLenght(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass','name','last','','rol2')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserMailNull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass','name','last',None,'rol2')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	#pruebas sobre password#
	def testUpdateUserPasswordNotStr(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user',1,'name','last','test2@gmail.com','rol2')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserPasswordTooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','Imtoodamnloooooong','name','last','test@gmail.com','rol1')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserPasswordNoLenght(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','','name','last','test@gmail.com','rol1')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserPasswordNull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user',None,'name','last','test@gmail.com','rol1')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	#pruebas sobre name#
	def testUpdateUserNameNotStr(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass',1,'last','test@gmail.com','rol1')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserNameTooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass','ImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'Imtoodamnloooooooooooooooo','last','test@gmail.com','rol2')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserNameNoLenght(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass','','last','test@gmail.com','rol1')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserNameNull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass',None,'last','test@gmail.com','rol1')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	#pruebas sobre last_name#
	def testUpdateUserLastNameNotStr(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass','name',1,'test@gmail.com','rol1')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserLastNameTooLong(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass','name','ImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'ImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlongImtoodamnlongImtoodamnlongImtoodamnlongImtoodammlong'
			'Imtoodamnloooooooooooooooo','test@gmail.com','rol2')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserLastNameNoLenght(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass','name','','test@gmail.com','rol1')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])
	def testUpdateUserLastNameNull(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol1')
		role_controller.createRole('rol2')
		user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol1')
		result = user_controller.updateUser('user','pass','name',None,'test@gmail.com','rol1')
		user_controller.deleteUser('user')
		role_controller.deleteRole(5)
		role_controller.deleteRole(6)
		self.assertFalse(result['result'])




if __name__ == '__main__':
	unittest.main()
	
		