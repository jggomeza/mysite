# Librerias de Formularios
from wtforms import Form, BooleanField, DateField, DateTimeField, DecimalField, FileField, MultipleFileField, FloatField, IntegerField, RadioField, SelectField, SelectMultipleField, SubmitField, StringField, HiddenField, PasswordField, TextAreaField
from wtforms.validators import DataRequired

class FormLogin(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FormRegister(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')