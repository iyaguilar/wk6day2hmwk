# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class PokemonForm(FlaskForm):
    pokemon_name = StringField("Pokemon Name")
    submit = SubmitField("Get Pokemon Data")