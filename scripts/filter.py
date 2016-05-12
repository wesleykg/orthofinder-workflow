'''Usage: filter.py <orthogroup> <wanted_species>'''

from docopt import docopt # For command-line arguments
import os # For creating output filename from input
from Bio import SeqIO # For reading orthgroup data

cmdln_args = docopt(__doc__) # Creates a dictionary of command-line arguments

orthogroup_file = cmdln_args.get('<orthogroup>')
wanted_species_file = cmdln_args.get('<wanted_species>')

#Read in the wanted_species_file as a list of lines. Loop through each line, 
#splitting it into 0:ID, 1:Genus_species, 2:#-samples-combined and retain the 
#ID in the list wanted_ids.
wanted_ids = []
with open(wanted_species_file, 'r') as species_file:
    wanted_species = species_file.readlines()
    for line in wanted_species:
        ID = line.split('-')[0]
        wanted_ids.append(ID)

#Loop through each wanted ID and if it matches with an ID in the orthogroup, 
#add that sequence record to the list matching_records
matching_records = []
for record in SeqIO.parse(orthogroup_file, 'fasta'): 
    for ID in wanted_ids: 
        if ID in record.id:
            matching_records.append(record)

#Write matching_records to file using the original filename and appending
#_filtered.fasta to the end
orthogroup_name = os.path.splitext(orthogroup_file)[0]
SeqIO.write(matching_records, orthogroup_name + '_filtered.fasta',
            format = 'fasta')