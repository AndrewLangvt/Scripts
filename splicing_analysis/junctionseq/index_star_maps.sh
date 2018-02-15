for i in $(ls /pylon2/mc3bg6p/al2025/isoform/STAR_analysis/STAR_mappings/*STAR2*bam); do
	samtools index -b $i
done
