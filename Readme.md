###Description of workflow

0. Download orthogroups based on gene accessions listed in wanted_accessions.txt
1. Filter out genes based on species listed in wanted_species.txt
2. Clean out duplicate sequences and low-scoring scaffolds
3. Align the sequences using MUSCLE

###How to use

In a terminal, type `make download` to download OrthoMCL groupings of wanted 
orthogroups from [here](http://iptol-api.iplantcollaborative.org/onekp/v1) and 
place them in the `data/` directory. Data files may also be manually placed in 
the `data/` directory. After data files are added to `data/` the program may be 
run using `make FNA` or `make FAA` if you have DNA or AA data.