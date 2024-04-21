#!/usr/bin/python3
"""This module creates a web app"""
from flask import render_template, Flask
from models import storage
from models.state import State


app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def ls():
    """Shows the contents"""
    states = storage.all(State).values()
    al = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", al = al)


@app.teardown_appcontext
def cls(exception):
    """Removes current sql session"""
    return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
