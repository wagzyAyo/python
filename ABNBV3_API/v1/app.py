from flask import Flask
from os import getenv
from flask_cors import CORS
from views import app_views
from views import helloworld_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(blueprint=app_views)
app.register_blueprint(blueprint=helloworld_bp)
host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')

@app.route('/')
def home():
    return {'str': 'Hello world'}

if __name__ == '__main__':
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = '5000'
    app.run(debug=True, host=host, port=port, threaded=True)