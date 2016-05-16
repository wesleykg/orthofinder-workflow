'''Usage: align.py <orthogroup_cleaned>'''

import os
from docopt import docopt
from Bio.Align.Applications import MuscleCommandline

cmdln_args = docopt(__doc__) #Creates a dictionary of command-line arguments

unaligned_orthogroup = cmdln_args.get('<orthogroup_cleaned>')
orthogroup_name = os.path.splitext(unaligned_orthogroup)[0]
orthogroup_name = orthogroup_name.rstrip('_cleaned')

file_size = os.path.getsize(unaligned_orthogroup)

if file_size > 0:
    muscle_align = MuscleCommandline(input = unaligned_orthogroup, 
                                     out = orthogroup_name + '_aligned.fasta')
    muscle_align()
    
elif file_size == 0:
    with open(orthogroup_name + '_aligned.fasta', 'w') as empty_file:
        print 'No orthogroups found for', orthogroup_name
                                     