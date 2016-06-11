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

if __name__ == '__main__':
	unittest.main()