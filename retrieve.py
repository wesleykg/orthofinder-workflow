
prefix = "http://onekp.westgrid.ca/1kp-data/"
middle = "/assembly/"
suffix = "-SOAPdenovo-Trans-Transrate-stats.tsv.gz"

wanted_species_file = "wanted_species.txt"

URL_list = []

with open(wanted_species_file, 'r') as species_file:
    for line in species_file:
        ID = line.split('-')[0]
        URL = prefix + line + middle + ID + suffix
        URL_list.append(URL)

