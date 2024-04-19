#!/usr/bin/python3
"""This module starts a web app application and displays message on a web app."""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def disp():
    """This returns a specific message."""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def disp_path():
    """This returns a specific message."""
    return "HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
