import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def flask_dash():
  return 'Hello World!'
