#!/bin/bash

cd data
mkdir not_needed

for file in $( echo *_aligned.fasta) ; do
	echo Working on $file
    python ../scripts/4_rename.py $file PHYPA_ARATH_pt-gene-accessions.csv
    mv $file not_needed
done
