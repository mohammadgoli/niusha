from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from project.homepage.views import homepage_blueprint
from project.registeration.views import registeration_blueprint 
from project.blog.views import blog_blueprint
from project.profiles.views import profiles_blueprint


app.register_blueprint(homepage_blueprint)
app.register_blueprint(registeration_blueprint)
app.register_blueprint(blog_blueprint)
app.register_blueprint(profiles_blueprint)