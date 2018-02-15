LOOK_LOC=$1

for i in $(ls $LOOK_LOC/*.TRIM.R1.fq.gz); do

        READ=$(basename -s .TRIM.R1.fq.gz $i)
        STAR_OUT=${READ}_STAR_

        echo ""
        echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        echo First round of mapping for $READ
        echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        echo ""

        STAR --runMode alignReads \
        --genomeDir /pylon2/mc3bg6p/al2025/isoform/STAR_analysis/v2_STAR_indices \
        --readFilesIn $LOOK_LOC/$READ.TRIM.R1.fq.gz \
        $LOOK_LOC/$READ.TRIM.R2.fq.gz \
        --sjdbGTFfile /pylon2/mc3bg6p/al2025/isoform/colLiv2_genome/Rockdove_cliv2.gtf \
        --sjdbOverhang 124 \
        --outFilterScoreMinOverLread 0 \
        --outFilterMatchNminOverLread 0 \
        --outFilterMismatchNmax 2 \
        --outSAMtype BAM SortedByCoordinate \
        --readFilesCommand zcat \
        --runThreadN 70 \
        --outFileNamePrefix $STAR_OUT
done
