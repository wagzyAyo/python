from flask import Flask
from flask_cors import CORS
from bp.bp1 import bpindex

app = Flask(__name__)
CORS(app)
app.register_blueprint(bpindex, url_prefix='/bp')

@app.route('/')
def home():
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=True)