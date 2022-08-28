from flask import Request
from werkzeug.security import generate_password_hash

from app.dto.register_dto import RegisterDTO
from app.exception.auth.passwords_not_equals_exception import PasswordsNotEqualsException


class RegisterResolver:
    @staticmethod
    def resolve(request: Request) -> RegisterDTO:
        password = request.form['password']
        confirmed = request.form['confirmed_password']
        if password != confirmed:
            raise PasswordsNotEqualsException('Passwords is not equals')
        username = request.form['username']

        return RegisterDTO(username, generate_password_hash(password, method='sha256'))
