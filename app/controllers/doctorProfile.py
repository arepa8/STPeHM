import sys
sys.path.append('app/')
sys.path.append('../')

from models import *

CONST_MIN = 1
CONST_MAX_PREGRADE = 100
CONST_MAX_EXP = 500
class doctorProfile():

	def insertDoctorProfile(self, ci_doctor, habilities, pregrade, postgrade, experience, courses, seminars, publications, awards):
		check_ci_doctor 	= (type(ci_doctor) == int) and (ci_doctor != None)
		check_habilities 	= (type(habilities) == str) and (habilities != None)
		check_pregrade 		= (type(pregrade) == str) and (pregrade != None)
		check_postgrade 	= (type(postgrade) == str) and (postgrade != None)
		check_experience 	= (type(experience) == str) and (experience != None)
		check_courses 		= (type(courses) == str) and (courses != None)
		check_seminars 		= (type(seminars) == str) and (seminars != None)
		check_publications 	= (type(publications) == str) and (publications != None)
		check_awards 		= (type(awards) == str) and (awards != None)

		if check_ci_doctor and check_habilities and check_pregrade and check_postgrade and check_experience and check_courses and check_seminars and check_publications and check_awards:
			check_long_ci_doctor 	= (CONST_MIN <= ci_doctor <= 99999999)
			check_long_habilities 	= (CONST_MIN <= len(habilities) <= CONST_MAX_EXP)
			check_long_pregrade 	= (CONST_MIN <= len(pregrade) <= CONST_MAX_PREGRADE)
			check_long_postgrade 	= (CONST_MIN <= len(postgrade) <= CONST_MAX_PREGRADE)
			check_long_experience 	= (CONST_MIN <= len(experience) <= CONST_MAX_EXP)
			check_long_courses 		= (CONST_MIN <= len(courses) <= CONST_MAX_EXP)
			check_long_seminars 	= (CONST_MIN <= len(seminars) <= CONST_MAX_EXP)
			check_long_publications = (CONST_MIN <= len(publications) <= CONST_MAX_EXP)
			check_long_awards 		= (CONST_MIN <= len(awards) <= CONST_MAX_EXP)

			if check_long_ci_doctor and check_long_habilities and check_long_pregrade and check_long_postgrade and check_long_experience and check_long_courses and check_long_seminars and check_long_publications and check_long_awards:
				target_profile = DoctorProfile.query.filter_by(ci_doctor=ci_doctor).first()

				if not target_profile:
					new_profile = DoctorProfile(ci_doctor, habilities, pregrade, postgrade, experience, courses, seminars, publications, awards)
					db.session.add(new_profile)
					db.session.commit()
					return True
		return False
			

	def updateDoctorProfile(self, ci_doctor, habilities, pregrade, postgrade, experience, courses, seminars, publications, awards):
		check_ci_doctor 	= (type(ci_doctor) == int) and (ci_doctor != None)
		check_habilities 	= (type(habilities) == str) and (habilities != None)
		check_pregrade 		= (type(pregrade) == str) and (pregrade != None)
		check_postgrade 	= (type(postgrade) == str) and (postgrade != None)
		check_experience 	= (type(experience) == str) and (experience != None)
		check_courses 		= (type(courses) == str) and (courses != None)
		check_seminars 		= (type(seminars) == str) and (seminars != None)
		check_publications 	= (type(publications) == str) and (publications != None)
		check_awards 		= (type(awards) == str) and (awards != None)

		if check_ci_doctor and check_habilities and check_pregrade and check_postgrade and check_experience and check_courses and check_seminars and check_publications and check_awards:
			check_long_ci_doctor 	= (CONST_MIN <= ci_doctor <= 99999999)
			check_long_habilities 	= (CONST_MIN <= len(habilities) <= CONST_MAX_EXP)
			check_long_pregrade 	= (CONST_MIN <= len(pregrade) <= CONST_MAX_PREGRADE)
			check_long_postgrade 	= (CONST_MIN <= len(postgrade) <= CONST_MAX_PREGRADE)
			check_long_experience 	= (CONST_MIN <= len(experience) <= CONST_MAX_EXP)
			check_long_courses 		= (CONST_MIN <= len(courses) <= CONST_MAX_EXP)
			check_long_seminars 	= (CONST_MIN <= len(seminars) <= CONST_MAX_EXP)
			check_long_publications = (CONST_MIN <= len(publications) <= CONST_MAX_EXP)
			check_long_awards 		= (CONST_MIN <= len(awards) <= CONST_MAX_EXP)

			if check_long_ci_doctor and check_long_habilities and check_long_pregrade and check_long_postgrade and check_long_experience and check_long_courses and check_long_seminars and check_long_publications and check_long_awards:
				target_profile = DoctorProfile.query.filter_by(ci_doctor=ci_doctor).first()

				if target_profile:
					target_profile.ci_doctor = ci_doctor
					target_profile.habilities = habilities
					target_profile.pregrade = pregrade
					target_profile.postgrade = postgrade
					target_profile.experience = experience
					target_profile.courses = courses
					target_profile.seminars = seminars
					target_profile.publications = publications
					target_profile.awards = awards
					db.session.commit()
					return True
		return False

	def getDoctorProfileById(self, id):
		check_id = (type(id) == int) and (id!=None)
		if check_id:
			check_long_id = (CONST_MIN <= id)
			if check_long_id:
				result = Profile.query.filter_by(id=id).first()
				return result
		return []

	def deleteDoctorProfile(self, id):
		check_id = (id != None) and (type(id) == int)
		if check_id:
			target_profile = DoctorProfile.query.filter_by(id=id).first()
			if target_profile:
				db.session.delete(target_profile)
				db.session.commit()
				return True
		return False

	def getAllDoctorProfiles():
		return DoctorProfile.query.all()
