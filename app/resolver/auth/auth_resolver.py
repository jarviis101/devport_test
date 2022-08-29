from flask import Request
from werkzeug.security import generate_password_hash

from app.dto.auth.login_dto import LoginDTO
from app.dto.auth.register_dto import RegisterDTO
from app.exception.auth.passwords_not_equals_exception import PasswordsNotEqualsException


class LoginResolver:
    @staticmethod
    def resolve(request: Request) -> LoginDTO:
        username = request.form.get('username')
        password = request.form.get('password')

        return LoginDTO(username, password)


class RegisterResolver:
    @staticmethod
    def resolve(request: Request) -> RegisterDTO:
        password = request.form.get('password')
        confirmed = request.form.get('confirmed_password')
        if password != confirmed:
            raise PasswordsNotEqualsException('Passwords is not equals')
        username = request.form.get('username')

        return RegisterDTO(username, generate_password_hash(password, method='sha256'))
