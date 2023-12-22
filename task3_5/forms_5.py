from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,DateField,BooleanField
from wtforms.validators import DataRequired, EqualTo,Email,Length


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    birthday = DateField('Birthday',validators=[DataRequired()])
    consent_personal = BooleanField('Consent to Personal Data',validators=[DataRequired()])