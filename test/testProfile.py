import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from Profile import profile
from datetime import date

class TestProfile(unittest.TestCase):
	###################################     
  	#   Pruebas para insertProfile    #
 	##################################
  	#se prueba funcionalidad sin asserts
	def testInsertProfile(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
	#se prueba funcionalidad con assert
	def testInsertProfileTrue(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		result = profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertTrue(result)
	def testInsertProfileCINotInt(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		result = profile_controller.insertProfile('asa', 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		self.assertFalse(result)
	def testInsertProfileSexNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		result = profile_controller.insertProfile(123, 565, fecha, 'Soltero', '04242135767', 'direccion')
		self.assertFalse(result)
	def testInsertProfileDateNone(self):
		profile_controller = profile()
		result = profile_controller.insertProfile(123, 'Femenino', None, 'Soltero', '04242135767', 'direccion')
		self.assertFalse(result)
	def testInsertProfileStatusNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		result = profile_controller.insertProfile(123, 'Femenino', fecha, 5468, '04242135767', 'direccion')
		self.assertFalse(result)
	def testInsertProfileTelephoneNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		result = profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', 4242135767, 'direccion')
		self.assertFalse(result)
	def testInsertProfileAddressNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		result = profile_controller.insertProfile(123, 'Femenino', fecha, 5468, '04242135767', -2154)
		self.assertFalse(result)
	##################################     
  	#   Pruebas para updateProfile   #
 	##################################
	def testUpdateProfileTrue(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(123, 'Masculino', fecha, 'Soltero', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertTrue(result)
	def testUpdateProfileCINotInt(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile('asa', 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	def testUpdateProfileSexNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(123, 0, fecha, 'Soltero', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	def testUpdateProfileDateNone(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		fecha = None
		result = profile_controller.updateProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()