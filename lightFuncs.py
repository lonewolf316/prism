import threading, time

def setFade():
    t = threading.currentThread()
    x=0
    while getattr(t, "doRun", True):
        print("Running thread", x, t.doRun)
        x+=1
        time.sleep(2)
    print("stopping thread")