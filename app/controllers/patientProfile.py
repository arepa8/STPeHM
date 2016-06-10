import sys
sys.path.append('app/')
sys.path.append('../')

from models import *

CONST_MIN = 1
CONST_MAX_ALLER = 500
CONST_MAX_HEIGTH = 15
CONST_MAX_DIAB = 3
CONST_MAX_CONTACT = 100
class patientProfile():

	def insertPatientProfile(self, ci_patient, heigth, weigth, blood_type, diabetic, allergies, emergency_contact, emergency_number,comments):
		check_ci_patient = (type(ci_patient) == int) and (ci_patient != None)
		check_heigth 	= (type(heigth) == str) and (heigth != None)
		check_weigth 	= (type(weigth) == str) and (weigth != None)
		check_blood_type = (type(blood_type) == str) and (blood_type != None)
		check_diabetic 	= (type(diabetic) == str) and (diabetic != None)
		check_allergies = (type(allergies) == str) and (allergies != None)
		check_emergency_contact = (type(emergency_contact) == str) and (emergency_contact != None)
		check_emergency_number = (type(emergency_number) == str) and (emergency_number != None)
		check_comments 	= (type(comments) == str) and (comments != None)

		if check_ci_patient and check_heigth and check_weigth and check_blood_type and check_diabetic and check_allergies and check_emergency_contact and check_emergency_number and check_comments:
			check_long_ci_patient 	= (CONST_MIN <= ci_user <= 99999999)
			check_long_heigth 		= (CONST_MIN <= len(heigth) <= CONST_MAX_HEIGTH)
			check_long_weigth 		= (CONST_MIN <= len(weigth) <= CONST_MAX_HEIGTH)
			check_long_blood_type 	= (CONST_MIN <= len(blood_type) <= CONST_MAX_DIAB)
			check_long_diabetic 	= (CONST_MIN <= len(diabetic) <= CONST_MAX_DIAB)
			check_long_allergies 	= (CONST_MIN <= len(allergies) <= CONST_MAX_ALLER)
			check_long_emer_contact = (CONST_MIN <= len(emergency_contact) <= CONST_MAX_CONTACT)
			check_long_emer_number 	= (CONST_MIN <= len(emergency_number) <= CONST_MAX_HEIGTH)
			check_long_comments 	= (CONST_MIN <= len(comments) <= CONST_MAX_ALLER)

			if check_long_ci_patient and check_long_heigth and check_long_weigth and check_long_blood_type and check_long_diabetic and check_long_allergies and check_long_emer_contact and check_long_emer_number and check_long_comments:
				target_profile = PatientProfile.query.filter_by(ci_patient=ci_patient).first()
			
				if not target_profile:
					new_profile = PatientProfile(ci_patient, heigth, weigth, blood_type, diabetic, allergies, emergency_contact, emergency_number,comments)
					db.session.add(new_profile)
					db.session.commit()
					return True 
		return False

	def updatePatientProfile(self, ci_patient, heigth, weigth, blood_type, diabetic, allergies, emergency_contact, emergency_number,comments):
		check_ci_patient = (type(ci_patient) == int) and (ci_patient != None)
		check_heigth 	= (type(heigth) == str) and (heigth != None)
		check_weigth 	= (type(weigth) == str) and (weigth != None)
		check_blood_type = (type(blood_type) == str) and (blood_type != None)
		check_diabetic 	= (type(diabetic) == str) and (diabetic != None)
		check_allergies = (type(allergies) == str) and (allergies != None)
		check_emergency_contact = (type(emergency_contact) == str) and (emergency_contact != None)
		check_emergency_number = (type(emergency_number) == str) and (emergency_number != None)
		check_comments 	= (type(comments) == str) and (comments != None)

		if check_ci_patient and check_heigth and check_weigth and check_blood_type and check_diabetic and check_allergies and check_emergency_contact and check_emergency_number and check_comments:
			check_long_ci_patient 	= (CONST_MIN <= ci_user <= 99999999)
			check_long_heigth 		= (CONST_MIN <= len(heigth) <= CONST_MAX_HEIGTH)
			check_long_weigth 		= (CONST_MIN <= len(weigth) <= CONST_MAX_HEIGTH)
			check_long_blood_type 	= (CONST_MIN <= len(blood_type) <= CONST_MAX_DIAB)
			check_long_diabetic 	= (CONST_MIN <= len(diabetic) <= CONST_MAX_DIAB)
			check_long_allergies 	= (CONST_MIN <= len(allergies) <= CONST_MAX_ALLER)
			check_long_emer_contact = (CONST_MIN <= len(emergency_contact) <= CONST_MAX_CONTACT)
			check_long_emer_number 	= (CONST_MIN <= len(emergency_number) <= CONST_MAX_HEIGTH)
			check_long_comments 	= (CONST_MIN <= len(comments) <= CONST_MAX_ALLER)

			if check_long_ci_patient and check_long_heigth and check_long_weigth and check_long_blood_type and check_long_diabetic and check_long_allergies and check_long_emer_contact and check_long_emer_number and check_long_comments:
				target_profile = PatientProfile.query.filter_by(ci_patient=ci_patient).first()
			
				if target_profile:
					target_profile.ci_patient = ci_patient
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

	def getPatientProfileById(self, id):
		check_id = (type(id) == int) and (id!=None)
		if check_id:
			check_long_id = (CONST_MIN <= id)
			if check_long_id:
				result = Profile.query.filter_by(id=id).first()
				return result
		return []

	def deletePatientProfile(self, id):
		check_id = (id != None) and (type(id) == int)
		if check_id:
			target_profile = PatientProfile.query.filter_by(id=id).first()
			if target_profile:
				db.session.delete(target_profile)
				db.session.commit()
				return True
		return False

	def getAllPatientProfiles():
		return PatientProfile.query.all()
