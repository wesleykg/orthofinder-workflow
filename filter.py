from Bio import SeqIO

atpD_index = SeqIO.index("At-atpD_orthofinder.fna", "fasta")

ids_1kp = open("ids_1kp.txt", 'r')
wanted_species = ids_1kp.readlines()
ids_1kp.close()
