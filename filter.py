'''Usage: filter.py <orthogroup> <wanted_species>'''

from docopt import docopt #For command-line arguments
import os #For creating output filename from input
from Bio import SeqIO #For reading orthgroup data

cmdln_args = docopt(__doc__) #Creates a dictionary of command-line arguments

orthogroup_file = cmdln_args.get('<orthogroup>')    #The file produced 
                                                    #by orthofinder
ids_1kp_file = cmdln_args.get('<wanted_species>')   #The file containing 
                                                    #wanted 1kp IDs

orthogroup_name = os.path.splitext(orthogroup_file)[0] #Drop the filename

def filter_by_id(orthgroup_file, ids_1kp_file):
    '''Filter out transcripts in orthgroup data by species ID'''
    
    ##Read in list of 1kp IDs of wanted species
    wanted_ids = [] #Initialize list of IDs
    
    with open(ids_1kp_file, 'r') as ids: #Open the file for reading
        wanted_ids_temp = ids.readlines() #Read in the file with newline chars
        for ID in wanted_ids_temp: #Loops through each ID
            wanted_ids.append(ID.rstrip()) #Remove newline chars
    
    ##Retrieve records in orthgroup of wanted species only
    matching_records = [] #Initialize list of records
    
    for record in SeqIO.parse(orthogroup_file, 'fasta'): #Open the file
        for ID in wanted_ids: #Loop through each wanted species ID
            if ID in record.id: #The '.id' method returns the names of records
                matching_records.append(record) #Add record to list
    
    SeqIO.write(matching_records, 
                orthogroup_name + '_filtered.fasta', 
                'fasta')
      
if __name__ == '__main__':
    filter_by_id(orthogroup_file, ids_1kp_file)