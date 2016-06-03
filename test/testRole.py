import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from role import *

class TestRole(unittest.TestCase):
	
  ###########################################      
  #         Pruebas para CreateRole         #
  ###########################################	

	#se prueba funcionalidad con assert 	
	def testCreateRoleTrue(self):
		role_controller = role()
		result = role_controller.createRole('rol')
		self.assertTrue(result)
		role_controller.deleteRole(5)

	#prueba sobre role_name
	def testCreateRoleEmpty(self):
		role_controller = role()
		result = role_controller.createRole('')
		self.assertFalse(result)

	def testCreateRoleInt(self):
		role_controller = role()
		result = role_controller.createRole(1)
		self.assertFalse(result)

	def testCreateRoleFloat(self):
		role_controller = role()
		result = role_controller.createRole(1.01)
		self.assertFalse(result)

	def testCreateRoleBoolean(self):
		role_controller = role()
		result = role_controller.createRole(True)
		self.assertFalse(result)

	def testCreateRoleThatExists(self):
		role_controller = role()
		role_controller.createRole('rol')
		result = role_controller.createRole('rol')
		self.assertEqual(result, 'El rol ya existe.')
		role_controller.deleteRole(5)

  ###########################################      
  #         Pruebas para deleteRole         #
  ###########################################

	def testDeleteRoleTrue(self):
		role_controller = role()
		role_controller.createRole('rol')
		result = role_controller.deleteRole(5)
		self.assertTrue(result)

	#pruebas sobre role_id
	def testDeleteRoleNotExist(self):
		role_controller = role()
		result = role_controller.deleteRole(5)
		self.assertFalse(result)

	def testDeleteRoleNone(self):
		role_controller = role()
		result = role_controller.deleteRole(None)
		self.assertFalse(result)

	def testDeleteRoleString(self):
		role_controller = role()
		result = role_controller.deleteRole('5')
		self.assertFalse(result)

	def testDeleteRoleFloat(self):
		role_controller = role()
		result = role_controller.deleteRole(5.1)
		self.assertFalse(result)

	def testDeleteRoleBoolean(self):
		role_controller = role()
		result = role_controller.deleteRole(True)
		self.assertFalse(result)

	def testDeleteRoleZero(self):
		role_controller = role()
		result = role_controller.deleteRole(0)
		self.assertFalse(result)

	def testDeleteRoleNegative(self):
		role_controller = role()
		result = role_controller.deleteRole(-1)
		self.assertFalse(result)

	def testDeleteRoleMaxInt(self):
		role_controller = role()
		result = role_controller.deleteRole(2**31)
		self.assertFalse(result)

  ###########################################
  #          Pruebas para getRole           #
  ###########################################

	def testGetRole(self):
		role_controller = role()
		role_controller.createRole('rol')
		result = role_controller.getRole(5)
		self.assertTrue(result)
		role_controller.deleteRole(5)

	#pruebas sobre role_id
	def testGetRoleNotExist(self):
		role_controller = role()
		result = role_controller.getRole(20)
		self.assertFalse(result)

	def testGetRoleNone(self):
		role_controller = role()
		result = role_controller.getRole(None)
		self.assertFalse(result)

	def testGetRoleString(self):
		role_controller = role()
		result = role_controller.getRole('5')
		self.assertFalse(result)

	def testGetRoleFloat(self):
		role_controller = role()
		result = role_controller.getRole(5.98)
		self.assertFalse(result)

	def testGetRoleBoolean(self):
		role_controller = role()
		result = role_controller.getRole(False)
		self.assertFalse(result)

	def testGetRoleZero(self):
		role_controller = role()
		result = role_controller.getRole(0)
		self.assertFalse(result)

	def testGetRoleNegative(self):
		role_controller = role()
		result = role_controller.getRole(-1)
		self.assertFalse(result)

	def testGetRoleMaxInt(self):
		role_controller = role()
		result = role_controller.getRole(2**31)
		self.assertFalse(result)
  
  ###########################################
  #         Pruebas para updateRole         #
  ###########################################

	def testUpdateRoleTrue(self):
		role_controller = role()
		role_controller.createRole('rol')
		result = role_controller.updateRole(5,'role')
		self.assertTrue(result)
		role_controller.deleteRole(5)

	#pruebas sobre role_id

	def testUpdateRoleIntInt(self):
		role_controller = role()
		result = role_controller.updateRole(5,2)
		self.assertFalse(result)

	def testUpdateRoleIntFloat(self):
		role_controller = role()
		result = role_controller.updateRole(5,2.2)
		self.assertFalse(result)

	def testUpdateRoleIntNone(self):
		role_controller = role()
		result = role_controller.updateRole(5,None)
		self.assertFalse(result)	

	def testUpdateRoleIntBool(self):
		role_controller = role()
		result = role_controller.updateRole(5,True)
		self.assertFalse(result)

	def testUpdateRoleIntNeg(self):
		role_controller = role()
		result = role_controller.updateRole(5,-2)
		self.assertFalse(result)	

	def testUpdateRoleIntZero(self):
		role_controller = role()
		result = role_controller.updateRole(5,0)
		self.assertFalse(result)

	def testUpdateRoleIntMaxInt(self):
		role_controller = role()
		result = role_controller.updateRole(5,2**31)
		self.assertFalse(result)

	## id Float

	def testUpdateRoleFloatInt(self):
		role_controller = role()
		result = role_controller.updateRole(5.1,2)
		self.assertFalse(result)

	def testUpdateRoleFloatFloat(self):
		role_controller = role()
		result = role_controller.updateRole(5.1,2.2)
		self.assertFalse(result)

	def testUpdateRoleFloatNone(self):
		role_controller = role()
		result = role_controller.updateRole(5.1,None)
		self.assertFalse(result)	

	def testUpdateRoleFloatBool(self):
		role_controller = role()
		result = role_controller.updateRole(5.1,True)
		self.assertFalse(result)

	def testUpdateRoleFloatNeg(self):
		role_controller = role()
		result = role_controller.updateRole(5.1,-2)
		self.assertFalse(result)	

	def testUpdateRoleFloatZero(self):
		role_controller = role()
		result = role_controller.updateRole(5.1,0)
		self.assertFalse(result)

	def testUpdateRoleFloatMaxInt(self):
		role_controller = role()
		result = role_controller.updateRole(5.1,2**31)
		self.assertFalse(result)

	## id String

	def testUpdateRoleStrInt(self):
		role_controller = role()
		result = role_controller.updateRole('5',2)
		self.assertFalse(result)

	def testUpdateRoleStrFloat(self):
		role_controller = role()
		result = role_controller.updateRole('5',2.2)
		self.assertFalse(result)

	def testUpdateRoleStrNone(self):
		role_controller = role()
		result = role_controller.updateRole('5',None)
		self.assertFalse(result)	

	def testUpdateRoleStrBool(self):
		role_controller = role()
		result = role_controller.updateRole('5',True)
		self.assertFalse(result)

	def testUpdateRoleStrNeg(self):
		role_controller = role()
		result = role_controller.updateRole('5',-2)
		self.assertFalse(result)	

	def testUpdateRoleStrZero(self):
		role_controller = role()
		result = role_controller.updateRole('5',0)
		self.assertFalse(result)

	def testUpdateRoleStrMaxInt(self):
		role_controller = role()
		result = role_controller.updateRole('5',2**31)
		self.assertFalse(result)

	## id Negative

	def testUpdateRoleNegInt(self):
		role_controller = role()
		result = role_controller.updateRole(-5,2)
		self.assertFalse(result)

	def testUpdateRoleNegFloat(self):
		role_controller = role()
		result = role_controller.updateRole(-5,2.2)
		self.assertFalse(result)

	def testUpdateRoleNegNone(self):
		role_controller = role()
		result = role_controller.updateRole(-5,None)
		self.assertFalse(result)	

	def testUpdateRoleNegBool(self):
		role_controller = role()
		result = role_controller.updateRole(-5,True)
		self.assertFalse(result)

	def testUpdateRoleNegNeg(self):
		role_controller = role()
		result = role_controller.updateRole(-5,-2)
		self.assertFalse(result)	

	def testUpdateRoleNegZero(self):
		role_controller = role()
		result = role_controller.updateRole(-5,0)
		self.assertFalse(result)

	def testUpdateRoleNegMaxInt(self):
		role_controller = role()
		result = role_controller.updateRole(-5,2**31)
		self.assertFalse(result)

	## id Zero

	def testUpdateRoleZeroInt(self):
		role_controller = role()
		result = role_controller.updateRole(0,2)
		self.assertFalse(result)

	def testUpdateRoleZeroFloat(self):
		role_controller = role()
		result = role_controller.updateRole(0,2.2)
		self.assertFalse(result)

	def testUpdateRoleZeroNone(self):
		role_controller = role()
		result = role_controller.updateRole(0,None)
		self.assertFalse(result)	

	def testUpdateRoleZeroBool(self):
		role_controller = role()
		result = role_controller.updateRole(0,True)
		self.assertFalse(result)

	def testUpdateRoleZeroNeg(self):
		role_controller = role()
		result = role_controller.updateRole(0,-2)
		self.assertFalse(result)	

	def testUpdateRoleZeroZero(self):
		role_controller = role()
		result = role_controller.updateRole(0,0)
		self.assertFalse(result)

	def testUpdateRoleZeroMaxInt(self):
		role_controller = role()
		result = role_controller.updateRole(0,2**31)
		self.assertFalse(result)

	## id Boolean

	def testUpdateRoleBoolInt(self):
		role_controller = role()
		result = role_controller.updateRole(True,2)
		self.assertFalse(result)

	def testUpdateRoleBoolFloat(self):
		role_controller = role()
		result = role_controller.updateRole(True,2.2)
		self.assertFalse(result)

	def testUpdateRoleBoolNone(self):
		role_controller = role()
		result = role_controller.updateRole(True,None)
		self.assertFalse(result)	

	def testUpdateRoleBoolBool(self):
		role_controller = role()
		result = role_controller.updateRole(True,True)
		self.assertFalse(result)

	def testUpdateRoleBoolNeg(self):
		role_controller = role()
		result = role_controller.updateRole(True,-2)
		self.assertFalse(result)	

	def testUpdateRoleBoolZero(self):
		role_controller = role()
		result = role_controller.updateRole(True,0)
		self.assertFalse(result)

	def testUpdateRoleBoolMaxInt(self):
		role_controller = role()
		result = role_controller.updateRole(True,2**31)
		self.assertFalse(result)

	## id None

	def testUpdateRoleNoneInt(self):
		role_controller = role()
		result = role_controller.updateRole(None,2)
		self.assertFalse(result)

	def testUpdateRoleNoneFloat(self):
		role_controller = role()
		result = role_controller.updateRole(None,2.2)
		self.assertFalse(result)

	def testUpdateRoleNoneNone(self):
		role_controller = role()
		result = role_controller.updateRole(None,None)
		self.assertFalse(result)	

	def testUpdateRoleNoneBool(self):
		role_controller = role()
		result = role_controller.updateRole(None,True)
		self.assertFalse(result)

	def testUpdateRoleNoneNeg(self):
		role_controller = role()
		result = role_controller.updateRole(None,-2)
		self.assertFalse(result)	

	def testUpdateRoleNoneZero(self):
		role_controller = role()
		result = role_controller.updateRole(None,0)
		self.assertFalse(result)

	def testUpdateRoleNoneMaxInt(self):
		role_controller = role()
		result = role_controller.updateRole(None,2**31)
		self.assertFalse(result) 

	## id MaxInt

	def testUpdateRoleMaxIntInt(self):
		role_controller = role()
		result = role_controller.updateRole(2**31,2)
		self.assertFalse(result)

	def testUpdateRoleMaxIntFloat(self):
		role_controller = role()
		result = role_controller.updateRole(2**31,2.2)
		self.assertFalse(result)

	def testUpdateRoleMaxIntNone(self):
		role_controller = role()
		result = role_controller.updateRole(2**31,None)
		self.assertFalse(result)	

	def testUpdateRoleMaxIntBool(self):
		role_controller = role()
		result = role_controller.updateRole(2**31,True)
		self.assertFalse(result)

	def testUpdateRoleMaxIntNeg(self):
		role_controller = role()
		result = role_controller.updateRole(2**31,-2)
		self.assertFalse(result)	

	def testUpdateRoleMaxIntZero(self):
		role_controller = role()
		result = role_controller.updateRole(2**31,0)
		self.assertFalse(result)

	def testUpdateRoleMaxIntMaxInt(self):
		role_controller = role()
		result = role_controller.updateRole(2**31,2**31)
		self.assertFalse(result)

	## prueba sobre role_name string

	def testUpdateRoleFloatStr(self):
		role_controller = role()
		result = role_controller.updateRole(2.31,'rol')
		self.assertFalse(result)

	def testUpdateRoleNoneStr(self):
		role_controller = role()
		result = role_controller.updateRole(None,'rol')
		self.assertFalse(result)	

	def testUpdateRoleBoolStr(self):
		role_controller = role()
		result = role_controller.updateRole(True,'rol')
		self.assertFalse(result)

	def testUpdateRoleNegStr(self):
		role_controller = role()
		result = role_controller.updateRole(-2,'rol')
		self.assertFalse(result)	

	def testUpdateRoleZeroStr(self):
		role_controller = role()
		result = role_controller.updateRole(0,'rol')
		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()

















