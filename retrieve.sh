#!/bin/bash

prefix="http://onekp.westgrid.ca/1kp-data/"
middle="/assembly/"
suffix="-SOAPdenovo-Trans-Transrate-stats.tsv.gz"

for i in $( cat wanted_species.txt ); do
	for j in $( awk -F '-' '{print $1}' wanted_species.txt ); do
			echo $prefix$i$middle$j$suffix
		done
	done