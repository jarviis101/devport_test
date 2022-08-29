from app.dto.calculator.calculator_dto import CalculatorDTO


class IndexCalculator:
    MIN_INDEX_VALUE = 0.01
    MAX_INDEX_VALUE = 1.00

    def calculate(self, dto: CalculatorDTO):
        index = self.MIN_INDEX_VALUE
        first_team_list = list(dto.get_first_team())
        second_team_list = list(dto.get_second_team())

        if first_team_list == second_team_list:
            return self.MAX_INDEX_VALUE

        if len(first_team_list) != len(second_team_list):
            # TODO check if length`s not equals
            return index
        return index
