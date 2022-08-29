from app.dto.calculator.calculator_dto import CalculatorDTO


class IndexCalculator:
    MIN_INDEX_VALUE = 0.01
    MAX_INDEX_VALUE = 1.00

    def calculate(self, dto: CalculatorDTO):
        index = self.MIN_INDEX_VALUE
        first_team_set = list(dto.get_first_team())
        second_team_set = list(dto.get_second_team())

        for first_team_letter in first_team_set:
            for second_team_letter in second_team_set:
                if first_team_letter == second_team_letter:
                    pass
        return index
