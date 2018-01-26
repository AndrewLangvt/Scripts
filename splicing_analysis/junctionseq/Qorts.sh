cd /pylon2/mc3bg6p/al2025/isoform/JunctionSeq_analysis


star_loc=/pylon2/mc3bg6p/al2025/isoform/STAR_analysis/STAR_mappings

for i in $(ls $star_loc/*_STAR2_Aligned.sortedByCoord.out.bam); do

        SAMPLE=$(basename -s _STAR2_Aligned.sortedByCoord.out.bam $i)
        echo ""
        echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        echo Qorts analysis on $SAMPLE
        echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        echo ""

        java -jar /pylon2/mc3bg6p/al2025/storage/QoRTs.jar QC \
        --stranded \
        --rawfastq /pylon2/mc3bg6p/al2025/stress_study/cor_reads/$SAMPLE.R1.cor.fq.gz,/pylon2/mc3bg6p/al2025/stress_study/cor_reads/$SAMPLE.R2.cor.fq.gz \
        /pylon2/mc3bg6p/al2025/isoform/STAR_analysis/STAR_mappings/${SAMPLE}_STAR2_Aligned.sortedByCoord.out.bam \
        /pylon2/mc3bg6p/al2025/isoform/genome_compare/GCF_000337935.1_Cliv_1.0_genomic.gtf \
        /pylon2/mc3bg6p/al2025/isoform/JunctionSeq_analysis/qorts_files/rawCts/$SAMPLE 
done

