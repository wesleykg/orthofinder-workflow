'''Usage: download.py <wanted_accesions> <token_file>'''

from docopt import docopt
from zipfile import ZipFile
from StringIO import StringIO
import requests

cmdln_args = docopt(__doc__) # Creates a dictionary of command-line arguments

wanted_accesions = cmdln_args.get('<wanted_accesions>') #"../data/wanted_gene_ids.txt"
token_file = cmdln_args.get('<token_file>') #'../data/1kp_token.txt'
file_format = 'zip'

base_url = 'http://iptol-api.iplantcollaborative.org/onekp/v1/orthogroups?'

with open(token_file, 'r') as token:
    token_1kp = token.read()

with open(wanted_accesions, 'r') as accesions:
    accessions = accesions.readlines()
    accesion_ID_list = []
    for line in accessions:
        line = line.rstrip()
        accesion_ID_list.append(line)
    seperator = '+'
    gene_IDs = seperator.join(accesion_ID_list)
    
URL = (base_url + 'accession=' + gene_IDs + '&token=' + token_1kp + 
        '&format=' + file_format)

orthogroup_file = requests.get(URL)
if orthogroup_file.status_code == requests.codes.ok:
    orthogroup_file = ZipFile(StringIO(orthogroup_file.content))
    orthogroup_file.extractall()