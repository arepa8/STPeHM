import sys
sys.path.append('app/')
sys.path.append('../')

from models import *
import datetime

CONST_MIN = 1
CONST_MAX_TEL = 15
CONST_MAX_ADDRESS = 100
CONST_MAX_SEX = 15
CONST_MAX_ALLER = 500
CONST_MAX_HEIGTH = 15
CONST_MAX_DIAB = 1
CONST_MAX_BLOOD = 2
CONST_MAX_CONTACT = 100

class patientProfile():

	def insertPatientProfile(self, ci_user, sex, date_of_birth, marital_status, telephone, address,
		heigth, weigth, blood_type, diabetic, allergies, emergency_contact, emergency_number,comments):
		
		check_ci_user 			= (type(ci_user) == int) and (ci_user!=None)

		check_sex 				= type(sex) == str 
		check_date_of_birth 	= type(date_of_birth) == datetime.date
		check_marital_status	= type(marital_status) == str
		check_telephone			= type(telephone) == str  
		check_address			= type(address) == str 

		check_heigth 			= type(heigth) == str
		check_weigth 			= type(weigth) == str
		check_blood_type 		= type(blood_type) == str
		check_diabetic 			= type(diabetic) == str
		check_allergies 		= type(allergies) == str
		check_emergency_contact = type(emergency_contact) == str
		check_emergency_number  = type(emergency_number) == str
		check_comments 			= type(comments) == str

		if check_ci_user and check_sex and check_date_of_birth and check_marital_status and check_telephone and check_address and \
		check_heigth  and check_weigth and check_blood_type and check_diabetic and check_allergies and check_emergency_contact and check_emergency_number and check_comments:

			check_long_ci_user 	= (CONST_MIN <= ci_user <= 99999999)

			check_long_sex 				= len(sex) <= CONST_MAX_SEX
			check_long_marital_status	= len(marital_status) <= CONST_MAX_TEL
			check_long_telephone		= len(telephone) <= CONST_MAX_TEL
			check_long_address			= len(address) <= CONST_MAX_ADDRESS
			
			check_long_heigth 			= len(heigth) <= CONST_MAX_HEIGTH
			check_long_weigth 			= len(weigth) <= CONST_MAX_HEIGTH
			check_long_blood_type 		= len(blood_type) <= CONST_MAX_BLOOD
			check_long_diabetic 		= len(diabetic) <= CONST_MAX_DIAB
			check_long_allergies 		= len(allergies) <= CONST_MAX_ALLER
			check_long_emer_contact 	= len(emergency_contact) <= CONST_MAX_CONTACT
			check_long_emer_number 		= len(emergency_number) <= CONST_MAX_HEIGTH
			check_long_comments 		= len(comments) <= CONST_MAX_ALLER

			if check_long_ci_user and check_long_sex and check_long_marital_status and check_long_telephone and check_long_address and \
			check_long_heigth and check_long_weigth and check_long_blood_type and check_long_diabetic and check_long_allergies and check_long_emer_contact and check_long_emer_number and check_long_comments:
				
				target_profile = PatientProfile.query.filter_by(ci_user=ci_user).first()
			
				if not target_profile:
					
					new_patient = PatientProfile(ci_user,
												sex, 
												date_of_birth, 
												marital_status, 
												telephone, 
												address,
												heigth, 
												weigth, 
												blood_type, 
												diabetic, 
												allergies, 
												emergency_contact, 
												emergency_number,
												comments)
					
					db.session.add(new_patient)
					db.session.commit()
					return True 

		return False

	def updatePatientProfile(self, ci_user, sex, date_of_birth, marital_status, telephone, address,
		heigth, weigth, blood_type, diabetic, allergies, emergency_contact, emergency_number,comments):
		
		check_ci_user 			= (type(ci_user) == int) and (ci_user!=None)

		check_sex 				= type(sex) == str
		check_date_of_birth 	= type(date_of_birth) == datetime.date
		check_marital_status	= type(marital_status) == str
		check_telephone			= type(telephone) == str
		check_address			= type(address) == str

		check_heigth 			= type(heigth) == str
		check_weigth 			= type(weigth) == str
		check_blood_type 		= type(blood_type) == str
		check_diabetic 			= type(diabetic) == str
		check_allergies 		= type(allergies) == str
		check_emergency_contact = type(emergency_contact) == str
		check_emergency_number 	= type(emergency_number) == str
		check_comments 			= type(comments) == str

		if check_ci_user and check_sex and check_date_of_birth and check_marital_status and check_telephone and check_address and \
			check_heigth and check_weigth and check_blood_type and check_diabetic and check_allergies and check_emergency_contact and check_emergency_number and check_comments:
		
			check_long_sex 				= len(sex) <= CONST_MAX_SEX
			check_long_marital_status	= len(marital_status) <= CONST_MAX_TEL
			check_long_telephone		= len(telephone) <= CONST_MAX_TEL
			check_long_address			= len(address) <= CONST_MAX_ADDRESS

			check_long_heigth 			= len(heigth) <= CONST_MAX_HEIGTH
			check_long_weigth 			= len(weigth) <= CONST_MAX_HEIGTH
			check_long_blood_type 		= len(blood_type) <= CONST_MAX_BLOOD
			check_long_diabetic 		= len(diabetic) <= CONST_MAX_DIAB
			check_long_allergies 		= len(allergies) <= CONST_MAX_ALLER
			check_long_emer_contact 	= len(emergency_contact) <= CONST_MAX_CONTACT
			check_long_emer_number 		= len(emergency_number) <= CONST_MAX_HEIGTH
			check_long_comments 		= len(comments) <= CONST_MAX_ALLER

			if check_long_sex and check_long_marital_status and check_long_telephone and check_long_address and \
				check_long_heigth and check_long_weigth and check_long_blood_type and check_long_diabetic and check_long_allergies and check_long_emer_contact and check_long_emer_number and check_long_comments:

				target_profile = PatientProfile.query.filter_by(ci_user=ci_user).first()
			
				if target_profile != None:

					target_profile.sex = sex
					target_profile.date_of_birth = date_of_birth
					target_profile.marital_status = marital_status
					target_profile.telephone = telephone
					target_profile.address = address

					target_profile.heigth = heigth
					target_profile.weigth = weigth
					target_profile.blood_type = blood_type
					target_profile.diabetic = diabetic
					target_profile.allergies = allergies
					target_profile.emergency_contact = emergency_contact
					target_profile.emergency_number = emergency_number
					target_profile.comments = comments

					db.session.commit()
					return True 
		return False

	def getPatientProfileByCi(self, ci):
		
		result = PatientProfile.query.filter_by(ci_user=ci).first()
		return result


	def deletePatientProfile(self, ci):
		check_ci = (ci != None)
		if check_ci:
			target_profile = PatientProfile.query.filter_by(ci_user=ci).first()
			
			if target_profile != None:
				db.session.delete(target_profile)
				db.session.commit()
				return True
		return False

	def getAllPatientProfiles():
		return PatientProfile.query.all()
