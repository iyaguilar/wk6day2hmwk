from flask import Blueprint, request, render_template, url_for, flash, redirect
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from app.models import User
from flask_login import LoginManager
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
    





