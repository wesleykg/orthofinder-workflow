FAA: $(patsubst %.FAA, %_aligned.fasta, $(wildcard data/*.FAA))

FNA: $(patsubst %.FNA, %_aligned.fasta, $(wildcard data/*.FNA))

clean:
	rm -f data/*_filtered.fasta data/*_cleaned.fasta data/*_aligned.fasta

data/%_filtered.fasta: data/%.FAA data/wanted_species.txt
	python scripts/filter.py $^

data/%_filtered.fasta: data/%.FNA data/wanted_species.txt
	python scripts/filter.py $^

data/%_cleaned.fasta: data/%_filtered.fasta
	python scripts/clean.py $^

data/%_aligned.fasta : data/%_cleaned.fasta
	python scripts/align.py $^
#	nohup aliview $@ > /dev/null 2>&1 &


.PHONY: FAA FNA clean
.DELETE_ON_ERROR:
#.PRECIOUS: data/%_filtered.fasta data/%_cleaned.fasta