from functools import wraps
from flask import flash, redirect, render_template, \
   request, session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError 


#from .forms import $$
from project import db
from project.models import User



#This bluePrint includes user registration and users profile system 
profiles_blueprint = Blueprint('profiles', __name__)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('profiles.login'))
    return wrap


@profiles_blueprint.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@profiles_blueprint.route('/login')
def login():
    session["logged_in"]=True
    return redirect(url_for('blog.blog', pageNumber=1))

@profiles_blueprint.route('/logout')
@login_required
def logout():
    session.pop("logged_in", None)
    return redirect(url_for('blog.blog', pageNumber=1))

