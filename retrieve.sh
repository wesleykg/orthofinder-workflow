#!/bin/bash

prefix="http://onekp.westgrid.ca/1kp-data/"
fullName=$(cat wanted_species.txt)
assembly="/assembly/"
ID=$(awk -F '-' '{print $1}' wanted_species.txt)
suffix="-SOAPdenovo-Trans-Transrate-stats.tsv.gz"

# Need to use a loop instead to construct URL
URL=$prefix$fullName$assembly$ID$suffix
echo $URL
