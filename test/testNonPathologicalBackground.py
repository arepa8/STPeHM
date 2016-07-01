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
from nonPathologicalBackground import *

class TestNonPathologicalBackground(unittest.TestCase):

	### INSERT NON PATHOLOGICAL PROBLEMS ###

	def testInsertNPB(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		
		self.assertTrue(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testInsertNPBExists(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		
		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testInsertNPBStringCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground('12345678','test','test','test','test','test','test','test','test','test')
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')
		
	def testInsertNPBFloatCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(1234.5678,'test','test','test','test','test','test','test','test','test')
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testInsertNPBNegCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(-123456,'test','test','test','test','test','test','test','test','test')
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testInsertNPBZeroCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(0,'test','test','test','test','test','test','test','test','test')
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testInsertNPBMaxintCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(2**31,'test','test','test','test','test','test','test','test','test')
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testInsertNPBBoolCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(False,'test','test','test','test','test','test','test','test','test')
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testInsertNPBNoneCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(None,'test','test','test','test','test','test','test','test','test')
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testInsertNPBIntOther(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test',1)
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testInsertNPBNoneOther(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test',None)
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testInsertNPBBoolOther(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test',False)
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testInsertNPBFloatOther(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test',1.2)
		
		self.assertFalse(result)
		user_controller.deleteUser('doctortest')


	### UPDATE NON PATHOLOGICAL PROBLEMS ###


	def testUpdateNPB(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test1')

		self.assertTrue(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBNotExists(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test1')

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBStringCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground('12345678','test','test','test','test','test','test','test','test','test1')

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBFloatCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(1234.5678,'test','test','test','test','test','test','test','test','test1')

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBNegCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(-12345678,'test','test','test','test','test','test','test','test','test1')

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')	

	def testUpdateNPBZeroCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(0,'test','test','test','test','test','test','test','test','test1')

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBNoneCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(None,'test','test','test','test','test','test','test','test','test1')

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBMaxintCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(2**31,'test','test','test','test','test','test','test','test','test1')

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBBoolCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(True,'test','test','test','test','test','test','test','test','test1')

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBIntOther(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test',1)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBNoneOther(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test',None)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBNegOther(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test',-1)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBFloatOther(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test',1.2)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testUpdateNPBBoolOther(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.updateNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test',False)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')


	### DELETE NON PATHOLOGICAL PROBLEMS ###

	
	def testDeleteNPB(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.deleteNonPathologicalBackground(12345678)

		self.assertTrue(result)
		user_controller.deleteUser('doctortest')

	def testDeleteNPBNotExists(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		result = npb_controller.deleteNonPathologicalBackground(12345678)

		self.assertFalse(result)
		user_controller.deleteUser('doctortest')

	def testDeleteNPBStringCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.deleteNonPathologicalBackground('12345678')

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testDeleteNPBFloatCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.deleteNonPathologicalBackground(123.45678)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testDeleteNPBNegCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.deleteNonPathologicalBackground(-674)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testDeleteNPBZeroCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.deleteNonPathologicalBackground(0)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testDeleteNPBBoolCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.deleteNonPathologicalBackground(True)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testDeleteNPBNoneCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.deleteNonPathologicalBackground(None)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

	def testDeleteNPBMaxIntCI(self):
		user_controller = user()
		npb_controller = nonPathologicalBackground()

		user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
		npb_controller.insertNonPathologicalBackground(12345678,'test','test','test','test','test','test','test','test','test')
		result = npb_controller.deleteNonPathologicalBackground(2**31)

		self.assertFalse(result)
		npb_controller.deleteNonPathologicalBackground(12345678)
		user_controller.deleteUser('doctortest')

if __name__ == '__main__':
	unittest.main()
















