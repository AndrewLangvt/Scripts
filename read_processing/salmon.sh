#!/bin/bash

# This script will map readset with Salmon.

DATA=$1

PIGEON_ASSEMBLY=/pylon2/mc3bg6p/al2025/parental_assembly/RockDove.HPG.v1.1.1.fasta
SALMON_DIR=/pylon2/mc3bg6p/al2025/storage/salmon-0.8.2/bin
SALMON_INDEX=/pylon2/mc3bg6p/al2025/mapping_indices/salmon_index/HPG_parental_index

echo ""
echo "~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~"
echo ""
echo "-----------------------------------------------Now Mapping reads-----------------------------------------------"
echo ""
echo "~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~"
echo ""

# If index is previously generated, the script can access the index file variable $SALMON_INDEX
# defined above.  If index needs to be generated, uncomment the below command to generate
# an index file for the desired assembly.

#$SALMON_DIR/salmon index --type quasi --threads 28 --index ${DATA}_index -t $PIGEON_ASSEMBLY

SALMON_OUT=${DATA}_salmon_mapping
mkdir ${SALMON_OUT}

ID_LIST=`ls -l *TRIM*gz | awk '{print $9}' | sed 's/.TRIM.*//g' | sort -u`
  
for SAMPLE in $ID_LIST; do

        OUTFILE_SALMON=${SAMPLE}_maps.txt
        mkdir ${SALMON_OUT}/salmon_$SAMPLE

        $SALMON_DIR/salmon quant -i $SALMON_INDEX -l A \
        -1 $SAMPLE.TRIM*.R1.fq.gz \
        -2 $SAMPLE.TRIM*.R2.fq.gz \
        -p 32 --gcBias --seqBias --output ${SALMON_OUT}/salmon_${SAMPLE}/$SAMPLE 2>&1 | tee -a $OUTFILE_SALMON
        echo ""

        cat $OUTFILE_SALMON >> ${DATA}_mapping_output.txt
        echo "" >> ${DATA}_mapping_output.txt
        rm $OUTFILE_SALMON
done

mv ${DATA}_mapping_output.txt $SALMON_OUT/
