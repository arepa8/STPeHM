import sys

sys.append('../')

from models import *

class profile():

	def insertProfile():
		pass

	def updateProfile():
		pass

	def getProfile():
		pass

	def deleteProfile():
		pass

	def getAllProfiles():
		return Profile.query.all()
