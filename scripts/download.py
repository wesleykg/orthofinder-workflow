
wanted_gene_ids = "../data/wanted_gene_ids.txt"
token_file = '../data/1kp_token.txt'
seperator = '+'


prefix = '''http://iptol-api.iplantcollaborative.org/
            onekp/v1/orthogroups?accession='''

with open(token_file, 'r') as token:
    token_1kp = token.read()

with open(wanted_gene_ids, 'r') as gene_ids:
    accessions = gene_ids.readlines()
    for line in accessions:
        line = line.rstrip()
        print line
    accession_url = seperator.join(accessions)
    print accession_url