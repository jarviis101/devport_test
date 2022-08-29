import json


class CalculatorDTO:
    def __init__(self, left_team: str, right_team: str):
        self.left_team = left_team
        self.right_team = right_team

    def get_left_team(self):
        return self.left_team

    def get_right_team(self):
        return self.right_team


class CalculatorDTOEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CalculatorDTO):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
