import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from appointment import *

class TestAppointment(unittest.TestCase):
	
	def testInsertAppointmentTrue(self):
		self.assertTrue(True)

if __name__ == '__main__':
	unittest.main()