## Load packages
suppressPackageStartupMessages(library(dplyr))
suppressPackageStartupMessages(library(Biostrings))

orthogroup <- readDNAStringSet(filepath = "AT4G09650_4729.FNA", 
                               format = "fasta")

species_names <- names(orthogroup)

wanted_species <- read.table(file = "ids_1kp.txt", sep = "\n", stringsAsFactors = FALSE) %>% unlist
