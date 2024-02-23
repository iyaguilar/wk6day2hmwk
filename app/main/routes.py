from . import main
from flask import render_template, request, flash, redirect, url_for
import requests
from app.models import User, db
from flask_login import current_user, login_required

# / route is your home route
@main.route('/')
def home():
    return render_template('home.html')