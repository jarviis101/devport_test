class UpdatePasswordDTO:
    def __init__(self, password: str):
        self.password = password

    def get_password(self) -> str:
        return self.password

    def set_password(self, password: str) -> None:
        self.password = password
