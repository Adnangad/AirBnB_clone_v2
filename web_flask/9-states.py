#!/usr/bin/python3
"""
Web app
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states/<id>', strict_slashes=False)
def states_lz(id):
    """display a HTML page with the states listed in alphabetical order"""
    states = storage.all("State")
    if id is not None:
        state_id = 'State.' + id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.route('/states', strict_slashes=False)
def states_list():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
