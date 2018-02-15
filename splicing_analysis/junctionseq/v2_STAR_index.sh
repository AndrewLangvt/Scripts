mkdir /pylon2/mc3bg6p/al2025/isoform/STAR_analysis/v2_STAR_indices

STAR --runMode genomeGenerate --genomeDir /pylon2/mc3bg6p/al2025/isoform/STAR_analysis/v2_STAR_indices \
--genomeFastaFiles /pylon2/mc3bg6p/al2025/isoform/colLiv2_genome/GCA_001887795.1_colLiv2_genomic.fna \
--sjdbGTFfile /pylon2/mc3bg6p/al2025/isoform/colLiv2_genome/Rockdove_cliv2.gtf \
--sjdbOverhang 124
