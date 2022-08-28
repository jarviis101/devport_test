from flask import Request

from app.dto.login_dto import LoginDTO


class LoginResolver:
    @staticmethod
    def resolve(request: Request) -> LoginDTO:
        username = request.form['username']
        password = request.form['password']
        # remember = True if request.form['remember'] else False

        return LoginDTO(username, password, True)

