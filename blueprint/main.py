from flask import Flask
from bp.hello import helloworld_bp

app = Flask(__name__)
app.register_blueprint(helloworld_bp)


if __name__ == '__main__':
    app.run(debug=True)