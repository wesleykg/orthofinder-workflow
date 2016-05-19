'''Usage: download.py <wanted_accessions> <format>'''

# Modules
import requests  # Downloading the authentication token and orthogroup files
from requests.auth import HTTPDigestAuth  # Authenticate the connection
import re  # Retrieving the authentication token for downloading files
from zipfile import ZipFile  # Decompressing orthogroup files
from StringIO import StringIO  # Reading the compressed assembly


# Check if running interactively in an iPython console, or in a script
# from the command-line
def in_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False
# Run in a script from the command-line
if in_ipython() is False:
    from docopt import docopt  # Command-line arguments handler
    cmdln_args = docopt(__doc__)
    wanted_accessions = cmdln_args.get('<wanted_accessions>')
    file_format = cmdln_args.get('<format>')
# Run interatively in an iPython console
if in_ipython() is True:
    wanted_accessions = '../data/wanted_accessions.txt'
    file_format = 'zip'

# Location of web API
base_url = 'http://iptol-api.iplantcollaborative.org/onekp/v1/'

# Connect to the server and obtain an authentication token. Setting
# allow_redirects to false stops Requests from redirecting us to
# the web GUI page.
auth_token = requests.get(base_url + 'login',
                          auth=HTTPDigestAuth('1kp-data', '1kp-rna1'),
                          allow_redirects=False)
# Check if the token was retrieved properly, and if not, give the status code
# providing the reason for failure.
if 'Successfully logged in with token' in auth_token.text:
    # Use regular expressions to find the token in the returned message from
    # the server. The search() method finds the pattern and stores it in
    # auth_token. The group() method returns the match to the previously
    # completed search(). Example token: 1463695387322_wsMwZ5o5EmmC1Oan
    token_pattern = re.compile('[0-9]{13}_[A-z0-9]{16}')
    auth_token = re.search(token_pattern, auth_token.text)
    auth_token = auth_token.group()
else:
    auth_token.raise_for_status()

# Open the wanted_accessions file and read in each accession, stripping newline
# characters, and adding each accesion into the list accession_ids
accession_IDs = []
with open(wanted_accessions, 'r') as accessions:
    accessions_list = accessions.readlines()
    for line in accessions_list:
        line = line.rstrip()
        accession_IDs.append(line)
# Join each accession id into a string seperated by '+' characters for URL
# construction below
gene_IDs = '+'.join(accession_IDs)

# Construct the URL with wanted accessions, Example URL:
# http://iptol-api.iplantcollaborative.org/onekp/v1/orthogroups?
# accession=AT4G04640+AT1G15700+AT4G09650+AT2G07707+AT4G32260
# &token=1463695387322_wsMwZ5o5EmmC1Oan
# &format=zip
wanted_url = (base_url + 'orthogroups?' + 'accession=' + gene_IDs + '&token=' +
              auth_token + '&format=' + file_format)

# Retrieve the wanted orthogroups and if an ok status code is given by the
# server, extract the zipped archive. If a bad status code is given by the
# server, print the attempted URL and the bad status code.
orthogroup_file = requests.get(wanted_url,
                               auth=HTTPDigestAuth('1kp-data', '1kp-rna1'))
if orthogroup_file.status_code == requests.codes.ok:
    #  print 'Success using this URL:', orthogroup_file.url
    orthogroup_file = ZipFile(StringIO(orthogroup_file.content))
    orthogroup_file.extractall()
else:
    orthogroup_file.raise_for_status()
    print 'Error using this URL:', orthogroup_file.url
