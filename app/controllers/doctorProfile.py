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

	def insertDoctorProfile(self, ci_user, sex, date_of_birth, marital_status, telephone, address,
		habilities, pregrade, postgrade, experience, courses, publications, awards):
		
		check_ci_user 			= (type(ci_user) == int) and (ci_user!=None)

		check_sex 				= type(sex) == str 
		check_date_of_birth 	= type(date_of_birth) == datetime.date
		check_marital_status	= type(marital_status) == str
		check_telephone			= type(telephone) == str  
		check_address			= type(address) == str 

		check_habilities 	= type(habilities) == str
		check_pregrade 		= type(pregrade) == str
		check_postgrade 	= type(postgrade) == str
		check_experience 	= type(experience) == str
		check_courses 		= type(courses) == str
		check_publications 	= type(publications) == str
		check_awards 		= type(awards) == str

		if check_ci_user and check_sex and check_date_of_birth and check_marital_status and check_telephone and check_address and \
		check_habilities and check_pregrade and check_postgrade and check_experience and check_courses and check_publications and check_awards:
			
			check_long_ci_user 	= (CONST_MIN <= ci_user <= 99999999)

			check_long_sex 				= len(sex) <= CONST_MAX_SEX
			check_long_marital_status	= len(marital_status) <= CONST_MAX_TEL
			check_long_telephone		= len(telephone) <= CONST_MAX_TEL
			check_long_address			= len(address) <= CONST_MAX_ADDRESS
			
			check_long_habilities 	= len(habilities) <= CONST_MAX_EXP
			check_long_pregrade 	= len(pregrade) <= CONST_MAX_PREGRADE
			check_long_postgrade 	= len(postgrade) <= CONST_MAX_PREGRADE
			check_long_experience 	= len(experience) <= CONST_MAX_EXP
			check_long_courses 		= len(courses) <= CONST_MAX_EXP
			check_long_publications = len(publications) <= CONST_MAX_EXP
			check_long_awards 		= len(awards) <= CONST_MAX_EXP

			if check_long_ci_user and check_long_sex and check_long_marital_status and check_long_telephone and check_long_address and \
			check_long_habilities and check_long_pregrade and check_long_postgrade and check_long_experience and check_long_courses and check_long_publications and check_long_awards:
				
				target_profile = DoctorProfile.query.filter_by(ci_user=ci_user).first()

				if not target_profile:
					new_doctor = DoctorProfile(ci_user,
												sex, 
												date_of_birth, 
												marital_status, 
												telephone, 
												address,
												habilities, 
												pregrade, 
												postgrade, 
												experience, 
												courses, 
												publications, 
												awards)		

					db.session.add(new_doctor)
					db.session.commit()
					return True
		return False
			

	def updateDoctorProfile(self, ci_user, sex, date_of_birth, marital_status, telephone, address,
	habilities, pregrade, postgrade, experience, courses, publications, awards):

		check_ci_user 			= (type(ci_user) == int) and (ci_user!=None)

		check_sex 				= type(sex) == str
		check_date_of_birth 	= type(date_of_birth) == datetime.date
		check_marital_status	= type(marital_status) == str
		check_telephone			= type(telephone) == str
		check_address			= type(address) == str

		check_habilities 	= type(habilities) == str
		check_pregrade 		= type(pregrade) == str
		check_postgrade 	= type(postgrade) == str
		check_experience 	= type(experience) == str
		check_courses 		= type(courses) == str
		check_publications 	= type(publications) == str
		check_awards 		= type(awards) == str

		if check_ci_user and check_sex and check_date_of_birth and check_marital_status and check_telephone and check_address and \
		check_habilities and check_pregrade and check_postgrade and check_experience and check_courses and  check_publications and check_awards:
			
			check_long_sex 				= len(sex) <= CONST_MAX_SEX
			check_long_marital_status	= len(marital_status) <= CONST_MAX_TEL
			check_long_telephone		= len(telephone) <= CONST_MAX_TEL
			check_long_address			= len(address) <= CONST_MAX_ADDRESS

			check_long_habilities 	= len(habilities) <= CONST_MAX_EXP
			check_long_pregrade 	= len(pregrade) <= CONST_MAX_PREGRADE
			check_long_postgrade 	= len(postgrade) <= CONST_MAX_PREGRADE
			check_long_experience 	= len(experience) <= CONST_MAX_EXP
			check_long_courses 		= len(courses) <= CONST_MAX_EXP
			check_long_publications = len(publications) <= CONST_MAX_EXP
			check_long_awards 		= len(awards) <= CONST_MAX_EXP

			if check_long_sex and check_long_marital_status and check_long_telephone and check_long_address and \
			check_long_habilities and check_long_pregrade and check_long_postgrade and check_long_experience and check_long_courses and check_long_publications and check_long_awards:
				
				target_profile = DoctorProfile.query.filter_by(ci_user=ci_user).first()

				if target_profile != None:

					target_profile.sex = sex
					target_profile.date_of_birth = date_of_birth
					target_profile.marital_status = marital_status
					target_profile.telephone = telephone
					target_profile.address = address

					target_profile.habilities = habilities
					target_profile.pregrade = pregrade
					target_profile.postgrade = postgrade
					target_profile.experience = experience
					target_profile.courses = courses
					target_profile.publications = publications
					target_profile.awards = awards

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
