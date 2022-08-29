import json


class RegisterDTO:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password


class RegisterDTOEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, RegisterDTO):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
