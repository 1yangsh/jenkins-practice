from flask import Flask
import flask_restful
from flask_restful import reqparse
from os import environ as env

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
