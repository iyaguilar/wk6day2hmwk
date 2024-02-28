#models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class Pokemon(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username =username
        self.email = email
        self.password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    base_hp = db.Column(db.Integer)
    base_attack = db.Column(db.Integer)
    base_defense = db.Column(db.Integer)
    sprite_img = db.Column(db.String)

    def __init__(self, img_url):
        self.img_url = img_url
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    
    # You can add more fields specific to the team if needed
    
    def save(self):
        db.session.add(self)
        db.session.commit()


