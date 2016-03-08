all: $(patsubst %.fna, %_aligned.fasta, $(wildcard *.fna))

clean:
	rm -f *_filtered.fasta *_aligned.fasta

%_filtered.fasta: %.fna wanted_species.txt
	python filter.py $^

%_aligned.fasta : %_filtered.fasta
	python align.py $^
	nohup aliview $@ > /dev/null 2>&1 &


.PHONY: all clean
.DELETE_ON_ERROR:
.SECONDARY: