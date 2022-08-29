class UpdatePasswordDTO:
    def __init__(self, password: str):
        self.__password = password

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        self.__password = password
