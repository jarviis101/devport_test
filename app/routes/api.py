import flask_login
from flask import Blueprint, request, flash, redirect, url_for

from app.exception.calculator.validation_exception import ValidationException
from app.resolver.calculator.calculator_resolver import CalculatorResolver
from app.service.calculator import IndexCalculator

api = Blueprint('api', __name__)
api.url_prefix = '/api'
cl = IndexCalculator()


@api.route('/calculator', methods=['POST'])
@flask_login.login_required
def calculator():
    try:
        dto = CalculatorResolver.resolve(request)
    except ValidationException as ex:
        flash(ex.args[0], 'error')
        return redirect(url_for('index.profile'))
    index = cl.calculate(dto)
    return str(index)
    # return calculator.calculate(dto)
