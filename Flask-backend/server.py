"""Variant Search Web Application"""

from flask import Flask, flash, redirect, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

# from model import connect_to_db, db

from query import *

app = Flask(__name__)
api = Api(app)
CORS(app)

# The Flask-DebugToolbar requires the 'SECRET_KEY' config var to be set
app.secret_key = "gene_machine"

variants = create_gene_dict(gene_file)

class HelloWorld(Resource):
    def get(self):
        # no need to say jsonify as flask_restful takes care of this
        return variants

api.add_resource(HelloWorld, '/')

class Genes(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gene', type=str, location='form')
        args = parser.parse_args()
        return variants[args['gene']]


api.add_resource(Genes, '/search')


if __name__ == "__main__":
    app.run(debug=True) # Debug mode should never be used in a production environment!
    
    # connect_to_db(app)

    DebugToolbarExtension(app)

    #port 5000 already taken I used 80 instead for this project
    app.run(host="0.0.0.0", port=80)