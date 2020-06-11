from flask import Flask, render_template, request
import neopixel, board, lightFuncs, threading

def threadHandler(function, functionVarDict):
	global bgThread
	try:
		threadLive = bgThread.is_alive()
	except:
		threadLive = False
		print("bgThread already killed")
	print(threadLive)
	if threadLive:
		bgThread.doRun = False
		bgThread.join()
		print("Running thread killed")
	
	if function=="kill":
		return
	else:
		bgThread = threading.Thread(target=lightFuncs.setFade)
		bgThread.doRun = True
		bgThread.start()

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
	threadHandler("kill", [])
	r = int(request.args.get('r'))
	g = int(request.args.get('g'))
	b = int(request.args.get('b'))

	strip.fill((r, b, g))
	return 'Let there be light'

@app.route('/setFade', methods=['GET', 'POST'])
def setFade():
	threadHandler("setFade", [])
	return 'starting fade'
