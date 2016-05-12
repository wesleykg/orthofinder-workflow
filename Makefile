FAA: $(patsubst data/%.FAA, data/%_aligned.fasta, $(wildcard data/*.FAA))

FNA: $(patsubst data/%.FNA, data/%_aligned.fasta, $(wildcard data/*.FNA))

data/*.FAA: data/wanted_accesions.txt data/1kp_token.txt
	cd data/ ; python ../scripts/download.py $(notdir $^)
	cd data/ ; find . -mindepth 2 -ipath "*.faa" -exec cp {} . \;

data/*.FNA: data/wanted_accesions.txt data/1kp_token.txt
	cd data/ ; python ../scripts/download.py $(notdir $^)
	cd data/ ; find . -mindepth 2 -ipath "*.fna" -exec cp {} . \;

data/%_filtered.fasta: data/%.FAA data/wanted_species
	cd data/ ; python ../scripts/filter.py $(notdir $^)

data/%_filtered.fasta: data/%.FNA data/wanted_species.txt
	cd data/ ; python ../scripts/filter.py $(notdir $^)

data/%_cleaned.fasta: data/%_filtered.fasta
	cd data/ ; python ../scripts/clean.py $(notdir $^)

data/%_aligned.fasta : data/%_cleaned.fasta
	cd data/ ; python ../scripts/align.py $(notdir $^)

clean:
	rm data/*_filtered.fasta data/*_cleaned.fasta data/*_aligned.fasta

cleanall:
	rm data/*.FNA data/*.FAA data/*_filtered.fasta data/*_cleaned.fasta \
	data/*_aligned.fasta

.PHONY: FAA FNA clean cleanall
.DELETE_ON_ERROR:
#.PRECIOUS: data/%_filtered.fasta data/%_cleaned.fasta