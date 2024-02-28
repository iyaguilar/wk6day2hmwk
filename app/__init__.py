from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin
from app.models import db, User


app = Flask(__name__)

app.config.from_object(Config)

login_manager=LoginManager()

login_manager.init_app(app)
db.init_app(app)
migrate = Migrate(app, db)
@login_manager.user_loader
def user_id(user_id):
    return User.query.get(int(user_id))
from .blueprints.main import main
print(main)
from .blueprints.auth import auth
app.register_blueprint(main)
app.register_blueprint(auth)

