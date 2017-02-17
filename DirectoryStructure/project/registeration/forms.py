# _*_ coding: utf-8 _*_
from flask_wtf import Form, RecaptchaField
from wtforms import StringField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp



class RegisterForm(Form):
    name = StringField(
        "name",
        validators=[DataRequired(), Length(max=35)])
    phone = StringField(
        "phone",
        validators=[Regexp('^\d*$', message='faulte'), DataRequired(), Length(min=10, max=15)])
    term = SelectField(
        "term",
        validators=[DataRequired()],
        choices=[('1', u'ترم ۱'), ('2', u'ترم ۲'), ('3', u'ترم ۳'), ('4', u'ترم ۴'), ('5', u'ترم ۵'), ('6', u'ترم ۶'), ('7', u'ترم ۷'), ('8', u'ترم ۸')])
    license = BooleanField(
        "license",
        validators=[DataRequired()])
    # recaptcha = RecaptchaField()