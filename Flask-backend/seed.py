import csv

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



def load_genes():

    for key,value in gene_dict.items():
        gene_name = key

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