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

todos = [{ 
    'BRCA1': {
        'variant_1': {
                'nucleotide_change': 'NM_003159.2:c.-162-?_99+?del',
                'protein_change':'207del',
                'other_mappings':'c.-162-?_99+?del',
                'alias':'NaN',
                'transcripts':'3159.2',
            },
    },
    'BRCA2': {
        'variant_1': {
            'nucleotide_change':'NM_003159.2:c.-162-?_99+?del',
            'protein_change':'p.Cys207del',
            'other_mappings':'NM_003159.2:c.-162-?_99+?del',
            'alias':'NaN',
            'transcripts':'NM_003159.2',
        },
        'variant_2': {
            'nucleotide_change':'NM_003159.2:',
            'protein_change':'p.Cys2',
            'other_mappings':'NM_003159.2:',
            'alias':'NaN',
            'transcripts':'NM_00',
        }

    }
}]


# @app.route('/')
# def index():
#     """Main page"""
    
#     return render_template("index.html", token="Hello Flask+React")

# contacts = [
#       {
#         "id": 1,
#         "name": "Leanne Graham",
#         "username": "Bret",
#         "email": "Sincere@april.biz",
#         "address": {
#           "street": "Kulas Light",
#           "suite": "Apt. 556",
#           "city": "Gwenborough",
#           "zipcode": "92998-3874",
#           "geo": {
#             "lat": "-37.3159",
#             "lng": "81.1496"
#           }
#         },
#         "phone": "1-770-736-8031 x56442",
#         "website": "hildegard.org",
#         "company": {
#           "name": "Romaguera-Crona",
#           "catchPhrase": "Multi-layered client-server neural-net",
#           "bs": "harness real-time e-markets"
#         }
#       }
#     ]

# class TodoSimple(Resource):
#     def get(self):
        
#         return {'task': 'Hello world'}

    # def put(self, todo_id):
    #     todos[todo_id] = request.form['data']
    #     return {todo_id: todos[todo_id]}
# api.add_resource(TodoSimple)

class HelloWorld(Resource):
    def get(self):
        return todos

api.add_resource(HelloWorld, '/index.html')


if __name__ == "__main__":
    app.debug = True # Debug mode should never be used in a production environment!
    # connect_to_db(app)

    DebugToolbarExtension(app)

    #port 5000 already taken I used 80 instead for this project
    app.run(host="0.0.0.0", port=80)