from . import main
from flask import render_template, request, flash, redirect, url_for
import requests
from app.models import User, db
from flask_login import current_user, login_required
from .forms import PokemonForm

# / route is your home route
@main.route('/')
def home():
    return render_template('home.html')



@main.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    form = PokemonForm() 
    
    if request.method == "POST" and form.validate_on_submit():
        pokemon_name = form.pokemon_name.data
        pokemon_data = get_pokemon_info(pokemon_name)
        return render_template("pokemon.html", pokemon_data=pokemon_data)

    return render_template("pokemon_form.html", form=form)
    


def get_pokemon_info(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/ditto#.json'
    api_key = "8470bcc5-0060-44e2-a0e1-26a7509fcced"
    params = {"key": api_key}
    response = requests.get(url)
    response = requests.get(url)
    if response.ok:
        data = response.json()


        info = {
            "name": data['name'],
            "base_stat_hp": data["stats"][0]["base_stat"],
            "base_stat_attack": data["stats"] [1]["base_stat"],
            "base_stat_defense": data["stats"][2]["base_stat"],
            "ability": data['abilities'][0]['ability']['name'],
            "base_experience": data["base_experience"],
            'sprite_url': data["sprites"]["front_default"]
   }       
    return info  
