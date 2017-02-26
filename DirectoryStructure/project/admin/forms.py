from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class AdminLoginForm(Form):
    username = StringField(
        'username',
        validators=[DataRequired(u'please enter your phone number')])
    password = PasswordField(
        'password',
        validators=[DataRequired()])

