from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, equal_to



class PokemonForm(FlaskForm):
    pokemon_name = StringField("Pokemon Name")
    submit = SubmitField("Create Pokemon Data")

class SearchForm(FlaskForm):
    pokemon_name = StringField("Pokemon Name")
    submit = SubmitField("Get Pokemon Data")

class CatchPokemonForm(FlaskForm):
    submit = SubmitField("Catch Pokemon")

class ReleasePokemonForm(FlaskForm):
    submit = SubmitField("Release Pokemon")

class BattleForm(FlaskForm):
    selected_pokemon = SelectField("Select Pokemon", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Start Battle")