class UpdatePasswordDTO:
    def __init__(self, password: str):
        self.__password = password

    def get_password(self) -> str:
        return self.__password

    def set_password(self, password: str) -> None:
        self.__password = password
