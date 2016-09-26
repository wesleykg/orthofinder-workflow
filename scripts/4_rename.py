'''Usage: 4_rename.py <fasta_alignment> <accessions_file>'''

# Modules
import pandas
import os
from Bio import SeqIO


# Check if running interactively in an iPython console, or in a script
# from the command-line
def in_ipython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False
# Run in a script from the command-line
if in_ipython() is False:
    from docopt import docopt  # Command-line argument handler
    cmdln_args = docopt(__doc__)
    in_alignment = cmdln_args.get('<fasta_alignment>')
    accessions_file = cmdln_args.get('<accessions_file>')
# Run interatively in an iPython console
if in_ipython() is True:
    in_alignment = '../data/ATCG00540_10485_aligned.fasta'
    accessions_file = '../data/PHYPA_ARATH_pt-gene-accessions.tsv'

alignment = SeqIO.parse(in_alignment, format='fasta')

table_header = 'gene', 'accession'

gene_accessions = pandas.read_csv(accessions_file, sep=',', names=table_header)

alignment_filename = os.path.split(in_alignment)[1]
alignment_file_accession_name = alignment_filename.partition('_')[0]
alignment_file_tail_name = alignment_filename.partition('_')[2]

fasta_file_gene_name = \
    gene_accessions[gene_accessions.accession == alignment_file_accession_name]
fasta_file_gene_name = fasta_file_gene_name.iloc[0]['gene']

fasta_file_outname = fasta_file_gene_name + '_' + alignment_file_tail_name

SeqIO.write(alignment, handle=fasta_file_outname, format='fasta')
