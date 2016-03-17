#!/bin/bash

wget --user=1kp-data --password=1kp-rna1 -i wanted_TRS_URLs.txt
gzip -d *.gz