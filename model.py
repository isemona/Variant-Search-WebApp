"""Models and database functions for Variant Search Web Application."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


#####################################################################
# Model definitions


#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sugarcoins'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)

    db.create_all()

    print("Connected to DB.")