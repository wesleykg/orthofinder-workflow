'''Usage: download.py <wanted_accessions>'''

from docopt import docopt
from zipfile import ZipFile
from StringIO import StringIO
import requests, re
from requests.auth import HTTPDigestAuth

cmdln_args = docopt(__doc__) # Creates a dictionary of command-line arguments

wanted_accessions = cmdln_args.get('<wanted_accessions>')
file_format = 'zip'

base_url = 'http://iptol-api.iplantcollaborative.org/onekp/v1/'

token = requests.get(base_url + 'login',
                     auth = HTTPDigestAuth('1kp-data', '1kp-rna1'), 
                     allow_redirects = False)

token_pattern = re.compile('[0-9]{13}_[A-z0-9]{16}')

token_1kp = re.search(token_pattern, token.text)
token_1kp = token_1kp.group()

with open(wanted_accessions, 'r') as accessions:
    accessions = accessions.readlines()
    accession_ID_list = []
    for line in accessions:
        line = line.rstrip()
        accession_ID_list.append(line)
    gene_IDs = '+'.join(accession_ID_list)
    
URL = (base_url + 'orthogroups?' + 'accession=' + gene_IDs + '&token='
        + token_1kp + '&format=' + file_format)

orthogroup_file = requests.get(URL)
if orthogroup_file.status_code == requests.codes.ok:
    orthogroup_file = ZipFile(StringIO(orthogroup_file.content))
    orthogroup_file.extractall()
else:
    print URL
    orthogroup_file.raise_for_status()