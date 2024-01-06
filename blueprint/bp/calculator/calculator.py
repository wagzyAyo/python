from flask import Blueprint, redirect,url_for

calculator_bp = Blueprint("calculator", __name__)

@calculator_bp.route('/')
def index():
    return 'Welcome to the calculator functionality app'

@calculator_bp.route('/add/<int:x>/<int:y>')
def add(x,y):
    result= x + y
    return str(result)

@calculator_bp.route('/subtract/<int:x>/<int:y>')
def subtract(x, y):
    result = x - y
    return str(result)

@calculator_bp.route('/divide/<int:x>/<int:y>')
def divide(x, y):
    result= x / y
    return str(result)