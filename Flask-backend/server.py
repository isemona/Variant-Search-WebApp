"""Variant Search Web Application"""

from flask import Flask, flash, redirect, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from flask_restful import Resource, Api
# need to allow access to database
# from model import connect_to_db, db

from query import *

app = Flask(__name__)
api = Api(app)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# The Flask-DebugToolbar requires the 'SECRET_KEY' config var to be set
app.secret_key = "gene"

# todos = { 
#     'BRCA1': {
#         'variant_1': {
#                 'nucleotide_change': 'NM_003159.2:c.-162-?_99+?del',
#                 'protein_change':'207del',
#                 'other_mappings':'c.-162-?_99+?del',
#                 'alias':'NaN',
#                 'transcripts':'3159.2',
#             },
#     },
#     'BRCA2': {
#         'variant_1': {
#             'nucleotide_change':'NM_003159.2:c.-162-?_99+?del',
#             'protein_change':'p.Cys207del',
#             'other_mappings':'NM_003159.2:c.-162-?_99+?del',
#             'alias':'NaN',
#             'transcripts':'NM_003159.2',
#         },
#         'variant_2': {
#             'nucleotide_change':'NM_003159.2:',
#             'protein_change':'p.Cys2',
#             'other_mappings':'NM_003159.2:',
#             'alias':'NaN',
#             'transcripts':'NM_00',
#         },

#     },
# };

# @app.route('/')
# def index():
#     """Main page"""
    
#     return render_template("index.html", token="Hello Flask+React")

# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}

#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}

# api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == "__main__":
    app.debug = True # Debug mode should never be used in a production environment!
    # connect_to_db(app)

    DebugToolbarExtension(app)

    #port 5000 already taken I used 80 instead for this project
    app.run(host="0.0.0.0", port=80)