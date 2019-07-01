import csv


gene_file = 'variants.tsv'

def create_gene_dict(gene_file):
    gene_dict = {}
    with open(gene_file) as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab')
        headers = reader.fieldnames
        for row in reader:
            # if it is not an empty string continue
            if row['Gene']: 
                # initializing each gene to have an array
                if gene_dict.get(row["Gene"]) is None: 
                    gene_dict[row['Gene']] = []
                # alway append a dict comprehension of the attributes except for Gene
                gene_dict[row['Gene']].append({attribute: row[attribute] for attribute in headers if attribute != "Gene" }) 

    return gene_dict

    # refactor with default dict