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


def load_genes():


    gene = Gene(
                    gene_name = 'BRCA2'
        )
        db.session.add(gene)
        db.session.commit()

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

    {
        "Gene" = {
            "BRCA" : [{
                "nucleotide_change":


            }]
        }
    }

if __name__ == "__main__":
    connect_to_db(app)
    load_genes()