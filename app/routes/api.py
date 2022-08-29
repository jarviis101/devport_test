import flask_login
from flask import Blueprint, request, jsonify, Response

from app.exception.calculator.validation_exception import ValidationException
from app.resolver.calculator.calculator_resolver import CalculatorResolver
from app.service.calculator import IndexCalculator

api = Blueprint('api', __name__)
api.url_prefix = '/api'
cl = IndexCalculator()


@api.route('/calculator', methods=['POST'])
@flask_login.login_required
def calculator() -> Response:
    try:
        dto = CalculatorResolver.resolve(request)
    except ValidationException as ex:
        return jsonify(
            error=ex.args[0]
        )
    index = cl.calculate(dto)
    return jsonify(
        response=index
    )
