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
	def testUpdateProfileStatusNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(123, 'Femenino', fecha, 575, '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	def testUpdateProfileTelphoneNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(123, 'Femenino', fecha, 'Soltero', 4242135767, 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	def testUpdateProfileAddressNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', -8)
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	def testUpdateProfileCIMAX(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(1000000000, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	def testUpdateProfileSexStrMax(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(123, 'Femeninoooo', fecha, 'Soltero', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	def testUpdateProfileStatusStrMax(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(123, 'Femenino', fecha, 'Solteroooooooooo', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	def testUpdateProfileTelphoneStrMax(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(123, 'Femenino', fecha, 'Soltero', '0042421357670000', 'direccion')
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	def testUpdateProfileAddressStrMax(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.updateProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', "d" * 101)
		p = profile_controller.getProfile(123)
		profile_controller.deleteProfile(p.id)
		self.assertFalse(result)
	##################################     
	#   Pruebas para deleteProfile   #
	##################################
	def testDeleteProfileTrue(self):
		fecha = date(2016, 7, 1)
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		p = profile_controller.getProfile(123)
		result = profile_controller.deleteProfile(p.id)	
		self.assertTrue(result)
	def testDeleteProfileFalse(self):
		profile_controller = profile()
		result = profile_controller.deleteProfile('123')
		self.assertFalse(result)
	###############################     
	#   Pruebas para getProfile   #
	###############################
	def testGetProfileTrue(self):
		fecha = date(2016, 7, 1)	
		profile_controller = profile()
		profile_controller.insertProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion')
		result = profile_controller.getProfile(123)
		profile_controller.deleteProfile(result.id)
		self.assertEqual(123, result.ci_user)
	def testGetProfileDoNotExists(self):
		profile_controller = profile()
		result = profile_controller.getProfile(0)
		self.assertEqual([], result)
	def testGetProfileNotValidID(self):
		profile_controller = profile()
		result = profile_controller.getProfile('2')
		self.assertEqual([],result)

if __name__ == '__main__':
	unittest.main()