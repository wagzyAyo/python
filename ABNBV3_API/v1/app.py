from flask import Flask
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')
cors = CORS(app=app)

if __name__ == '__main__':
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = '5000'
    app.run(debug=True, host=host, port=port, threaded=True)