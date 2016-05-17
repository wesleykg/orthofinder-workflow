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
auth_token = requests.get(token_url, 
                          auth=HTTPDigestAuth('1kp-data', '1kp-rna1'), 
                            allow_redirects = False)

#Use regex to find the token in the returned message from the server
token_pattern = re.compile('[0-9]{13}_[A-z0-9]{16}')
auth_token = re.search(token_pattern, auth_token.text)
auth_token = auth_token.group() #Method to read the matched regex token

#Open the wanted_accessions file and read in each accession into accession_ids
accession_IDs = []
with open(wanted_accessions, 'r') as accessions:
    accessions_list = accessions.readlines()
    for line in accessions_list:
        line = line.rstrip()
        accession_IDs.append(line)
    gene_IDs = '+'.join(accession_IDs)
    
URL = (orthogroup_url + '?accession=' + gene_IDs + '&token='
        + auth_token + '&format=' + file_format)

orthogroup_file = requests.get(URL)
if orthogroup_file.status_code == requests.codes.ok:
    orthogroup_file = ZipFile(StringIO(orthogroup_file.content))
    orthogroup_file.extractall()
else:
    print URL
    orthogroup_file.raise_for_status()