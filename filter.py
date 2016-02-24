from Bio import SeqIO
from Bio.SeqUtils.CheckSum import seguid

ids_1kp = 'ids_1kp.txt'
orthofinder_file = "At-atpD_orthofinder.fna"

##############################################################################

def filter(ids_1kp, orthofinder_file):
    ##Produce a list of 1kp IDs
    wanted_ids = [] #Initialize the list
    with open(ids_1kp, 'r') as ids: #Open the file
        wanted_ids_temp = ids.readlines() #Read in the file
        for ID in wanted_ids_temp: 
            wanted_ids.append(ID.rstrip()) #Remove newline characters
    
    ##Loop through orthofinder data and retrieve records that match wanted_ids
    matching_records = []
    for record in SeqIO.parse(orthofinder_file, 'fasta'):
        for ID in wanted_ids:
            if ID in record.id:
                matching_records.append(record)
    
    ##Loop through wanted records and create a list containing unique sequence
    unique_records = []
    checksum_container = []
    for record in matching_records:
        checksum = seguid(record.seq)
        if checksum not in checksum_container:
            checksum_container.append(checksum)
            unique_records.append(record)
    
    ##Write filtered records to file
    return SeqIO.write(unique_records, 'filtered_orthofinder.fasta', 'fasta')

