from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class FormName(Form):
    FieldName = FieldType(
        'HTMLName',
        validators=[DataRequired(), Email(), Length(min=num, max=num), EqualTo('HTMLNameP')])