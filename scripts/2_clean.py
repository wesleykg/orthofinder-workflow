'''Usage: 2_clean.py <orthogroup_filtered>'''

# Modules
import os  # Manipulating filenames
from Bio import SeqIO  # Reading orthogroup sequences
from Bio.SeqUtils.CheckSum import seguid  # Identifying unique sequences


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
    uncleaned_orthogroup = cmdln_args.get('<orthogroup_filtered>')
# Run interatively in an iPython console
if in_ipython() is True:
    uncleaned_orthogroup = ''

# Create an ID for each record based on the sequence. All records with unique
# IDs, and therefore unique sequences, are saved to unique_records. Duplicate
# sequences should not be added.
unique_records = []
checksum_container = []
for record in SeqIO.parse(uncleaned_orthogroup, 'fasta'):
    checksum = seguid(record.seq)
    if checksum not in checksum_container:
        checksum_container.append(checksum)
        unique_records.append(record)

# Write unique_records to file using the original filename and appending
# _cleaned.fasta to the end.
orthogroup_name = os.path.splitext(uncleaned_orthogroup)[0]
orthogroup_name = orthogroup_name.rpartition('_')[0]
SeqIO.write(unique_records, orthogroup_name + '_cleaned.fasta', format='fasta')
