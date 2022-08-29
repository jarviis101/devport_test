from flask import Request

from app.dto.auth.login_dto import LoginDTO


class LoginResolver:
    @staticmethod
    def resolve(request: Request) -> LoginDTO:
        username = request.form['username']
        password = request.form['password']

        return LoginDTO(username, password)

