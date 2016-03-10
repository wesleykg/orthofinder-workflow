#!/bin/bash

echo "Hello world"
#Read ids, using awk, from wanted_species.txt
#Match an ID to the species
#Use paste to create ID-Genus_species/assembly/ID
#Use paste to combine:
#	1. url-prefix.txt 
#	2. ID-Genus_species/assembly/ID
#	3. url-suffix.txt
#Read combined file with wget -i