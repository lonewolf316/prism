import threading, time, neopixel
import colorsys

def setFade(strip):
    t = threading.currentThread()
    while getattr(t, "doRun", True):
        for dec in range(0, 1000):
            if getattr(t, "doRun", True):
                x = colorsys.hls_to_rgb(dec/1000, .5, 1)
                colour=[int(round(255*x[0])), int(round(255*x[1])), int(round(255*x[2]))]
                strip.fill(colour)
                time.sleep(0.01)
    print("stopping thread")