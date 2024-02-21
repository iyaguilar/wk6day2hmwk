from flask import Flask, flash, redirect, request, render_template, \
    request, url_for
import requests

from forms import PokemonForm, LoginForm, SignupForm

from api import get_pokemon_info

from flask_wtf import FlaskForm

from config import Config

from dotenv import load_dotenv 
import os

load_dotenv()

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, logout_user
from models import db, User

api_key = os.getenv ("POKEMON_API_KEY")

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Route

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


# New routes for signup and login
@app.route('/signup', methods=['GET', 'POST'])
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

@app.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        flash('Login successful', 'success')
        return redirect (url_for('login'))
    else:

        return render_template('login.html', form=form)


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


if __name__ == "__main__":
    app.run(debug=True)

    
