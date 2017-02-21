from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# class Login(Form):
#     FieldName = FieldType(
#         'HTMLName',
#         validators=[DataRequired(), Email(), Length(min=num, max=num), EqualTo('HTMLNameP')])

class LoginForm(Form):
    telegram_number = StringField(
        'phone',
        validators=[DataRequired(u'please enter your phone number'), Length(min=10, max=15)])
    password = PasswordField(
        'password',
        validators=[DataRequired()])

