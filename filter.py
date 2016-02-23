from Bio import SeqIO

def name_trunc(record):
    ID = record.id.split()
    return ID
    
atpD_index = SeqIO.index("At-atpD_orthofinder.fna", "fasta")

atpD_index.name()

ids_1kp = open("ids_1kp.txt", 'r')
wanted_species = ids_1kp.readlines()
ids_1kp.close()

#for id in atpD_index:
    