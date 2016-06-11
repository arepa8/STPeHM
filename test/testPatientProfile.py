import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from patientProfile import patientProfile
from datetime import date

class TestPatientProfile(unittest.TestCase):

	##########################################    
  	#   Pruebas para insertPatientProfile    #
 	##########################################

  	#se prueba funcionalidad sin asserts
	def testInsertProfile(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(123)

	#se prueba funcionalidad con assert
	def testInsertProfileTrue(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		result = profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(p.id)
		self.assertTrue(result)

	def testInsertProfileCINotInt(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		result = profile_controller.insertPatientProfile('asa', 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		self.assertFalse(result)

	def testInsertProfileSexNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		result = profile_controller.insertPatientProfile(123, 444, fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		self.assertFalse(result)

	def testInsertProfileStatusNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		result = profile_controller.insertPatientProfile(123, 'Femenino', fecha, 5468, '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		self.assertFalse(result)

	def testInsertProfileTelephoneNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		result = profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', 54242, 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')		
		self.assertFalse(result)

	def testInsertProfileAddressNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		result = profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', -2154,'1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		self.assertFalse(result)

	#########################################   
  	#   Pruebas para updatePatientProfile   #
 	#########################################

	def testUpdateProfileTrue(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile(123, 'Masculino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(123)
		self.assertTrue(result)

	def testUpdateProfileCINotInt(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile('asa', 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		profile_controller.deletePatientProfile(123)
		self.assertFalse(result)

	def testUpdateProfileSexNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile(123, 456, fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(123)
		self.assertFalse(result)

	def testUpdateProfileStatusNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile(123, 'Masculino', fecha, 575, '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(p.id)
		self.assertFalse(result)

	def testUpdateProfileTelphoneNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile(123, 'Masculino', fecha, 'Soltero', 4242135767, 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(p.id)
		self.assertFalse(result)

	def testUpdateProfileAddressNotStr(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile(123, 'Masculino', fecha, 'Soltero', '04242135767', -8,'1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(p.id)
		self.assertFalse(result)

	def testUpdateProfileCIMAX(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile(1000000000, 'Masculino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(p.id)
		self.assertFalse(result)

	def testUpdateProfileStatusStrMax(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile(123, 'Masculino', fecha, 'Solteroooooooooo', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(p.id)
		self.assertFalse(result)

	def testUpdateProfileTelphoneStrMax(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile(123, 'Masculino', fecha, 'Soltero', '0042421357670000', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(p.id)
		self.assertFalse(result)

	def testUpdateProfileAddressStrMax(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.updatePatientProfile(123, 'Masculino', fecha, 'Soltero', '04242135767', "d" * 101,'1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(p.ci_user)
		self.assertFalse(result)

	#########################################     
	#   Pruebas para deletePatientProfile   #
	#########################################
	def testDeleteProfileTrue(self):
		fecha = date(2016, 7, 1)
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		p = profile_controller.getPatientProfileByCi(123)
		result = profile_controller.deletePatientProfile(p.ci_user)	
		self.assertTrue(result)

	def testDeleteProfileFalse(self):
		profile_controller = patientProfile()
		result = profile_controller.deletePatientProfile('123')
		self.assertFalse(result)

	##########################################    
	#   Pruebas para getPatientProfileByCi   #
	##########################################

	def testGetProfileTrue(self):
		fecha = date(2016, 7, 1)	
		profile_controller = patientProfile()
		profile_controller.insertPatientProfile(123, 'Femenino', fecha, 'Soltero', '04242135767', 'direccion','1,5m','55kg','a+','F','Ninguna', 'Contacto', '04165551234','Comentario')
		result = profile_controller.getPatientProfileByCi(123)
		profile_controller.deletePatientProfile(result.ci_user)
		self.assertEqual(123, result.ci_user)

	def testGetProfileDoNotExists(self):
		profile_controller = patientProfile()
		result = profile_controller.getPatientProfileByCi(-1)
		self.assertEqual(None, result)

	def testGetProfileNotValidCi(self):
		profile_controller = patientProfile()
		result = profile_controller.getPatientProfileByCi('2')
		self.assertEqual(None,result)

if __name__ == '__main__':
	unittest.main()