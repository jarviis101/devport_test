import flask_login
from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index() -> str:
    return render_template('index.html', user=flask_login.current_user)


@main.route('/profile')
@flask_login.login_required
def profile() -> str:
    return render_template('profile.html', user=flask_login.current_user)
