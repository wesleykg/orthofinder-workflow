'''Usage: download.py <wanted_accessions> <token_file>'''

#from docopt import docopt
from zipfile import ZipFile
from StringIO import StringIO
import requests
from requests.auth import HTTPDigestAuth

#cmdln_args = docopt(__doc__) # Creates a dictionary of command-line arguments

wanted_accessions = '../data/wanted_accessions.txt' # cmdln_args.get('<wanted_accessions>')
token_file = '../data/1kp_token.txt' # cmdln_args.get('<token_file>')
file_format = 'zip'

base_url = 'http://iptol-api.iplantcollaborative.org/onekp/v1/login'

with open(token_file, 'r') as token:
    token_1kp = token.read()

token = requests.get(base_url, auth=HTTPDigestAuth('1kp-data', '1kp-rna1'))

print token.text

with open(wanted_accessions, 'r') as accessions:
    accessions = accessions.readlines()
    accession_ID_list = []
    for line in accessions:
        line = line.rstrip()
        accession_ID_list.append(line)
    seperator = '+'
    gene_IDs = seperator.join(accession_ID_list)
    
URL = (base_url + 'orthogroups?' + 'accession=' + gene_IDs + '&token='
        + token_1kp + '&format=' + file_format)

orthogroup_file = requests.get(URL)
if orthogroup_file.status_code == requests.codes.ok:
    orthogroup_file = ZipFile(StringIO(orthogroup_file.content))
    orthogroup_file.extractall()
else:
    orthogroup_file.raise_for_status()