# _*_ coding: utf-8 _*_

from functools import wraps
import datetime
import random
import string 

from flask import flash, redirect, render_template, \
   request, session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError 


from .forms import RegisterForm
from project import db
from project.models import User


from suds.client import Client

import sqlite3

# configuratin for payment
WEBSERVICE = 'http://pardano.com/p/webservice/?wsdl'
API = 'mv9bR'
#order_id = 1000 
DESCREPTION = 'registration'
#cost = 25000
USER = "Fatemeh_Valizadeh"
MONTH = 13

#This bluePrint includes user registration and users profile system 
registeration_blueprint = Blueprint('registeration', __name__)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap

# def flash_errors(form):
#     for field, errors in form.errors.items():
#         for error in errors:
#             flash(()


def costDef(classNum):
    if classNum == '1':
        cost = 100
    elif classNum == '2': 
        cost = 30000
    elif classNum == '3':
        cost = 35000
    elif classNum == '4':
        cost = 35000
    elif classNum == '5':
        cost = 40000
    elif classNum == '6':
        cost = 35000
    elif classNum == '7':
        cost = 40000
    elif classNum == '8':
        cost = 40000
    return cost

def userfinder(data):
    return db.session.query(Register).filter_by(tele_number=data).filter_by(class_name=data2).order_by(Register.month.desc()).first()


@registeration_blueprint.route('/test')
def main():
	return "this is a test"

@registeration_blueprint.route('/register', methods=['GET', 'POST'])
def register():
	error = None 
	form = RegisterForm()
	if request.method == 'POST':
	    if form.validate_on_submit():
###                print 'form register'
                Name = form.name.data
                Phone = form.phone.data
                Class = str(form.term.data) + str(MONTH)
                
                Year = 2017
                # Username = 'U{}:{}'.format(Phone, Class[1]) #put flask g for thread problem
                Class = int(Class)
                
                Date = datetime.datetime.now()
                className = 'FrenchOnline{}'.format(Class)

                s = string.lowercase+string.digits
                Password = ''.join(random.sample(s,10))
                new_student = User(
                    Name,
                    # Username,
                    Password,
                    Phone,
                    Class,   
                    Date,
                    Year,
                    False,
                    0
                    )
                db.session.add(new_student)
                db.session.commit()
#                with open("user_list.txt", "w") as user_list:
#                    user_list.write("{}\n".format(userName))                       
                user_id = db.session.query(User).filter_by(tele_number=Phone).\
                filter_by(class_name=Class).order_by(User.date.desc()).first().user_id
                uuid = int(user_id)
                uuid = (uuid * 1000) + Class

                complete_phone = str('+98') + str(Phone)
                return redirect(url_for('registeration.send_request', uuid=uuid))
        else:
            error = "there were an error!"
	return render_template('register.html', form = form,  error = error)

@registeration_blueprint.route('/request/<uuid>', methods=['GET', 'POST'])
def send_request(uuid):
        try:
            term = uuid[-3]
            print term
            term = str(term)
            cost = costDef(term)
        
            # order_id = str(username[2:11]) + str(term)
            # order_id = int(order_id)
            #  Both are obsolete! 
            # order_id = str(username[1:11])
            # order_id = int(order_id)
            order_id = int(uuid)
            print order_id 
        except TypeError:
            return (u'error')
        client = Client(WEBSERVICE)
        result = client.service.requestpayment(API,
                                        cost,
                                        str(url_for('registeration.verify', _external=True)),
				                    	order_id,
                                        DESCREPTION)
        if result > -1:
            return redirect('http://pardano.com/p/payment/' + result)
        else:
            return 'Error'



@registeration_blueprint.route('/verify/', methods=['GET', 'POST'])
def verify():
    client = Client(WEBSERVICE)
    authority = request.args.get('au')
    order_id = request.args.get('order_id')
    try:
        # if len(order_id) < 10:
        #     order_id = str(0) + str(order_id)
        term = order_id[-3]
        cost = costDef(term)
        # phone = str('9') + str(order_id[0:9])
        # phone = str(order_id)
        # phone = db.session.query(User).filter_by(tele_number=Phone).\
        #         filter_by(class_name=Class).order_by(User.date.desc()).first().tele_number
        # print phone
    except TypeError:
        flash(u'canceld')
        return redirect(url_for('homepage.main'))
    # month = datetime.datetime.now().month 
    # userName = 'U:{}:{}'.format(phone, term)
    # className = 'FrenchOnline_term{}_month{}'.format(term, month)
    if authority > -1 :
        result = client.service.verification(API,
				cost,
				authority)
        if str(result) == str(1):
            order_id = int(order_id)
            term = int(term)
            userid = order_id / 1000
            myuser = db.session.query(User).filter_by(user_id=userid).first()
            # conn = sqlite3.connect('project/FrenchOnlineDatabase.db')
            # cur = conn.cursor()
            # cur.execute('''select * from users where user_id={}'''.format(userid))
            # myuser = cur.fetchone()
            myuser.payment_verify = True
            myuser.payment_id = authority
            db.session.commit()
            with open("user_list.txt", "a") as user_list:
                className = str(myuser.class_name)
                user_list.write("{}:{}\n".format(myuser.tele_number, className[-3]))
            flash(u'success')
            flash(authority)
        elif result == -11:
            flash(u'failed')
    else:
        flash(u'canceld')

    return redirect(url_for('homepage.main'))