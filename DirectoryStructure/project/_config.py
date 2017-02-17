# project/_config.py


import os


# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE = 'FrenchOnlineDatabase.db'
CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH


# recaptcha configuration 
RECAPTCHA_PUBLIC_KEY = '6LfgIiQTAAAAAD4VOs97PZVcVUjhHw_r_TkML0Fz' 
RECAPTCHA_PRIVATE_KEY = '6LfgIiQTAAAAAOluOFcRYtjguCzW-e15-foEIkVU'
RECAPTCHA_PARAMETERS = {'hl': 'fa'}

# payment 

