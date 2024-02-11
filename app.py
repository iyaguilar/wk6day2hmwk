from flask import Flask, request, render_template 
import requests

from forms import PokemonForm

from api import get_pokemon_info

from flask_wtf import FlaskForm

from config import Config



from dotenv import load_dotenv 
import os

load_dotenv()

api_key = os.getenv ("POKEMON_API_KEY")


app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/pokemon", methods=["GET", "POST"])
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



    
