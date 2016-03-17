'''Usage: clean.py <orthogroup_filtered> <TRS_file>'''

from docopt import docopt #For command-line arguments
import os #For creating output filename from input
from Bio import SeqIO #For reading orthgroup data
from Bio.SeqUtils.CheckSum import seguid #For identifying unique sequences

cmdln_args = docopt(__doc__) #Creates a dictionary of command-line arguments

uncleaned_orthogroup = cmdln_args.get('<orthogroup_filtered>')
transrate_stats_file = cmdln_args.get('<TRS_file>')



def duplicate_remover(uncleaned_orthogroup):
    '''Return a list of orthogroup genes without duplicate sequences'''
    global unique_records
    unique_records = [] #Initialize list of unique records
    checksum_container = [] #Initialize list of unique 
                            #identifiers for each gene
    for record in SeqIO.parse(uncleaned_orthogroup, 'fasta'):
        checksum = seguid(record.seq) #Create a unique identifier for only
                                      #the sequence of the record
        if checksum not in checksum_container: #Duplicate seqeunce can't pass
            checksum_container.append(checksum) #Add unique identifier to list
            unique_records.append(record) #Add record to list
    
    return unique_records

orthogroup_name = os.path.splitext(uncleaned_orthogroup)[0]
orthogroup_name = orthogroup_name.rstrip('_filtered')

SeqIO.write(unique_records, orthogroup_name + '_cleaned.fasta', 
                'fasta')

if __name__ == '__main__':
    duplicate_remover(uncleaned_orthogroup)