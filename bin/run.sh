#! /bin/bash
# runs server with root python instead of virtualenv python
# due to neopixel library installation issue

export FLASK_APP=main.py
/usr/bin/python3 -m flask run --host=0.0.0.0
