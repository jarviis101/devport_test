from app.dto.calculator.calculator_dto import CalculatorDTO


class IndexCalculator:
    MIN_INDEX_VALUE = 0.01
    MAX_INDEX_VALUE = 1.00

    def calculate(self, dto: CalculatorDTO):
        first_team_list = list(
            dto.get_first_team().replace(" ", "").lower()
        )
        second_team_list = list(
            dto.get_second_team().replace(" ", "").lower()
        )

        if first_team_list == second_team_list:
            return self.MAX_INDEX_VALUE

        count = 0
        for i in range(min(len(first_team_list), len(second_team_list))):
            if first_team_list[i] == second_team_list[i]:
                count += 1

        if count > 0:
            idx = self.MAX_INDEX_VALUE - (self.MAX_INDEX_VALUE / count)
            return idx
        return self.MIN_INDEX_VALUE
