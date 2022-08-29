import json


class CalculatorDTO:
    def __init__(self, left_team: str, right_team: str):
        self.left_team = left_team
        self.right_team = right_team

    def get_left_team(self) -> str:
        return self.left_team

    def get_right_team(self) -> str:
        return self.right_team
