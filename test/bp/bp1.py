
from flask import jsonify

from flask import Blueprint

bpindex = Blueprint('bpindex', __name__, url_prefix='/bp')

@bpindex.route('/')
def home():
    return jsonify({'str': 'Hello Again'})