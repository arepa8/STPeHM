import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from doctorSpecialization import *
from user import *
from specialization import *



class TestDoctorSpecialization(unittest.TestCase):
  ###########################################      
  #   Pruebas para insertDS    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testInsertDS(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
	#se prueba funcionalidad con assert
	def testInsertDSTrue(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		result=doctorSpecialization_controller.insertDS(12345678,1)

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertTrue(result)
	def testInsertDSNotValidUci(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		result=doctorSpecialization_controller.insertDS('12345678',1)

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertDSNoneUci(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		result=doctorSpecialization_controller.insertDS(None,1)

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertDSNoExistsUci(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		result=doctorSpecialization_controller.insertDS(12345679,1)

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertDSNotValidSid(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		result=doctorSpecialization_controller.insertDS(12345678,'1')

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertDSNoneSid(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		result=doctorSpecialization_controller.insertDS(12345678,None)

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertDSNoLenghtSid(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		result=doctorSpecialization_controller.insertDS(12345678,'')

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertDSNoExistsSid(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		result=doctorSpecialization_controller.insertDS(12345678,2)

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertDSNotDoctor(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'pacientetest','pass','name','last','doctorest@gmail.com',2)
		specialization_controller.insertSpecialization('speciality')
		result=doctorSpecialization_controller.insertDS(12345678,1)

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('pacientetest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)

  ###########################################      
  #   Pruebas para modifyDS    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testModifyDS(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		doctorSpecialization_controller.insertDS(12345678,1)
		doctorSpecialization_controller.modifyDS(1,12345678,2)


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
	#se prueba funcionalidad con assert
	def testModifyDSTrue(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		doctorSpecialization_controller.insertDS(12345678,1)
		result= doctorSpecialization_controller.modifyDS(1,12345678,2)


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertTrue(result)
	def testModifyDSNotValidUci(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		doctorSpecialization_controller.insertDS(12345678,1)
		result= doctorSpecialization_controller.modifyDS(1,'12345678',2)


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertFalse(result)
	def testModifyDSNoneUci(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		doctorSpecialization_controller.insertDS(12345678,1)
		result= doctorSpecialization_controller.modifyDS(1,None,2)


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertFalse(result)
	def testtModifyDSNoExistsUci(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		doctorSpecialization_controller.insertDS(12345678,1)
		result= doctorSpecialization_controller.modifyDS(1,12345679,2)


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertFalse(result)
	def testModifyDSNotValidSid(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		doctorSpecialization_controller.insertDS(12345678,1)
		result= doctorSpecialization_controller.modifyDS(1,12345678,'2')


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertFalse(result)
	def testModifyDSNoneSid(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		doctorSpecialization_controller.insertDS(12345678,1)
		result= doctorSpecialization_controller.modifyDS(1,12345678,None)


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertFalse(result)
	def testModifyDSNoLenghtSid(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		doctorSpecialization_controller.insertDS(12345678,1)
		result= doctorSpecialization_controller.modifyDS(1,12345678,'')


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertFalse(result)
	def testModifyDSNoExistsSid(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		doctorSpecialization_controller.insertDS(12345678,1)
		result= doctorSpecialization_controller.modifyDS(1,12345678,3)


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertFalse(result)

  ###########################################      
  #   Pruebas para deleteDS                 #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testDeleteDS(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)

		doctorSpecialization_controller.deleteDS(1) #
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
	#se prueba funcionalidad con assert
	def testDeleteDSTrue(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)

		result = doctorSpecialization_controller.deleteDS(1) #
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertTrue(result)
	def testDeleteDSIdNotValid(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)

		result = doctorSpecialization_controller.deleteDS('1') #
		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testDeleteDSIdNotExists(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)

		result = doctorSpecialization_controller.deleteDS(2) #
		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
  ###########################################      
  #   Pruebas para getDSByID    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetDSByID(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)
		doctorSpecialization_controller.getDSByID(1)

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
	#se prueba funcionalidad con assert
	def testGetDSByIDTrue(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)
		result=doctorSpecialization_controller.getDSByID(1)


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertEqual(12345678,result.doctor)
		self.assertEqual(1,result.speciality)
	def testGetDSByIDNoexists(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)
		result=doctorSpecialization_controller.getDSByID(2)


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertEqual(None,result)
	def testGetDSByIDNotValidID(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)
		result=doctorSpecialization_controller.getDSByID('2')


		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertEqual(None,result)

  ###########################################      
  #   Pruebas para getAllDS    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetAllSpecializations(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)
		doctorSpecialization_controller.getAllDS()

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
	#se prueba funcionalidad con assert
	def testGetAllSpecializationsAsserts(self):
		user_controller = user()
		specialization_controller = specialization()
		doctorSpecialization_controller = doctorSpecialization()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		specialization_controller.insertSpecialization('speciality')
		doctorSpecialization_controller.insertDS(12345678,1)
		result = doctorSpecialization_controller.getAllDS()

		doctorSpecialization_controller.deleteDS(1)
		user_controller.deleteUser('doctortest')
		specialization_controller.deleteSpecialization(1)
		self.assertEqual(12345678,result[0].doctor)
		self.assertEqual(1,result[0].speciality)

if __name__ == '__main__':
	unittest.main()