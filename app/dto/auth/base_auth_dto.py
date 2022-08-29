class BaseAuthDTO:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password = password

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password
