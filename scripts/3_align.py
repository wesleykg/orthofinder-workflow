'''Usage: align.py <orthogroup_cleaned>'''

# Modules
import os  # Manipulating filenames
from Bio.Align.Applications import MuscleCommandline  # Aligning sequences


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
    unaligned_orthogroup = cmdln_args.get('<orthogroup_cleaned>')
# Run interatively in an iPython console
if in_ipython() is True:
    unaligned_orthogroup = ''

# Record the file size of the cleaned orthogroup file to check if its empty.
# The file may be empty because no genes were found in this orthogroup from
# the list of species given.
file_size = os.path.getsize(unaligned_orthogroup)

# Set the original filename
orthogroup_name = os.path.splitext(unaligned_orthogroup)[0]
orthogroup_name = orthogroup_name.rstrip('_cleaned')

# If the file has sequences, initialize the muscle module, set parameters, and
# run the muscle alignment
if file_size > 0:
    muscle_align = MuscleCommandline(input=unaligned_orthogroup,
                                     out=orthogroup_name + '_aligned.fasta')
    muscle_align()
# If the file has no sequences, Print this warning and write an empty file
# using the same convention as above to prevent downstream scripts from
# breaking
elif file_size == 0:
    with open(orthogroup_name + '_aligned.fasta', 'w') as empty_file:
        print 'No orthogroups found for', orthogroup_name
