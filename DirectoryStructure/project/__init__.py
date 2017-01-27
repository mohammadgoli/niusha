from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from project.BLUEPRINTNAME.views import BLUEPRINTNAME_blueprint

app.register_blueprint(BLUEPRINTNAME_blueprint)