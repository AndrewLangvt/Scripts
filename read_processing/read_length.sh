# This script generates a list of all sample datasets in Col1 and longest read lengths in Col2
# Some data was sequenced at NYGC (150PE) and some at NOVOGene (125PE), this script identifies
# any reads that are not trimmed to 125 bp. 

for i in $(ls /pylon2/mc3bg6p/al2025/parental_study/trim_cor_reads/*R1*); do
	F=$(basename -s .R1.fq.gz $i)
	echo $F	`zcat $i | awk 'NR%4 == 2 {lengths[length($0)]++} END {for (l in lengths) {print l}}' | tail -n1` >> /pylon2/mc3bg6p/al2025/parental_study/read_length.tsv
done
