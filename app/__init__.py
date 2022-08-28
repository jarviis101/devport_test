import os

import flask_login
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = f'mongodb://' \
                          f'{os.environ["DB_USER"]}:' \
                          f'{os.environ["DB_PASSWORD"]}@' \
                          f'{os.environ["DB_HOST"]}:27017/' \
                          f'{os.environ["DB_NAME"]}'
app.config['SECRET_KEY'] = 's3cr3t'
client = PyMongo(app)

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

from .routes.auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)
from .routes.main import main as main_blueprint

app.register_blueprint(main_blueprint)