import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from user import *
from role import *

class TestUser(unittest.TestCase):
	
	def testInsertUserTrue(self):
		user_controller = user()
		role_controller = role()
		role_controller.createRole('rol')
		result = user_controller.insertUser(12345678,'user','pass','name','last','test@gmail.com','rol')
		self.assertTrue(result)
		user_controller.deleteUser('user')
		role_controller.deleteRole(1)

if __name__ == '__main__':
	unittest.main()
	
		