cd /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/

READ_LOC=/pylon2/mc3bg6p/al2025/isoform/subset

##julia /opt/packages/whippet/Whippet.jl-0.8/bin/whippet-index.jl \
##--fasta /pylon2/mc3bg6p/al2025/isoform/colLiv2_genome/Rockdove_cliv2.gtf
##--gtf /pylon2/mc3bg6p/al2025/isoform/colLiv2_genome/Rockdove_cliv2.gtf
##--index /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/index/ColLiv_v2

for i in $(ls $READ_LOC/*TRIM.R1.fq.gz); do

        SAMPLE=$(basename -s .TRIM.R1.fq.gz $i)
        echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        echo mapping $SAMPLE
        echo ""
        julia /opt/packages/whippet/Whippet.jl-0.8/bin/whippet-quant.jl \
        --index /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/index/ColLiv_v2 \
        --out /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/quant/$SAMPLE \
        --mismatches 2 \
        --score-min 0 \
        --phred-33 \
        --circ \
        $READ_LOC/$SAMPLE.TRIM.R1.fq.gz $READ_LOC/$SAMPLE.TRIM.R2.fq.gz
        echo ""
        echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        echo ""
done
