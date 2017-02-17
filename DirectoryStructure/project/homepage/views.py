from functools import wraps
from flask import flash, redirect, render_template, \
   request, session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError 


# from .forms import $$
from project import db
from project.models import User




homepage_blueprint = Blueprint('homepage', __name__)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap



@homepage_blueprint.route('/')
@homepage_blueprint.route('/main')
def main():
	return render_template("homepage.html"), 200