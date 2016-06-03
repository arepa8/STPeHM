import sys
sys.path.append('app/')

from models import *

# Constantes

CONST_MIN_CI = 1
CONST_MAX_CI = 999999999
CONST_MIN_ID = 1
CONST_MAX_ID = 999999999

class doctorSpecialization():

	def insertDS(self, uci, sid):
		check_uci = (uci != None) and (type(uci) == int)
		check_sid = (sid != None) and (type(sid) == int)
		if check_uci and check_sid:
			check_lon_uci = CONST_MIN_CI <= uci <= CONST_MAX_CI
			check_lon_sid = CONST_MIN_ID <= sid <= CONST_MAX_ID
			if check_lon_uci and check_lon_sid:
				check_doctor_exists = User.query.filter_by(ci=uci).first()
				check_spec_exists = Specialization.query.filter_by(id=sid).first()
				if check_doctor_exists and check_spec_exists and int(check_doctor_exists.role) == 1:
					ds = Doctor_Specialization(uci, sid)
					db.session.add(ds)
					db.session.commit()
					return True
		return False

	def modifyDS(self, id, uci, sid):
		check_uci = (uci != None) and (type(uci) == int)
		check_sid = (sid != None) and (type(sid) == int)
		if check_uci and check_sid:
			check_lon_uci = CONST_MIN_CI <= uci <= CONST_MAX_CI
			check_lon_sid = CONST_MIN_ID <= sid <= CONST_MAX_ID
			if check_lon_uci and check_lon_sid:
				check_doctor_exists = User.query.filter_by(ci=uci).first()
				check_spec_exists = Specialization.query.filter_by(id=sid).first()
				if check_doctor_exists and check_spec_exists:
					ds = Doctor_Specialization.query.filter_by(id=id).first()
					ds.doctor = uci
					ds.speciality = sid
					db.session.commit()
					return True
		return False

	def deleteDS(self, id):
		check_id = (id != None) and (type(id) == int)
		if check_id:
			check_long_id = CONST_MIN_ID <= id <= CONST_MAX_ID
			if (check_long_id):
				ds = Doctor_Specialization.query.filter_by(id=id).first()
				if ds:
					db.session.delete(ds)
					db.session.commit()
					return True
		return False

	def getDSByID(self, id):
		check_id = (id != None) and (type(id) == int)
		if check_id:
			check_long_id = CONST_MIN_ID <= id <= CONST_MAX_ID
			if check_long_id:
				ds = Doctor_Specialization.query.filter_by(id=id).first()
				return ds
		return None

	def getAllDS(self):
		return Doctor_Specialization.query.all()