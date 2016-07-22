'''Usage: 4_rename.py <file> <names_file>'''

# Modules
import pandas
import os

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
    from docopt import docopt  # Command-line argument handler
    cmdln_args = docopt(__doc__)
    in_file = cmdln_args.get('<fasta_file>')
    names_file = cmdln_args.get('<names_file>')
# Run interatively in an iPython console
if in_ipython() is True:
    in_file = ''
    names_file = '../kegg_pathway_photosynthesis'

pandas.read_csv()