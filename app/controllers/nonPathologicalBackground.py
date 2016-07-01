import sys
#sys.path.append('app/')
sys.path.append('../')
from models import *

# Constantes
CONST_MIN		= 0
CONST_MAX_100	= 100
CONST_MAX_500	= 500
CONST_MAX_CI	= 999999999

class nonPathologicalBackground():
	""" Constrolador de Antecedentes Familiares """

	def insertNonPathologicalBackground(self,ci_user,defecation,toothbrushing,cigarrettes,years,beverages,frecuency,physical_activity,frecuency2,other):
		check_ci 	= (ci_user !=None) and (type(ci_user) == int)
		check_other = type(other) == str

		if (check_ci and check_other):

			check_long_ci = 1 <= ci_user <= CONST_MAX_CI
			check_long_other = CONST_MIN <= len(other) <= CONST_MAX_500
			
			if check_long_ci and check_long_other:

				old = NonPathologicalBackground.query.filter_by(ci_user=ci_user).first()

				if old == None:
					new = NonPathologicalBackground(ci_user,
												defecation,
												toothbrushing,
												cigarrettes,
												years,
												beverages,
												frecuency,
												physical_activity,
												frecuency2,
												other)
					db.session.add(new)
					db.session.commit()

					return True
		return False

	def updateNonPathologicalBackground(self,ci_user,defecation,toothbrushing,cigarrettes,years,beverages,frecuency,physical_activity,frecuency2,other):

		check_ci 	= (ci_user !=None) and (type(ci_user) == int)
		check_other = type(other) == str

		if (check_ci and check_other):

			check_long_ci = 1 <= ci_user <= CONST_MAX_CI
			check_long_other = CONST_MIN <= len(other) <= CONST_MAX_500

			if check_long_ci and check_long_other:
				old = NonPathologicalBackground.query.filter_by(ci_user=ci_user).first()

				if old != None:
					old.defecation=defecation
					old.toothbrushing=toothbrushing
					old.cigarrettes=cigarrettes
					old.years=years
					old.beverages=beverages
					old.frecuency=frecuency
					old.physical_activity=physical_activity
					old.frecuency2=frecuency2
					old.other=other
					db.session.commit()
					return True
		return False

	def deleteNonPathologicalBackground(ci_user):
		
		old = NonPathologicalBackground.query.filter_by(ci_user=ci_user).first()
		
		if old != None:
			db.session.delete(old)
			db.session.commit()
			return True

		return False 	
