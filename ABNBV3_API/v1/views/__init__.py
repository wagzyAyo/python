from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
helloworld_bp = Blueprint('hello', __name__, url_prefix='/hello')