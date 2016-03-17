
prefix = "http://onekp.westgrid.ca/1kp-data/"
middle = "/assembly/"
suffix = "-SOAPdenovo-Trans-Transrate-stats.tsv.gz"

wanted_species_file = "wanted_species.txt"
out_URL_list = "wanted_TRS_URLs.txt"

URL_list = []

with open(wanted_species_file, 'r') as species_file:
    for line in species_file:
        ID = line.split('-')[0]
        URL = prefix + line.rstrip() + middle + ID + suffix
        URL_list.append(URL)

with open(out_URL_list, "w") as URLs_out:
	for URL in URL_list:
		URLs_out.write(URL + '\n')