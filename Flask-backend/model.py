"""Models and database functions for Variant Search Web Application."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#####################################################################
# Model definitions

class Gene(db.Model):
    """Table to hold gene."""

    __tablename__ = "gene"

    gene_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    gene_name = db.Column(db.Varchar(10), nullable=True) # nullable as it is not req, varchar?
    
    
    def __repr__(self):
        """Provide helpful representation when printed."""
        return f"<Gene gene={self.gene_name} variant={self.gene_variant}>"


class Variant(db.Model):
    """Variants and their attributes."""

    __tablename__ = "variants"

    variant_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    gene_id = db.Column(db.Varchar(10), db.ForeignKey('gene.gene_id'))
    nucleotide_change = db.Column(db.Varchar(200), nullable=True) # combination of numbers, letters, and symbols _,(),+-  //or we can just evaluate this as a string
    protein_change = db.Column(db.Varchar(200), nullable=True)
    other_mappings = db.Column(db.Varchar(200), nullable=True)
    alias = db.Column(db.Varchar(200), nullable=True) # combination of numbers, letters, and symbols _,(),+-
    transcripts = db.Column(db.Varchar(200), nullable=True) # combination of numbers, letters, and symbols _,(),+-
    region = db.Column(db.Varchar(200), nullable=True) # combination of numbers, letters, and symbols _,(),+-
    reported_classification = db.Column(db.String(20), nullable=True) # pathogenic, likely benign, etc.
    inferred_classification = db.Column(db.String(20), nullable=True)
    source = db.Column(db.String(20), nullable=True) # Clinvar
    last_evaluated = db.Column(db.String(20), nullable=True) # dates can be a string, are dates 20 string chars long?
    last-updated = db.Column(db.String(20), nullable=True)
    url = db.Column(db.Varchar(200), nullable=True) # url can be long
    submitter_comment = db.Column(db.Varchar(200), nullable=True) # submitter can write a lot
    assembly = db.Column(db.Varchar(10), nullable=True) # looks like gene_id
    chrm = db.Column(db.String(48), nullable=True) # a person can have 48 chromosomes
    genomic_start = db.Column(db.Numeric(20), nullable=True) # numbers only
    genomic_stop = db.Column(db.Numeric(20), nullable=True)
    ref = db.Column(db.Varchar(200), nullable=True) # this column is mainly NaN, or -, not sure if 200 is appropriate here
    alt = db.Column(db.Varchar(200), nullable=True) # this column is mainly NaN, or -, not sure if 200 is appropriate here
    accession = db.Column(db.Varchar(200), nullable=True) # combination of numbers, letters, and symbols _,(),+-
    reported_ref = db.Column(db.Varchar(200), nullable=True) # this column is mainly NaN, or -, not sure if 200 is appropriate here
    reported_alt = db.Column(db.Varchar(200), nullable=True) # this column is mainly NaN, or -, not sure if 200 is appropriate here


    gene = db.relationship("Gene", backref="variant")

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