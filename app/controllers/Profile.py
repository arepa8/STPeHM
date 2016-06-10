import sys
#sys.path.append('app/')
sys.path.append('../')

from models import *

CONST_MIN = 1
CONST_MAX_TEL = 15
CONST_MAX_ADDRESS = 100
CONST_MAX_SEX = 10

class profile():

	def insertProfile(self, ci_user, sex, date_of_birth, marital_status, telephone, address):
		check_ci_user 		= (type(ci_user) == int) and (ci_user!=None)
		check_sex 			= (type(sex) == str) and (sex!=None)
		check_date_of_birth = date_of_birth != None
		check_marital_status= (type(marital_status) == str) and (marital_status!=None)
		check_telephone		= (type(telephone) == str) and (telephone!=None)
		check_address		= (type(address) == str) and (address!=None)

		if check_ci_user and check_sex and check_date_of_birth and check_marital_status and check_telephone and check_address:
			check_long_ci_user 		= (CONST_MIN<= ci_user <= 99999999)
			check_long_sex 			= (CONST_MIN<= len(sex) <= CONST_MAX_SEX)
			check_long_marital_status= (CONST_MIN<= len(marital_status) <= CONST_MAX_TEL)
			check_long_telephone	= (CONST_MIN<= len(telephone) <= CONST_MAX_TEL)
			check_long_address		= (CONST_MIN<= len(address) <= CONST_MAX_ADDRESS)
			
			if check_long_ci_user and check_long_sex and check_long_marital_status and check_long_telephone and check_long_address:
				target_profile = Profile.query.filter_by(ci_user=ci_user).first()
			
				if not target_profile:
					new_profile = Profile(ci_user, sex, date_of_birth, marital_status, telephone, address)
					db.session.add(new_profile)
					db.session.commit()
					return True 
		return False

	def updateProfile(self, ci_user, sex, date_of_birth, marital_status, telephone, address):
		check_ci_user 		= (type(ci_user) == int) and (ci_user!=None)
		check_sex 			= (type(sex) == str) and (sex!=None)
		check_date_of_birth = date_of_birth != None
		check_marital_status= (type(marital_status) == str) and (marital_status!=None)
		check_telephone		= (type(telephone) == str) and (telephone!=None)
		check_address		= (type(address) == str) and (address!=None)

		if check_ci_user and check_sex and check_date_of_birth and check_marital_status and check_telephone and check_address:
			check_long_ci_user 		= (CONST_MIN<= ci_user <= 99999999)
			check_long_sex 			= (CONST_MIN<= len(sex) <= CONST_MAX_SEX)
			check_long_marital_status= (CONST_MIN<= len(marital_status) <= CONST_MAX_TEL)
			check_long_telephone	= (CONST_MIN<= len(telephone) <= CONST_MAX_TEL)
			check_long_address		= (CONST_MIN<= len(address) <= CONST_MAX_ADDRESS)
			
			if check_long_ci_user and check_long_sex and check_long_marital_status and check_long_telephone and check_long_address:
				target_profile = Profile.query.filter_by(ci_user=ci_user).first()
			
				if target_profile:
					target_profile.ci_user = ci_user
					target_profile.sex = sex
					target_profile.date_of_birth = date_of_birth
					target_profile.marital_status = marital_status
					target_profile.telephone = telephone
					target_profile.address = address
					db.session.commit()
					return True 
		return False

	def deleteProfile(self, id):
		check_id = (id != None) and (type(id) == int)
		if check_id:
			target_profile = Profile.query.filter_by(id=id).first()
			if target_profile:
				db.session.delete(target_profile)
				db.session.commit()
				return True
		return False

	def getProfile(self, ci_user):
		check_ci_user = (type(ci_user) == int) and (CONST_MIN<= ci_user <= 99999999)
		if check_ci_user:
			result = Profile.query.filter_by(ci_user=ci_user).first()
			return result
		return []

	def getProfileByID(self, id):
		check_id = (type(id) == int) and (id!=None)
		if check_id:
			check_long_id = (CONST_MIN<= id)
			if check_long_id:
				result = Profile.query.filter_by(id=id).first()
				return result
		return []

	def getAllProfiles():
		return Profile.query.all()