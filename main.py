from flask import Flask, render_template, request
import neopixel, board


def setStripColor(strip, color):
	"""set all pixels to a color"""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
	strip.show()

strip = neopixel.NeoPixel(board.D10, 12)

# SERVER

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/setColor', methods=['GET', 'POST'])
def setColor():
	r = int(request.args.get('r'))
	g = int(request.args.get('g'))
	b = int(request.args.get('b'))

	strip.fill((r, b, g))
	return 'Let there be light'
