from functools import wraps
from flask import flash, redirect, render_template, \
   request, session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError 


from .forms import LoginForm
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

@profiles_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(tele_number=request.form['telegram_number']).filter_by(payment_verify=1).first()
            if user is not None and str(user.password) == str(request.form['password']):
                session['logged_in'] = True
                session['name'] = user.name
                return redirect(url_for('profiles.profile'))
            else:
                "user credentials"
        else:
            print "not validate"
    else:
        print "request.method"

    return render_template('login.html', form=form, error=error)

@profiles_blueprint.route('/logout')
@login_required
def logout():
    session.pop("logged_in", None)
    return redirect(url_for('blog.blog', pageNumber=1))

