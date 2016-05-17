'''Usage: filter.py <orthogroup> <wanted_species>'''

from docopt import docopt # or command-line arguments
import os #For creating output filename from input
from Bio import SeqIO #For reading orthgroup data

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
#add that sequence record to the list matching_records.
matching_records = []
matching_record_ids = []
for record in SeqIO.parse(orthogroup_file, 'fasta'): 
    for ID in wanted_ids: 
        if ID in record.id:
            matching_records.append(record)
            #Record the ID of matched species in a sperate list for checking
            #missed species later.
            record_id = record.id
            record_id = ID.split('-')[0]
            matching_record_ids.append(record_id)

#Check if any IDs in the wanted_ids list did not have a sequence found for
#this gene and if so, add them to the list missing_records. Join 
#missing_records together in a string for writing to file.
missing_records = []
for ID in wanted_ids:
    if ID not in matching_record_ids:
        missing_records.append(ID)
missing_records = '\n'.join(missing_records)

#Write matching_records to file using the original filename and appending
#_filtered.fasta to the end.
orthogroup_name = os.path.splitext(orthogroup_file)[0]
SeqIO.write(matching_records, orthogroup_name + '_filtered.fasta',
            format = 'fasta')
#Write missing_records to file using the original filename and appending
#_missing.txt to the end.
with open(orthogroup_name + '_missing.txt', 'w') as missing_file:
    missing_file.write(missing_records)