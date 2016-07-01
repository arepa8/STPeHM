import sys
#sys.path.append('app/')
sys.path.append('../')
from models import *

# Constantes
CONST_MIN		= 0
CONST_MAX_100	= 100
CONST_MAX_500	= 500
CONST_MAX_CI	= 999999999

class familyBackground():
	""" Constrolador de Antecedentes Familiares """

	def insertFamilyBackground(self,ci_user,asthma,cancer,heartdisease,diabetes,liverdisease,hypertension,other):
		check_ci 	= (ci_user !=None) and (type(ci_user) == int)
		check_other = type(other) == str
		print("1")

		if (check_ci and check_other):
			print("2")	
			check_long_ci = 1 <= ci_user <= CONST_MAX_CI
			check_long_other = CONST_MIN <= len(other) <= CONST_MAX_500
			
			if check_long_ci and check_long_other:
				print("3")
				old = FamilyBackground.query.filter_by(ci_user=ci_user).first()

				if old == None:
					print("4")
					new = FamilyBackground(ci_user,asthma,
										cancer,
										heartdisease,
										diabetes,
										liverdisease,
										hypertension,
										other)
					db.session.add(new)
					db.session.commit()
					return True
		return False

	def updateFamilyBackground(self,ci_user,asthma,cancer,heartdisease,diabetes,liverdisease,hypertension,other):

		check_ci 	= (ci_user !=None) and (type(ci_user) == int)
		check_other = type(other) == str
		print("1")
		if (check_ci and check_other):
			print("2")
			check_long_ci = 1 <= ci_user <= CONST_MAX_CI
			check_long_other = CONST_MIN <= len(other) <= CONST_MAX_500

			if check_long_ci and check_long_other:
				print("3")
				old = FamilyBackground.query.filter_by(ci_user=ci_user).first()

				if old != None:
					print("4")
					old.asthma=asthma
					old.cancer=cancer
					old.heartdisease=heartdisease
					old.diabetes=diabetes
					old.liverdisease=liverdisease
					old.hypertension=hypertension
					old.other=other
					db.session.commit()
					return True
		return False

	def deleteFamilyBackground(self,ci_user):
		
		old = FamilyBackground.query.filter_by(ci_user=ci_user).first()
		
		if old != None:
			db.session.delete(old)
			db.session.commit()
			return True

		return False 	
