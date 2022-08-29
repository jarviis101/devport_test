class CalculatorDTO:
    def __init__(self, left_team: str, right_team: str):
        self.__left_team = left_team
        self.__right_team = right_team

    def get_left_team(self) -> str:
        return self.__left_team

    def get_right_team(self) -> str:
        return self.__right_team
