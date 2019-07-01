"""Variant Search Web Application"""

from flask import Flask, flash, redirect, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from flask_restful import Resource, Api
from flask_cors import CORS
# need to allow access to database
# from model import connect_to_db, db

from query import *

app = Flask(__name__)
api = Api(app)
CORS(app)

app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# The Flask-DebugToolbar requires the 'SECRET_KEY' config var to be set
app.secret_key = "gene_machine"

variants = create_gene_dict(gene_file)

class HelloWorld(Resource):
    def get(self):
        return variants

api.add_resource(HelloWorld, '/')


if __name__ == "__main__":
    app.run(debug=True) # Debug mode should never be used in a production environment!
    # connect_to_db(app)

    DebugToolbarExtension(app)

    #port 5000 already taken I used 80 instead for this project
    app.run(host="0.0.0.0", port=80)