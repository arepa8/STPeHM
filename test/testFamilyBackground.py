# 
# Casos de prueba para Family Background
#
# Grupo:	"Papagayo"
# Fecha:	30-06-2016
#

import sys
import unittest

sys.path.append('app/controllers')
sys.path.append('app/')

from user import *
from familyBackground import *

class TestFamilyBackground(unittest.TestCase):

	### INSERT FAMILY BACKGROUND ###
	
	def testInsertFamilyBackground(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		self.assertTrue(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testInsertFBExists(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFBAllNone(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(12345678, None, None, None, None, None, None, 'test')

		self.assertTrue(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testInsertFBStringCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground('5764', True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testInsertFBFloatCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(57.64, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)	

	def testInsertFBBoolCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(True, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testInsertFBNegCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.updateFamilyBackground(-5764, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testInsertFBZeroCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(0, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testInsertFBNoneCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(None, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testInsertFBIntOther(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 1)

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testInsertFBFloatOther(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 1.2)

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testInsertFBNoneOther(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, None)

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)
	
	def testInsertFBBoolOther(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, False)

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)



	### UPDATE FAMILY BACKGROUND ###

	def testUpdateFamilyBackground(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(12345678, True, False, True, False, True, False, 'test')

		self.assertTrue(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFamilyBackgroundNotExist(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(5764, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)
	
	def testUpdateFBAllNone(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(12345678, None, None, None, None, None, None, 'test')

		self.assertTrue(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFBStringCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground('5764', True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFBFloatCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(57.64, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)	

	def testUpdateFBBoolCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(True, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFBNegCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(-5764, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFBZeroCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(0, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFBNoneCI(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(None, True, False, True, False, True, False, 'test')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFBIntOther(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(12345678, True, False, True, False, True, False, 1)

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFBFloatOther(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(12345678, True, False, True, False, True, False, 1.2)

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)

	def testUpdateFBNoneOther(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(12345678, True, False, True, False, True, False, None)

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)
	
	def testUpdateFBBoolOther(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		result = family_background_controller.updateFamilyBackground(12345678, True, False, True, False, True, False, False)

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		family_background_controller.deleteFamilyBackground(12345678)




	### DELETE FAMILY BACKGROUND ###

	def testDeleteFamilyBackground(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		result = family_background_controller.deleteFamilyBackground(12345678)
		self.assertTrue(result)
		user_controller.deleteUser('doctortest')

	def testDeleteFBNoExist(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		result = family_background_controller.deleteFamilyBackground(958)
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testDeleteFBString(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		result = family_background_controller.deleteFamilyBackground("12345678")
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testDeleteFBFloat(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		result = family_background_controller.deleteFamilyBackground(12.34)
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testDeleteFBNeg(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		result = family_background_controller.deleteFamilyBackground(-1)
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testDeleteFBZero(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		result = family_background_controller.deleteFamilyBackground(0)
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
	
	def testDeleteFBMAXplus1(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		result = family_background_controller.deleteFamilyBackground(1000000000)
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testDeleteFBBoolean(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		result = family_background_controller.deleteFamilyBackground(True)
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
	
	def testDeleteFBNone(self):
		user_controller = user()
		family_background_controller = familyBackground()
		
		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		family_background_controller.insertFamilyBackground(12345678, True, False, True, False, True, False, 'test')
		
		result = family_background_controller.deleteFamilyBackground(None)
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

if __name__ == '__main__':
	unittest.main()






















