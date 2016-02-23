from Bio import SeqIO

ids_1kp = 'ids_1kp.txt'
orthofinder_data = "At-atpD_orthofinder.fna"

##############################################################################

##Produce a list of 1kp IDs
wanted_ids = [] #Initialize the list
with open(ids_1kp, 'r') as ids: #Open the file
    wanted_ids_temp = ids.readlines() #Read in the file
    for ID in wanted_ids_temp: 
        wanted_ids.append(ID.rstrip()) #Remove newline characters

##Loop through orthofinder data and retrieve records that match wanted_ids

for record in SeqIO.parse(orthofinder_data, 'fasta'):
    for ID in wanted_ids:
        if ID in record.id:
            print record.id
            


