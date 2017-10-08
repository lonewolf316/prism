from flask import Flask, render_template, request
from neopixel import *

import time
from neopixel import *

# LED
LED_COUNT = 60
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.SK6812_STRIP_RGBW

def setStripColor(strip, color):
	"""set all pixels to a color"""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
	strip.show()

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()

# SERVER

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/setColor', methods=['GET', 'POST'])
def setColor():
	r = int(request.args.get('r'))
	g = int(request.args.get('g'))
	b = int(request.args.get('b'))
	w = int(request.args.get('w'))
	setStripColor(strip, Color(g, r, b, w));
	return 'Let there be light'
