#!/usr/bin/python3
from flask import Flask
"""This module displays a message on the webpage"""


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def disp():
    """This returns a specific message."""
    return "Hello HBNB!"


run(app, host='0.0.0.0', port=5000)
