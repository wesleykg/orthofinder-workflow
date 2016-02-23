from Bio import SeqIO
#from Bio.SeqRecord import SeqRecord

ids_1kp = 'ids_1kp.txt'
orthofinder_file = "At-atpD_orthofinder.fna"

##############################################################################

##Produce a list of 1kp IDs
wanted_ids = [] #Initialize the list
with open(ids_1kp, 'r') as ids: #Open the file
    wanted_ids_temp = ids.readlines() #Read in the file
    for ID in wanted_ids_temp: 
        wanted_ids.append(ID.rstrip()) #Remove newline characters

##Loop through orthofinder data and retrieve records that match wanted_ids
orthofinder_data = SeqIO.parse(orthofinder_file, 'fasta')
wanted_records = []
for record in orthofinder_data:
    for ID in wanted_ids:
        if ID in record.id:
            wanted_records.append(record)

SeqIO.write(wanted_records, 'filtered_orthofinder.fasta', 'fasta')

