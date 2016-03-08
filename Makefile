all: $(patsubst %.fna, %_aligned.fasta, $(wildcard *.fna))

clean:
	rm -f *_filtered.fasta *_cleaned.fasta *_aligned.fasta

%_filtered.fasta: %.fna wanted_species.txt
	python filter.py $^

%_cleaned.fasta: %_filtered.fasta
	python clean.py $^

%_aligned.fasta : %_cleaned.fasta
	python align.py $^
	nohup aliview $@ > /dev/null 2>&1 &


.PHONY: all clean
.DELETE_ON_ERROR:
.PRECIOUS: %_filtered.fasta %_cleaned.fasta