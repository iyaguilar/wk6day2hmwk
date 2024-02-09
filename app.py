from flask import Flask, request, render_template 
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    
    if request.method == "POST":
        pokemon_name = request.form.get("pokemon_name")
        pokemon_data = get_pokemon_info("pokemon_name")
        return render_template("pokemon.html", pokemon_data=pokemon_data)

    return render_template("pokemon_form.html")
    


def get_pokemon_info(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/ditto#.json'
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



    
