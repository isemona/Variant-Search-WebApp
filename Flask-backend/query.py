import csv


gene_file = 'variants.tsv'

def create_gene_dict(gene_file):
    gene_dict = {}
    with open(gene_file) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        headers = reader.fieldnames
        for row in reader:
            # If it is not an empty string continue.
            if row['Gene']: 
                # Initializing each gene to have an array to store variants.
                if gene_dict.get(row["Gene"]) is None: 
                    gene_dict[row['Gene']] = []
                # Always append a dict-comprehension of the attributes including the Gene column.
                gene_dict[row['Gene']].append({attribute: row[attribute] for attribute in headers}) 

    return gene_dict

    # Refactor with default-dict

