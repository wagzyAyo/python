from flask import Blueprint, render_template, redirect
from views import helloworld_bp

@helloworld_bp.route('/')
def index():
    return 'Hello world!'

@helloworld_bp.route('/hello')
def hello():
    return 'Hello world Again!'

@helloworld_bp.route('/hello/<name>')
def hello_name(name):
    return f"Hello {name}!"

@helloworld_bp.route('/hellohtml')
def hello_html():
    return render_template('helloworld/hello.html')