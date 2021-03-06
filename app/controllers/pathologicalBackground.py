import sys
#sys.path.append('app/')
sys.path.append('../')
from models import *

# Constantes
CONST_MIN		= 0
CONST_MAX_100	= 100
CONST_MAX_500	= 500
CONST_MAX_CI	= 999999999

class pathologicalBackground():
	""" Constrolador de Antecedentes Familiares """

	def insertPathologicalBackground(self,ci_user,current_condition,surgical_history,transfusional_history,allergies,traumatic_history,hospitalizations,addictions,other):
		check_ci 	= (ci_user !=None) and (type(ci_user) == int)
		check_other = type(other) == str

		if (check_ci and check_other):

			check_long_ci = 1 <= ci_user <= CONST_MAX_CI
			check_long_other = CONST_MIN <= len(other) <= CONST_MAX_500
			
			if check_long_ci and check_long_other:

				old = PathologicalBackground.query.filter_by(ci_user=ci_user).first()

				if old == None:
					new = PathologicalBackground(ci_user,current_condition,
												surgical_history,
												transfusional_history,
												allergies,
												traumatic_history,
												hospitalizations,
												addictions,
												other)
					db.session.add(new)
					db.session.commit()
					return True

		return False

	def updatePathologicalBackground(self,ci_user,current_condition,surgical_history,transfusional_history,allergies,traumatic_history,hospitalizations,addictions,other):

		check_ci 	= (ci_user !=None) and (type(ci_user) == int)
		check_other = type(other) == str

		if (check_ci and check_other):

			check_long_ci = 1 <= ci_user <= CONST_MAX_CI
			check_long_other = CONST_MIN <= len(other) <= CONST_MAX_500

			if check_long_ci and check_long_other:
				old = PathologicalBackground.query.filter_by(ci_user=ci_user).first()

				if old != None:
					old.current_condition=current_condition
					old.surgical_history=surgical_history
					old.transfusional_history=transfusional_history
					old.allergies=allergies
					old.traumatic_history=traumatic_history
					old.hospitalizations=hospitalizations
					old.addictions=addictions
					old.other=other
					db.session.commit()

					return True
		return False

	def deletePathologicalBackground(self, ci_user):
		check_ci 	= (ci_user !=None) and (type(ci_user) == int)
		if check_ci:
			check_long_ci = 1 <= ci_user <= CONST_MAX_CI
			if check_long_ci:
				
				old = PathologicalBackground.query.filter_by(ci_user=ci_user).first()
				
				if old != None:
					db.session.delete(old)
					db.session.commit()
					return True

		return False 	
