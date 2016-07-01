import sys
#sys.path.append('app/')
sys.path.append('../')
from models import *

# Constantes
CONST_MIN_ID = 1
CONST_MAX_ID = sys.maxsize
CONST_MIN_ROLE_NAME = 1
CONST_MAX_ROLE_NAME	= 255

class inbox():
	"""Controlador de Inox"""

	def createInbox(self,ci_user,subject,sent_by):
		check_ci_user= type(ci_user) == int
		if check_ci_user:
			check_long_ci_user = CONST_MIN_ROLE_NAME <= len(role_name) <= CONST_MAX_ROLE_NAME
			if check_long_ci_user:
				user = User.query.filter_by(ci=ci_user).first()
				new_inbox = Inbox(user.ci,subject,sent_by)
				db.session.add(new_inbox)
				db.session.commit()
				return True
			else:
				return False
		else:
			return False