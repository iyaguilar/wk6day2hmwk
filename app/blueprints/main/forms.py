from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, equal_to



class PokemonForm(FlaskForm):
    pokemon_name = StringField("Pokemon Name")
    submit = SubmitField("Get Pokemon Data")
