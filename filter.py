from Bio import SeqIO

ids_1kp = 'ids_1kp.txt'
orthofinder_data = "At-atpD_orthofinder.fna"

##############################################################################

atpD_index = SeqIO.index(orthofinder_data, "fasta")

##Produce a list of 1kp IDs
wanted_ids = [] #Initialize the list
with open(ids_1kp, 'r') as ids: #Open the file
    wanted_ids_temp = ids.readlines() #Read in the file
    for ID in wanted_ids_temp: 
        wanted_ids.append(ID.rstrip()) #Remove newline characters