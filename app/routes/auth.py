import flask_login
from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from app import client
from app.exception.auth.passwords_not_equals_exception import PasswordsNotEqualsException
from app.exception.auth.user_register_validation_exception import UserRegisterValidationException
from app.resolver.auth.auth_resolver import LoginResolver, RegisterResolver
from app.service.auth import RegisterService, LoginService

auth = Blueprint('auth', __name__)
register_service = RegisterService(client.db)
login_service = LoginService(client.db)


@auth.route('/login', methods=['GET'])
def login() -> str:
    return render_template('login.html', user=flask_login.current_user)


@auth.route('/login', methods=['POST'])
def login_action() -> Response:
    dto = LoginResolver.resolve(request)
    try:
        login_service.login(dto)
    except UserRegisterValidationException as ex:
        flash(ex.args[0], 'error')
        return redirect(url_for('auth.login'))

    return redirect(url_for('main.profile'))


@auth.route('/signup', methods=['GET'])
def signup() -> str:
    return render_template('signup.html', user=flask_login.current_user)


@auth.route('/signup', methods=['POST'])
def signup_action() -> Response:
    try:
        dto = RegisterResolver.resolve(request)
    except PasswordsNotEqualsException as ex:
        flash(ex.args[0], 'error')
        return redirect(url_for('auth.signup'))

    register_service.register(dto)
    flash('Successfully registered')
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout() -> Response:
    flask_login.logout_user()
    return redirect(url_for('main.index'))
