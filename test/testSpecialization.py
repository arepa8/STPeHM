import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from specialization import *

class TestSpecialization(unittest.TestCase):
  ###########################################      
  #   Pruebas para insertSpecialization    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testInsertSpecialization(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		specialization_controller.deleteSpecialization(1)
	#se prueba funcionalidad con assert
	def testInsertSpecializationTrue(self):
		specialization_controller = specialization()
		result = specialization_controller.insertSpecialization('speciality')
		specialization_controller.deleteSpecialization(1)
		self.assertTrue(result)
	def testInsertSpecializationNotStr(self):
		specialization_controller = specialization()
		result = specialization_controller.insertSpecialization(1)
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertSpecializationNoLenght(self):
		specialization_controller = specialization()
		result = specialization_controller.insertSpecialization('')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertSpecializationNone(self):
		specialization_controller = specialization()
		result = specialization_controller.insertSpecialization(None)
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testInsertSpecializationAlreadyExists(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality1')
		result = specialization_controller.insertSpecialization('speciality1')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
  ###########################################      
  #   Pruebas para modifySpecialization    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testModifySpecialization(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		specialization_controller.modifySpecialization(1,'speciality1')
		specialization_controller.deleteSpecialization(1)
	#se prueba funcionalidad con assert
	def testModifySpecializationTrue(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.modifySpecialization(1,'speciality1')
		specialization_controller.deleteSpecialization(1)
		self.assertTrue(result)
	def testModifySpecializationNotStr(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.modifySpecialization(1,1)
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testModifySpecializationNoLenght(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.modifySpecialization(1,'')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testModifySpecializationNone(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.modifySpecialization(1,None)
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testModifySpecializationAlreadyExists(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		result = specialization_controller.modifySpecialization(1,'speciality2')
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertFalse(result)
  ###########################################      
  #   Pruebas para deleteSpecialization    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testDeleteSpecialization(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		specialization_controller.deleteSpecialization(1)
	#se prueba funcionalidad con assert
	def testDeleteSpecializationTrue(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result =specialization_controller.deleteSpecialization(1)
		self.assertTrue(result)
	def testDeleteSpecializationIdNotValid(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result =specialization_controller.deleteSpecialization('1')
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
	def testDeleteSpecializationIdNotExists(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result =specialization_controller.deleteSpecialization(2)
		specialization_controller.deleteSpecialization(1)
		self.assertFalse(result)
  ###########################################      
  #   Pruebas para getSpecializationByID    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetSpecializationByID(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		specialization_controller.getSpecializationByID(1)
		specialization_controller.deleteSpecialization(1)
	#se prueba funcionalidad con assert
	def testGetSpecializationByIDTrue(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.getSpecializationByID(1)
		specialization_controller.deleteSpecialization(1)
		self.assertEqual('speciality',result.speciality)
	def testGetSpecializationByIDNoexists(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.getSpecializationByID(2)
		specialization_controller.deleteSpecialization(1)
		self.assertEqual(None,result)
	def testGetSpecializationByIDNotValidID(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.getSpecializationByID('2')
		specialization_controller.deleteSpecialization(1)
		self.assertEqual(None,result)
  ###########################################      
  #Pruebas para getSpecializationBySpeciality#
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetSpecializationBySpeciality(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		specialization_controller.getSpecializationBySpeciality('speciality')
		specialization_controller.deleteSpecialization(1)
	#se prueba funcionalidad con assert
	def testetSpecializationBySpecialityTrue(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.getSpecializationBySpeciality('speciality')
		specialization_controller.deleteSpecialization(1)
		self.assertEqual('speciality',result.speciality)
	def testetSpecializationBySpecialityNoexists(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.getSpecializationBySpeciality('speciality2')
		specialization_controller.deleteSpecialization(1)
		self.assertEqual(None,result)
	def testetSpecializationBySpecialityNotValidSpeciality(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality')
		result = specialization_controller.getSpecializationBySpeciality(1)
		specialization_controller.deleteSpecialization(1)
		self.assertEqual(None,result)

  ###########################################      
  #   Pruebas para getAllSpecializations    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetAllSpecializations(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		specialization_controller.getAllSpecializations()
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
	#se prueba funcionalidad con assert
	def testGetAllSpecializationsAsserts(self):
		specialization_controller = specialization()
		specialization_controller.insertSpecialization('speciality1')
		specialization_controller.insertSpecialization('speciality2')
		result = specialization_controller.getAllSpecializations()
		specialization_controller.deleteSpecialization(1)
		specialization_controller.deleteSpecialization(2)
		self.assertEqual('speciality1',result[0].speciality)
		self.assertEqual('speciality2',result[1].speciality)

if __name__ == '__main__':
	unittest.main()