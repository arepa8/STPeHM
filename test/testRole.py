import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from role import *

class TestRole(unittest.TestCase):
	
	def testCreateRoleTrue(self):
		role_controller = role()
		result = role_controller.createRole('rol')
		self.assertTrue(result)
		role_controller.deleteRole(1)

if __name__ == '__main__':
	unittest.main()