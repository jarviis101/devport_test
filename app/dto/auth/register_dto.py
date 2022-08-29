import json


class RegisterDTO:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password
