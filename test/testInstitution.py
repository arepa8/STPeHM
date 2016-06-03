import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from institution import *

class TestInstitution(unittest.TestCase):
  ###########################################      
  #   Pruebas para insertInstitution    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testInsertInstitution(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		institution_controller.deleteInstitution(1)
	#se prueba funcionalidad con assert
	def testInsertInstitutionTrue(self):
		institution_controller = institution()
		result = institution_controller.insertInstitution('institucion','direccion')
		institution_controller.deleteInstitution(1)
		self.assertTrue(result)
	def testInsertInstitutionNameNotStr(self):
		institution_controller = institution()
		result = institution_controller.insertInstitution(1,'direccion')
		institution_controller.deleteInstitution(1)
		self.assertFalse(result)
	def testInsertInstitutionNameNoLenght(self):
		institution_controller = institution()
		result = institution_controller.insertInstitution('','direccion')
		institution_controller.deleteInstitution(1)
		self.assertFalse(result)
	def testInsertInstitutionNameNone(self):
		institution_controller = institution()
		result = institution_controller.insertInstitution(None,'direccion')
		institution_controller.deleteInstitution(1)
		self.assertFalse(result)
	def testInsertInstitutionAddressNotStr(self):
		institution_controller = institution()
		result = institution_controller.insertInstitution('institucion',1)
		institution_controller.deleteInstitution(1)
		self.assertFalse(result)
	def testInsertInstitutionAddressNoLenght(self):
		institution_controller = institution()
		result = institution_controller.insertInstitution('institucion','')
		institution_controller.deleteInstitution(1)
		self.assertFalse(result)
	def testInsertInstitutionAddressNone(self):
		institution_controller = institution()
		result = institution_controller.insertInstitution('institucion',None)
		institution_controller.deleteInstitution(1)
		self.assertFalse(result)
	def testInsertInstitutionNameAlreadyExists(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.insertInstitution('institucion','direccion1')
		institution_controller.deleteInstitution(1)
		self.assertEqual('El nombre y la dirección deben ser únicos.',result)
	def testInsertInstitutionAddressAlreadyExists(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.insertInstitution('institucion2','direccion')
		institution_controller.deleteInstitution(1)
		self.assertEqual('El nombre y la dirección deben ser únicos.',result)
  ###########################################      
  #   Pruebas para modifyInstitution    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testModifyInstitution(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		institution_controller.modifyInstitution(1,'institucion nueva','direccion nueva')
		institution_controller.deleteInstitution(1)
	#se prueba funcionalidad con assert
	def testModifyInstitutionTrue(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.modifyInstitution(1,'institucion3','direccion3')
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertTrue(result)
	def testModifyInstitutionNameNotStr(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.modifyInstitution(1,3,'direccion3')
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertFalse(result)
	def testModifyInstitutionNameNoLenght(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.modifyInstitution(1,'','direccion3')
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertFalse(result)
	def testModifyInstitutionNameNone(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.modifyInstitution(1,None,'direccion3')
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertFalse(result)
	def testModifyInstitutionAddressNotStr(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.modifyInstitution(1,'institucion3',1)
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertFalse(result)
	def testModifyInstitutionAddressNoLenght(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.modifyInstitution(1,'institucion3','')
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertFalse(result)
	def testModifyInstitutionAddressNone(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.modifyInstitution(1,'institucion3',None)
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertFalse(result)
	def testModifyInstitutionNameAlreadyExists(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.modifyInstitution(1,'institucion2','direccion3')
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertEqual('El nombre y la dirección no pueden ser duplicados.',result)
	def testModifyInstitutionAddressAlreadyExists(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.modifyInstitution(1,'institucion3','direccion2')
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertEqual('El nombre y la dirección no pueden ser duplicados.',result)
  ###########################################      
  #   Pruebas para deleteInstitution    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testDeleteInstitution(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		institution_controller.deleteInstitution(1)
	#se prueba funcionalidad con assert
	def testDeleteInstitutionTrue(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.deleteInstitution(1)
		self.assertTrue(result)
	def testDeleteInstitutionIdNotValid(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.deleteInstitution('1')
		self.assertFalse(result)
	def testDeleteInstitutionIdNotExists(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.deleteInstitution('1')
		self.assertFalse(result)
  ###########################################      
  #   Pruebas para getInstitutionByName    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetInstitutionByName(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		institution_controller.getInstitutionByName('institucion')
		institution_controller.deleteInstitution(1)
	#se prueba funcionalidad con assert
	def testGetInstitutionByNameTrue(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.getInstitutionByName('institucion')
		institution_controller.deleteInstitution(1)
		self.assertEqual('institucion',result.name)
		self.assertEqual('direccion',result.address)
	def testGetInstitutionByNameNoexists(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.getInstitutionByName('institucion1')
		institution_controller.deleteInstitution(1)
		self.assertEqual(None,result)
	def testGetInstitutionByNameNotValidName(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.getInstitutionByName(1)
		institution_controller.deleteInstitution(1)
		self.assertEqual(None,result)
  ###########################################      
  #   Pruebas para getInstitutionById    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetInstitutionById(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		institution_controller.getInstitutionById(1)
		institution_controller.deleteInstitution(1)
	#se prueba funcionalidad con assert
	def testGetInstitutionByIdTrue(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.getInstitutionById(1)
		institution_controller.deleteInstitution(1)
		self.assertEqual('institucion',result.name)
		self.assertEqual('direccion',result.address)
	def testGetInstitutionByIdNoexists(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.getInstitutionById(2)
		institution_controller.deleteInstitution(1)
		self.assertEqual(None,result)
	def testGetInstitutionByIdNotValidId(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion','direccion')
		result = institution_controller.getInstitutionById('1')
		institution_controller.deleteInstitution(1)
		self.assertEqual(None,result)
  ###########################################      
  #   Pruebas para getAllInstitutions    #
  ###########################################
  #se prueba funcionalidad sin asserts
	def testGetAllInstitutions(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		institution_controller.getAllInstitutions()
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
	#se prueba funcionalidad con assert
	def testGetAllInstitutionsWorks(self):
		institution_controller = institution()
		institution_controller.insertInstitution('institucion1','direccion1')
		institution_controller.insertInstitution('institucion2','direccion2')
		result = institution_controller.getAllInstitutions()
		institution_controller.deleteInstitution(1)
		institution_controller.deleteInstitution(2)
		self.assertEqual('institucion1',result[0].name)
		self.assertEqual('direccion1',result[0].address)
		self.assertEqual('institucion2',result[1].name)
		self.assertEqual('direccion2',result[1].address)

if __name__ == '__main__':
	unittest.main()