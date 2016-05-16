import os
DEBUG = True

_basedir = os.path.abspath(os.path.dirname(__file__))

DATA_PATH = os.path.join(_basedir, 'data')
DEFAULT_TPL = 'default'

USERNAME = 'admin'
PASSWORD = 'default'
SECRET_KEY = 'devel secret key'

URL = 'http://localhost:5000/'
TITLE = 'STPeHM'
VERSION = '0.1'
LANG = 'es'
LANG_DIRECTION = 'ltr'
YEAR = '2012'

del os