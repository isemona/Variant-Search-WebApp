import csv
import pandas as pd
import numpy as np

file = 'variants.tsv'
def get_gene_list(file):
    arr = []
    with open(file) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            arr.append(row['Gene'])
    variants = [item for item in arr if item != ''] # duplicates that okay
    print(len(variants))
    genes = set(variants)
    print(len(genes))
    return genes 

# turn file into dictionary gene_dict

0 BRCA2: {variant1: attr1, attr2, variant2: attr1, attr2}

def get_attributes:
    file = 'variants.tsv'
    file_data = pd.read_table(file,sep='\t')
    # file_data.head()
    for data in file_data:
        print(data)

def load_genes():
    file = 'variants.tsv'
    
def get_gene_list(file):
    dict = {}
    with open(file) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        for row in reader:
            if row["Gene"] not in dict:
                dict[row["Gene"]] = (
                    [row['Nucleotide Change'], 
                     row['Protein Change'], 
                     row['Other Mappings'],
                     row['Alias'], 
                     row['Transcripts'], 
                     row['Region']])
                     row['Reported'], 
                     row['Classification'], 
                     row['Inferred Classification'], 
                     row['Source'], 
                     row['Last Evaluated'], 
                     row['Last Updated'], 
                     row['URL'], 
                     row['Submitter Comment'], 
                     row['Assembly'], 
                     row['Chr'], 
                     row['Genomic Start'], 
                     row['Genomic Stop'], 
                     row['Ref'], 
                     row['Alt'], 
                     row['Accession'], 
                     row['Reported Ref'], 
                     row['Reported Alt']])
            
    return dict

        gene = Gene(
                    gene_name = 'BRCA2'
        )
        db.session.add(gene)
        db.session.commit()



def load_variants():

    for key,value in gene_dict.items():
        variants = value
        nucleotide_change = 
        protein_change = 
        other_mappings = 
        alias = 
        transcripts = 
        region = 
        reported_classification = 
        inferred_classification = 
        source = 
        last_evaluated = 
        last_updated = 
        url = 
        submitter_comment = 
        assembly = 
        chrm = 
        genomic_start = 
        genomic_stop = 
        ref = 
        alt = 
        accession = 
        reported_ref = 
        reported_alt = 

    # query for the gene _id save to a variable gene_id
    # gene_id = sql query
    variant = Variant(
                    gene_id = gene_id
                    nucleotide_change = 
                    protein_change = 
                    other_mappings = 
                    alias = 
                    transcripts = 
                    region = 
                    reported_classification = 
                    inferred_classification = 
                    source = 
                    last_evaluated = 
                    last_updated = 
                    url = 
                    submitter_comment = 
                    assembly = 
                    chrm = 
                    genomic_start = 
                    genomic_stop = 
                    ref = 
                    alt = 
                    accession = 
                    reported_ref = 
                    reported_alt = 
        )
        db.session.add(gene)
        db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)
    load_genes()