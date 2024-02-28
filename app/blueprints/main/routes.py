from . import main
from flask import render_template, request, flash, redirect, url_for
import requests
from app.models import Pokemon, User, db
from flask_login import current_user, login_required
from .forms import PokemonForm, SearchForm, CatchPokemonForm, ReleasePokemonForm, BattleForm 

# / route is your home route
@main.route('/')
def home():
    return render_template('base.html')

@main.route("/pokemon", methods=["GET", "POST"])
def pokemon():
    form = PokemonForm() 
    
    if request.method == "POST" and form.validate_on_submit():
        pokemon_name = form.pokemon_name.data
        

        pokemon_data = get_pokemon_info(pokemon_name)
        

        return render_template("pokemon.html", pokemon_data=pokemon_data)
    
    return render_template("pokemon_form.html", form=form)

@main.route('/get_pokemon_info/<pokemon_name>', methods=['GET'])
def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}.json'
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
    else:

        #Handle in case API call fails
        flash("Failed to retrieve Pokemon data.", 'danger')
    
    return None

@main.route('/catch/<int:pokemon_id>', methods=['GET', 'POST'])
@login_required
def catch_pokemon(pokemon_id):
    pokemon = Pokemon.query.get(pokemon_id)
    catch_form = CatchPokemonForm()

    if catch_form.validate_on_submit():
        # Logic to check and add Pokemon to user's team goes here
        
        if pokemon not in current_user.team and len(current_user.team) < 6:
            current_user.team.append(pokemon)
            db.session.commit()
            flash(f"You caught {pokemon.name}!", 'success')
        else:
            flash("You already have this Pokemon in your team or your team is full.", 'danger')

        return redirect(url_for('index'))

    return render_template('catch_pokemon.html', pokemon=pokemon, form=catch_form)

# Route to view user's Pokemon team
@main.route('/my_team')
@login_required
def my_team():
    
    return render_template('my_team.html', user=current_user)

# Route to release Pokemon from user's team
@main.route('/release/<int:pokemon_id>', methods=['POST'])
@login_required
def release_pokemon(pokemon_id):
    release_form = ReleasePokemonForm()

    if release_form.validate_on_submit():
        
        pokemon = Pokemon.query.get(pokemon_id)

        if pokemon in current_user.team:
            current_user.team.remove(pokemon)
            db.session.commit()
            flash(f"You released {pokemon.name} from your team.", 'success')
        else:
            flash("This Pokemon is not in your team.", 'danger')

    return redirect(url_for('my_team'))


@main.route('/attack/<int:opponent_id>', methods=['GET', 'POST'])
@login_required
def attack(opponent_id):
    # Get user's and opponent's Pokemo
    user_pokemon = user_attack_sum(current_user.id)
    opponent_pokemon = opponent_attack_sum(opponent_id)

    if request.method == 'POST':
        # Calculate the winner based on some rules
        # Assume the Pokemon with higher attack wins
        user_attack_sum = sum(pokemon['base_attack'] for pokemon in user_pokemon)
        opponent_attack_sum = sum(pokemon['base_attack'] for pokemon in opponent_pokemon)

        if user_attack_sum > opponent_attack_sum:
            winner = 'You'
        elif user_attack_sum < opponent_attack_sum:
            winner = 'Opponent'
        else:
            winner = 'It\'s a tie'

        flash(f'Battle result: {winner} wins!', 'info')

    # Assuming that the database connection is handled elsewhere, no need to close it here

    return render_template('battle.html', user_pokemon=user_pokemon, opponent_pokemon=opponent_pokemon)

@main.route('/battle', methods=['GET', 'POST'])
def battle():
    form = BattleForm()

    if request.method == 'POST' and form.validate_on_submit():
        pokemon_name = form.selected_pokemon.data
        pokemon_data = pokemon_data(pokemon_name)

        # Determine if it's a valid battle
        pokemon_battle = bool(pokemon_data)

        if pokemon_battle:
            flash(f'Battle started with {pokemon_name}!', 'info')
        else:
            flash(f'Invalid Pokemon selected for battle!', 'error')

        return redirect(url_for('battle'))

    # If it's a GET request or the form didn't validate on submit
    return render_template('battle.html', pokemon_battle=pokemon_battle, pokemon_data=pokemon_data, form=BattleForm())
