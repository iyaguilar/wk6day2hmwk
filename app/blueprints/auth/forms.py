# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, equal_to



class PokemonForm(FlaskForm):
    pokemon_name = StringField("Pokemon Name")
    submit = SubmitField("Get Pokemon Data")

class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), equal_to('password')])
    submit_btn= SubmitField('Sign Up')