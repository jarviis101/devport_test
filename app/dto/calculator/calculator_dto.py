class CalculatorDTO:
    def __init__(self, first_team: str, second_team: str):
        self.first_team = first_team
        self.second_team = second_team

    def get_first_team(self):
        return self.first_team

    def get_second_team(self):
        return self.second_team
