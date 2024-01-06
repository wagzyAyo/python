from flask import Flask
from bp.hello import helloworld_bp
from bp.calculator.calculator import calculator_bp

app = Flask(__name__)
app.register_blueprint(helloworld_bp)
app.register_blueprint(calculator_bp, url_prefix='/calculator')


if __name__ == '__main__':
    app.run(debug=True)