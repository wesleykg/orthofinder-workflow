##Align unique records using Muscle
from Bio.Align.Applications import MuscleCommandline

muscle_align = MuscleCommandline(input = 'filtered_orthofinder.fasta', out = 'orthofinder_aligned.fasta')
muscle_align()