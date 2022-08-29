import json

from flask import Request

from app.dto.calculator.calculator_dto import CalculatorDTO
from app.exception.calculator.validation_exception import ValidationException


class CalculatorResolver:
    @staticmethod
    def resolve(request: Request):
        dto = json.loads(
            json.dumps(request.get_json()),
            object_hook=lambda d: CalculatorDTO(**d)
        )

        if not dto.get_left_team() or not dto.get_right_team():
            raise ValidationException('Validation failed')

        return dto
