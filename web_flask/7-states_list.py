#!/usr/bin/python3
"""Importing Flask to run the web app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask("__name__")


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Render state_list html page"""
    states = storage.all()
    return render_template('states_list.html', states=states)


@app.teardown_appcontext()
def teardown(self):
    storage.close()
