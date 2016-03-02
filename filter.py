from docopt import docopt #For command-line arguments
from os import path #For creating output filename from input
from Bio import SeqIO #For reading orthgroup data
from Bio.SeqUtils.CheckSum import seguid #For identifying unique sequences

ids_1kp_file = 'wanted_species.txt' #The file containing wanted 1kp IDs
orthogroup_file = "AT4G09650_4729.fna" # The file produced by orthofinder

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
        for ID in wanted_ids: #Loop through each species ID
            if ID in record.id: #The '.id' returns the names of records
                matching_records.append(record) #Add record to list
    
    return matching_records
    
def duplicate_remover(matching_records):
    '''Return a list of orthogroup genes without duplicate sequences'''
    unique_records = [] #Initialize list of unique records
    checksum_container = [] #Initialize list of unique 
                            #identifiers for each gene
    for record in matching_records: #Loop through each record
        checksum = seguid(record.seq) #Create a unique identifier for only
                                      #the sequence of the record
        if checksum not in checksum_container: #Duplicate seqeunce can't pass
            checksum_container.append(checksum) #Add unique identifier to list
            unique_records.append(record) #Add record to list
    
    return unique_records

def file_writer(unique_records):
    '''Write records to file'''
    SeqIO.write(unique_records, 'filtered_orthofinder.fasta', 'fasta')

if __name__ == '__main__':
    filter_by_id(orthogroup_file, ids_1kp_file)