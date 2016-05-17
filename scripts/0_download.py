'''Usage: download.py <wanted_accessions>'''

from docopt import docopt #For command-line arguments
from zipfile import ZipFile #For decompressing orthogroup files
from StringIO import StringIO #For reading 
import requests #For downloading orthogroup files
import re #For retrieving the authentication token for downloading files
from requests.auth import HTTPDigestAuth #For authenticating the connection

cmdln_args = docopt(__doc__) # Creates a dictionary of command-line arguments

wanted_accessions = cmdln_args.get('<wanted_accessions>')
file_format = 'zip'

base_url = 'http://iptol-api.iplantcollaborative.org/onekp/v1/'
token_url = base_url + 'login'
orthogroup_url = base_url + 'orthogroups'

#Connect to the server and obtain an authentication token. Setting ridirection
#to false stops Requests from redirecting us to the web GUI page
token = requests.get(token_url, auth = HTTPDigestAuth('1kp-data', '1kp-rna1'),
                     allow_redirects = False)

#Use regex to find the token in the returned message from the server
token_pattern = re.compile('[0-9]{13}_[A-z0-9]{16}')
token_1kp = re.search(token_pattern, token.text)
token_1kp = token_1kp.group() #Method to actually read the matched regex token

#Open the wanted_accessions file and read in each accession into accession_ids
accession_IDs = []
with open(wanted_accessions, 'r') as accessions:
    wanted_accesions = accessions.readlines()
    for line in wanted_accessions:
        line = line.rstrip()
        accession_IDs.append(line)
    gene_IDs = '+'.join(accession_IDs)
    
URL = (base_url + 'orthogroups?' + 'accession=' + gene_IDs + '&token='
        + token_1kp + '&format=' + file_format)

orthogroup_file = requests.get(orthogroup_url)
if orthogroup_file.status_code == requests.codes.ok:
    orthogroup_file = ZipFile(StringIO(orthogroup_file.content))
    orthogroup_file.extractall()
else:
    print URL
    orthogroup_file.raise_for_status()