#! /bin/bash
# runs server with root python instead of virtualenv python
# due to neopixel library installation issue

export FLASK_APP=main.py
export FLASK_DEBUG=1
/usr/bin/python -m flask run --host=0.0.0.0
