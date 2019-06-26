"""Models and database functions for Variant Search Web Application."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#####################################################################
# Model definitions

class Gene(db.Model):
    """Table to hold gene."""

    __tablename__ = "gene"

    gene_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    gene_name = db.Column(db.String(64), nullable=True)
    gene_variant = db.Column(db.String(100), nullable=True) # variants can be long
    

    def __repr__(self):
        """Provide helpful representation when printed."""
        return f"<Gene gene={self.gene_name} variant={self.gene_variant}>"


class Variant(db.Model):
    """Variants and their attributes."""

    __tablename__ = "variants"

    variant_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    variant_name = db.Column(db.String(100), nullable=True) # variants can be long
    nucleotide_change = db.Column(db.String(64), nullable=True)
    protein_change = db.Column(db.String(64), nullable=True)
    other_mappings = db.Column(db.String(64), nullable=True)

    gene_id = db.Column(db.String(1), db.ForeignKey('gender.gender_code'))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<" \
            f"Variant variant_id={self.variant_id} variant_name = {self.variant_gname}>"



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