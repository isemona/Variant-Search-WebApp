"""Variant Search Web Application"""

from flask import Flask, flash, redirect, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

# need to allow access to database
from model import connect_to_db, db

from query import *

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "willywonka"


@app.route('/')
def index():
    """Main page"""
    
    return render_template("index.html", token="Hello Flask+React")


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    #port 5000 already taken I used 80 instead for this project
    app.run(host="0.0.0.0", port=80)