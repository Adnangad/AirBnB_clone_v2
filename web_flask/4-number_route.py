#!/usr/bin/python3
"""starts a web app application and displays message on a web app."""
from flask import Flask, abort


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
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def disp_py(text):
    """This returns a specific message."""
    if text is None:
        return "Python is cool"
    return "Python " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
def disp_py_withouttext():
    """This returns a specific message."""
    return "Python is cool"


@app.route("/number/<n>", strict_slashes=False)
def disp_num(n):
    """This returns a specific message."""
    try:
        n = int(n)
        return f"{n} is a number"
    except:
        return abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
