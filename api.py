from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("POKEMON_API_KEY")

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/ditto#.json"
    response = requests.get(url)

    if response.ok:
        data = response.json()

        info = {
            "name": data['name'],
            "base_stat_hp": data["stats"][0]["base_stat"],
            "base_stat_attack": data["stats"][1]["base_stat"],
            "base_stat_defense": data["stats"][2]["base_stat"],
            "ability": data['abilities'][0]['ability']['name'],
            "base_experience": data["base_experience"],
            'sprite_url': data["sprites"]["front_default"]
        }

    return info 
