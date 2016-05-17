'''Usage: align.py <orthogroup_cleaned>'''

import os #For creating filenames and checking for empty files
from docopt import docopt #For command-line arguments
from Bio.Align.Applications import MuscleCommandline #For aligning sequences

cmdln_args = docopt(__doc__) #Creates a dictionary of command-line arguments

unaligned_orthogroup = cmdln_args.get('<orthogroup_cleaned>')
orthogroup_name = os.path.splitext(unaligned_orthogroup)[0]
orthogroup_name = orthogroup_name.rstrip('_cleaned')

#Record the file size of the cleaned orthogroup file to check if its empty
file_size = os.path.getsize(unaligned_orthogroup)

#If the file has sequences, initialize the muscle module, set parameters, and
#run the muscle alignment
if file_size > 0:
    muscle_align = MuscleCommandline(input = unaligned_orthogroup, 
                                     out = orthogroup_name + '_aligned.fasta')
    muscle_align()

#If the file has no sequences, write an empty file using the same convention
#as above to prevent downstream scripts from breaking    
elif file_size == 0:
    with open(orthogroup_name + '_aligned.fasta', 'w') as empty_file:
        print 'No orthogroups found for', orthogroup_name
                                     