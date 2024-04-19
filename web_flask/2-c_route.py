#!/usr/bin/python3
"""starts a web app application and displays message on a web app."""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def disp():
    """This returns a specific message."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def disp_path():
    """This returns a specific message."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def disp_args(text):
    """This returns a specific message."""
    return "C " + text.replace("_", "")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
