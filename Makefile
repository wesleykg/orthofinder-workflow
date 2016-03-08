all: $(patsubst %.fna, %_aligned.fasta, $(wildcard *.fna))

clean:
	rm -f *-filtered.fasta

%_filtered.fasta: %.fna wanted_species.txt
	python filter.py $^

%_aligned.fasta : %_filtered.fasta
	python align.py $^
	aliview $@


.PHONY: all clean
.DELETE_ON_ERROR:
.SECONDARY: