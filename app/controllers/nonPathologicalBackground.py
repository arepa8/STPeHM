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
		check_ci 			= (ci_user !=None) and (type(ci_user) == int)
		# check_defecation 	= type(defecation) == str
		# check_toothbrushing = type(toothbrushing) == str
		# check_cigarrettes 	= type(cigarrettes) == str
		# check_years 		= type(years) == str
		# check_beverages 	= type(beverages) == str
		# check_frecuency 	= type(frecuency) == str
		# check_physical_activity = type(physical_activity) == str
		# check_frecuency2 	= type(frecuency2) == str
		check_other 		= type(other) == str

		if (check_ci and check_other):

			check_long_ci 			= 1 <= ci_user <= CONST_MAX_CI
			# check_long_defecation 	= CONST_MIN <= len(defecation) <= CONST_MAX_100
			# check_long_toothbrushing= CONST_MIN <= len(toothbrushing) <= CONST_MAX_100
			# check_long_cigarrettes	= CONST_MIN <= len(cigarrettes) <= CONST_MAX_100
			# check_long_years		= CONST_MIN <= len(years) <= CONST_MAX_100
			# check_long_beverages	= CONST_MIN <= len(beverages) <= CONST_MAX_100
			# check_long_frecuency 	= CONST_MIN <= len(frecuency) <= CONST_MAX_100
			# check_long_physical_activity = CONST_MIN <= len(physical_activity) <= CONST_MAX_500
			# check_long_frecuency2	= CONST_MIN <= len(frecuency2) <= CONST_MAX_100
			check_long_other 		= CONST_MIN <= len(other) <= CONST_MAX_500
			
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
		# check_defecation = type(defecation) == str
		# check_toothbrushing = type(toothbrushing) == str
		# check_cigarrettes = type(cigarrettes) == str
		# check_years = type(years) == str
		# check_beverages = type(beverages) == str
		# check_frecuency = type(frecuency) == str
		# check_physical_activity = type(physical_activity) == str
		# check_frecuency2 = type(frecuency2) == str
		check_other = type(other) == str


		if (check_ci and check_other):

			check_long_ci = 1 <= ci_user <= CONST_MAX_CI
			# check_long_defecation 	= CONST_MIN <= len(defecation) <= CONST_MAX_100
			# check_long_toothbrushing= CONST_MIN <= len(toothbrushing) <= CONST_MAX_100
			# check_long_cigarrettes	= CONST_MIN <= len(cigarrettes) <= CONST_MAX_100
			# check_long_years		= CONST_MIN <= len(years) <= CONST_MAX_100
			# check_long_beverages	= CONST_MIN <= len(beverages) <= CONST_MAX_100
			# check_long_frecuency 	= CONST_MIN <= len(frecuency) <= CONST_MAX_100
			# check_long_physical_activity = CONST_MIN <= len(physical_activity) <= CONST_MAX_500
			# check_long_frecuency2	= CONST_MIN <= len(frecuency2) <= CONST_MAX_100
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

	def deleteNonPathologicalBackground(self, ci_user):
		
		check_ci 	= (ci_user !=None) and (type(ci_user) == int)
		
		if check_ci:
			check_length = CONST_MIN < ci_user <= CONST_MAX_CI
			
			if check_length:
				old = NonPathologicalBackground.query.filter_by(ci_user=ci_user).first()
				
				if old != None:
					db.session.delete(old)
					db.session.commit()
					return True

		return False 	
