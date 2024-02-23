from flask import Blueprint, request, render_template, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from models import User
from flask_login import login_required

from ..auth.forms import LoginForm, SignupForm
from flask import render_template, request

auth = Blueprint('auth', __name__, template_folder='templates')


#routes
@auth.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


# New routes for signup and login
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        flash('Success! Thank You for Signing Up', 'success')
        return redirect (url_for('home'))
    else:

        return render_template('signup.html', form=form)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        flash('Login successful', 'success')
        return redirect (url_for('login'))
    else:

        return render_template('login.html', form=form)
    
@auth.route("/")
def home():
    return render_template('home.html')


@auth.route("/pokemon", methods=["GET", "POST"])
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



