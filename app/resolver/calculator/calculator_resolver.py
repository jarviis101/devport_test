from flask import Request

from app.dto.calculator.calculator_dto import CalculatorDTO
from app.exception.calculator.validation_exception import ValidationException


class CalculatorResolver:
    @staticmethod
    def resolve(request: Request) -> CalculatorDTO:
        left_team = request.form.get('left_team')
        right_team = request.form.get('right_team')
        if not left_team or not right_team:
            raise ValidationException('Validation failed')

        return CalculatorDTO(left_team, right_team)
