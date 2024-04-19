#!/usr/bin/python3
from flask import Flask
"""This module displays a message on the webpage"""

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def disp():
  return "Hello HBNB!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
