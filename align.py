'''Usage: align.py <orthogroup_filtered>'''

import os
from docopt import docopt
from Bio.Align.Applications import MuscleCommandline

cmdln_args = docopt(__doc__) #Creates a dictionary of command-line arguments

unaligned_orthogroup = cmdln_args.get('<orthogroup_filtered>')
orthogroup_name = os.path.splitext(unaligned_orthogroup)[0]
orthogroup_name = orthogroup_name.rstrip('_filtered')

muscle_align = MuscleCommandline(input = unaligned_orthogroup, 
                                 out = orthogroup_name + '_aligned.fasta')
if __name__ == '__main__':
    muscle_align()