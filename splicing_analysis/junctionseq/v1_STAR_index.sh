mkdir /pylon2/mc3bg6p/al2025/isoform/STAR_analysis/v1_STAR_indices

STAR --runMode genomeGenerate --genomeDir /pylon2/mc3bg6p/al2025/isoform/STAR_analysis/v1_STAR_indices \
--genomeFastaFiles /pylon2/mc3bg6p/al2025/isoform/genome_compare/GCF_000337935.1_Cliv_1.0_genomic.fna \
--sjdbGTFfile /pylon2/mc3bg6p/al2025/isoform/genome_compare/GCF_000337935.1_Cliv_1.0_genomic.gtf \
--sjdbOverhang 124

sbatch /pylon2/mc3bg6p/al2025/isoform/STAR_analysis/STAR_analysis.job
