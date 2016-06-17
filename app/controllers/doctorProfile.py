import sys
sys.path.append('app/')
sys.path.append('../')

from models import *
import datetime

CONST_MIN = 1
CONST_MAX_TEL = 15
CONST_MAX_ADDRESS = 100
CONST_MAX_SEX = 15
CONST_MAX_PREGRADE = 100
CONST_MAX_EXP = 500

class doctorProfile():

	def insertDoctorProfile(self, ci_user, sex, date_of_birth, marital_status, telephone, address):
		
		check_ci_user 			= (type(ci_user) == int) and (ci_user!=None)

		check_sex 				= type(sex) == str 
		check_date_of_birth 	= type(date_of_birth) == datetime.date
		check_marital_status	= type(marital_status) == str
		check_telephone			= type(telephone) == str  
		check_address			= type(address) == str 


		if check_ci_user and check_sex and check_date_of_birth and check_marital_status and check_telephone and check_address:
			
			check_long_ci_user 	= (CONST_MIN <= ci_user <= 99999999)

			check_long_sex 				= len(sex) <= CONST_MAX_SEX
			check_long_marital_status	= len(marital_status) <= CONST_MAX_TEL
			check_long_telephone		= len(telephone) <= CONST_MAX_TEL
			check_long_address			= len(address) <= CONST_MAX_ADDRESS
			

			if check_long_ci_user and check_long_sex and check_long_marital_status and check_long_telephone and check_long_address:
				
				target_profile = DoctorProfile.query.filter_by(ci_user=ci_user).first()

				if not target_profile:
					new_doctor = DoctorProfile(ci_user,
												sex, 
												date_of_birth, 
												marital_status, 
												telephone, 
												address)		

					db.session.add(new_doctor)
					db.session.commit()
					return True
		return False
			

	def updateDoctorProfile(self, ci_user, sex, date_of_birth, marital_status, telephone, address):

		check_ci_user 			= (type(ci_user) == int) and (ci_user!=None)

		check_sex 				= type(sex) == str
		check_date_of_birth 	= type(date_of_birth) == datetime.date
		check_marital_status	= type(marital_status) == str
		check_telephone			= type(telephone) == str
		check_address			= type(address) == str


		if check_ci_user and check_sex and check_date_of_birth and check_marital_status and check_telephone and check_address:
			
			check_long_sex 				= len(sex) <= CONST_MAX_SEX
			check_long_marital_status	= len(marital_status) <= CONST_MAX_TEL
			check_long_telephone		= len(telephone) <= CONST_MAX_TEL
			check_long_address			= len(address) <= CONST_MAX_ADDRESS


			if check_long_sex and check_long_marital_status and check_long_telephone and check_long_address:
				
				target_profile = DoctorProfile.query.filter_by(ci_user=ci_user).first()

				if target_profile != None:

					target_profile.sex = sex
					target_profile.date_of_birth = date_of_birth
					target_profile.marital_status = marital_status
					target_profile.telephone = telephone
					target_profile.address = address
					db.session.commit()
					return True
		return False

	def getDoctorProfileByCi(self, ci):
		result = DoctorProfile.query.filter_by(ci_user=ci).first()
		return result
		

	def deleteDoctorProfile(self, ci):
		check_ci = (ci != None)
		if check_ci:
			target_profile = DoctorProfile.query.filter_by(ci_user=ci).first()
			if target_profile != None:
				db.session.delete(target_profile)
				db.session.commit()
				return True
		return False

	def getAllDoctorProfiles():
		return DoctorProfile.query.all()
