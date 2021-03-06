FAA: $(patsubst data/%.FAA, data/%_aligned.fasta, $(wildcard data/*.FAA))

FNA: $(patsubst data/%.FNA, data/%_aligned.fasta, $(wildcard data/*.FNA))

download:
	cd data/ ; python ../scripts/0_download.py wanted_accessions.txt zip
	cd data/ ; find . -mindepth 2 -ipath "*.f?a" -exec mv {} . \;
	cd data/ ; rm -r */

rename:
	bash scripts/4_rename.sh

data/%_filtered.fasta: data/%.FAA data/wanted_species.txt
	cd data/ ; python ../scripts/1_filter.py $(notdir $^)

data/%_filtered.fasta: data/%.FNA data/wanted_species.txt
	cd data/ ; python ../scripts/1_filter.py $(notdir $^)

# data/%_cleaned.fasta: data/%_filtered.fasta
# 	cd data/ ; python ../scripts/2_clean.py $(notdir $^)

data/%_aligned.fasta : data/%_filtered.fasta
	if [ -s $^ ] ; \
	then \
		cd data/ ; muscle -in  $(notdir $^) -out $(notdir $@) ; \
	fi

clean:
	rm -f data/*_filtered.fasta data/*_cleaned.fasta data/*_aligned.fasta \
	data/*_missing.txt

cleanall:
	rm -f data/*.FNA data/*.FAA data/*_filtered.fasta data/*_cleaned.fasta \
	data/*_aligned.fasta data/*_missing.txt

.PHONY: FAA FNA download clean cleanall
.DELETE_ON_ERROR:
#.PRECIOUS: data/%_filtered.fasta data/%_cleaned.fasta
