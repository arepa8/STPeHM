# 
# Casos de prueba para Family Background
#
# Grupo:	"Papagayo"
# Fecha:	30-06-2016
#

import sys
import unittest

sys.path.append('../app/controllers')
sys.path.append('../app/')

from user import *
from pathologicalBackground import *

class TestPathologicalBackground(unittest.TestCase):
  ###############################################      
  # Pruebas para Insert Pathological Background #
  ###############################################	

  def testinsertPathologicalBackgroundTrue(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertTrue(result)

  def testinsertPathologicalBackgroundCiAlreadyExists(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundCiString(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground('12345678','current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundCiBool(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(True,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundCiFloat(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(12345678.0,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundCiNegativeInt(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(-12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundCiLong(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(1000000000,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundCiZero(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(0,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundCiNull(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(None,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundOtherInt(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions',1)
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundOtherBool(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions',True)
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundOtherFloat(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions',23.3)
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundOtherNotMaxLen(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testinsertPathologicalBackgroundOtherNull(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions',None)
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  ###############################################      
  # Pruebas para Update Pathological Background #
  ###############################################	

  def testupdatePathologicalBackgroundTrue(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(12345678,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other2')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertTrue(result)

  def testupdatePathologicalBackgroundCiNotExists(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(23232323,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other2')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundCiString(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground('12345678','current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other2')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundCiBool(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(True,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other2')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundCiFloat(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(12345678.0,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other2')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundCiNegativeInt(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(-12345678,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other2')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundCiLong(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(1000000000,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other2')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundCiZero(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(0,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other2')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundCiNull(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(None,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other2')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundOtherInt(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(12345678,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2',2)
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundOtherBool(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(12345678,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2',True)
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundOtherFloat(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(12345678,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2',23.3)
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundOtherNotMaxLen(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(12345678,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2','other'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother'+
						'otherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherotherother')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  def testupdatePathologicalBackgroundOtherNull(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result = pb_controller.updatePathologicalBackground(12345678,'current_condition2','surgical_history2',
						'transfusional_history2','allergies2','traumatic_history2','hospitalizations2','addictions2',None)
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)

  ###############################################      
  # Pruebas para Delete Pathological Background #
  ###############################################	
  def testdeletePathologicalBackgroundTrue(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	result = pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	pb_controller.deletePathologicalBackground(12345678)
  	user_controller.deleteUser('doctortest')
  	self.assertTrue(result)

  def testdeletePathologicalBackgroundCiNotExists(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result =  pb_controller.deletePathologicalBackground(23232323)
  	user_controller.deleteUser('doctortest')
  	self.assertFalse(result)
  def testdeletePathologicalBackgroundCiString(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result =  pb_controller.deletePathologicalBackground('12345678')
  	user_controller.deleteUser('doctortest')
  	pb_controller.deletePathologicalBackground(12345678)
  	self.assertFalse(result)

  def testdeletePathologicalBackgroundCiBool(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result =  pb_controller.deletePathologicalBackground(True)
  	user_controller.deleteUser('doctortest')
  	pb_controller.deletePathologicalBackground(12345678)
  	self.assertFalse(result)

  def testdeletePathologicalBackgroundCiFloat(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result =  pb_controller.deletePathologicalBackground(12345678.0)
  	user_controller.deleteUser('doctortest')
  	pb_controller.deletePathologicalBackground(12345678)
  	self.assertFalse(result)

  def testdeletePathologicalBackgroundCiNegativeInt(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result =  pb_controller.deletePathologicalBackground(-12345678)
  	user_controller.deleteUser('doctortest')
  	pb_controller.deletePathologicalBackground(12345678)
  	self.assertFalse(result)

  def testdeletePathologicalBackgroundCiLong(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result =  pb_controller.deletePathologicalBackground(1000000000)
  	user_controller.deleteUser('doctortest')
  	pb_controller.deletePathologicalBackground(12345678)
  	self.assertFalse(result)

  def testdeletePathologicalBackgroundCiZero(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result =  pb_controller.deletePathologicalBackground(0)
  	user_controller.deleteUser('doctortest')
  	pb_controller.deletePathologicalBackground(12345678)
  	self.assertFalse(result)

  def testdeletePathologicalBackgroundCiNull(self):
  	user_controller = user()
  	pb_controller = pathologicalBackground()

  	user_controller.insertUser(12345678,'doctortest','pass','name','last','doctorest@gmail.com',1)
  	pb_controller.insertPathologicalBackground(12345678,'current_condition','surgical_history',
						'transfusional_history','allergies','traumatic_history','hospitalizations','addictions','other')
  	result =  pb_controller.deletePathologicalBackground(None)
  	user_controller.deleteUser('doctortest')
  	pb_controller.deletePathologicalBackground(12345678)
  	self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()
