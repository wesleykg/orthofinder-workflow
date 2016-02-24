all: $(patsubst %.fna, %-aligned.fasta, $(wildcard *.fna))

clean:
	rm -f *-filtered.fasta

%-filtered.fasta: %.fna wanted_species.txt
	python filter.py $^

%-aligned.fasta : %-filtered.fasta
	python align.py $^

.PHONY: all clean
.DELETE_ON_ERROR:
.SECONDARY: