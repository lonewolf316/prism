from flask import Flask, render_template, request
from neopixel import *

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'
