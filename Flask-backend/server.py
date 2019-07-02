"""Variant Search Web Application"""

from flask import Flask, flash, redirect, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
 

# from model import connect_to_db, db

from query import gene_file, create_gene_dict

app = Flask(__name__)
api = Api(app)
CORS(app)

# The Flask-DebugToolbar requires the 'SECRET_KEY' config var to be set
app.secret_key = "gene_machine"

variants = create_gene_dict(gene_file)

class Genes(Resource):
    def get(self, gene_id):
        gene_list = list(variants)
        gene = [gene for gene in gene_list if gene_id in gene]
        return gene

# Handles the route, explicitly tells Flask we are requesting gene_id
api.add_resource(Genes, '/genes/<string:gene_id>') 

class Variants(Resource):
    def get(self, var_id):
        return variants[var_id]

api.add_resource(Variants, '/variants/<string:var_id>') 


if __name__ == "__main__":
    app.run(debug=True) # Debug mode should never be used in a production environment!
    
    # connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")