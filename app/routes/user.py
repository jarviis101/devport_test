import flask_login
from flask import Blueprint, render_template, request, jsonify, Response

from app import client
from app.exception.user.empty_password_exception import EmptyPasswordException
from app.resolver.user.user_resolver import UserResolver
from app.service.user import UserService

user = Blueprint('user', __name__)
service = UserService(client.db)


@user.route('/profile')
@flask_login.login_required
def profile() -> str:
    return render_template('profile.html', user=flask_login.current_user)


@user.route('/profile/password', methods=['POST'])
@flask_login.login_required
def change_password() -> Response:
    try:
        dto = UserResolver.resolve(request)
    except EmptyPasswordException as ex:
        return jsonify(
            error=ex.args[0]
        )

    service.password_update(dto, flask_login.current_user)
    return jsonify(
        response='Password successfully update'
    )
