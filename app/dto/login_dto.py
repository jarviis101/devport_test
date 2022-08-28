class LoginDTO:
    def __init__(self, username, password, remember: bool):
        self.username = username
        self.password = password
        self.remember = remember

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_remember(self):
        return self.remember