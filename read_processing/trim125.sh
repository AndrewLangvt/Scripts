#!/bin/bash

# This script will trim reads at 125bp in the directory from which it is executed.
# Make sure to set DATA and ADAPTERS to reflect correct dataset

DATA=$1

ADAPTERS=/home/al2025/linuxbrew/.linuxbrew/Cellar/trimmomatic/0.36/share/trimmomatic/adapters/NEB-PE.fa
#ADAPTERS=/home/al2025/linuxbrew/.linuxbrew/Cellar/trimmomatic/0.36/share/trimmomatic/adapters/TruSeq3-PE-2.fa

ID_LIST=`ls -l *cor.fq.gz | awk '{print $9}' | sed 's/[\.]R[1-2][\.].*//g;s/.*[\/]//g' | sort -u`

for READ in $ID_LIST;do
        TRIM_ID=${READ}_TRIM
        OUTFILE=${TRIM_ID}_STATS.txt

        trimmomatic PE -phred33 -threads 28 -baseout $TRIM_ID \
        $READ.R1.cor.fq.gz $READ.R2.cor.fq.gz \
        ILLUMINACLIP:$ADAPTERS:2:40:15 LEADING:2 TRAILING:2 SLIDINGWINDOW:4:2 \
        CROP:125 \
        MINLEN:25 2>&1 | tee -a $OUTFILE
        echo ""

        cat $OUTFILE >> ${DATA}_trimming_output.txt
        echo "" >> ${DATA}_trimming_output.txt

        echo $READ >> ${DATA}_reads_trimmed.txt
        grep "Input Read Pairs" $OUTFILE >> ${DATA}_reads_trimmed.txt 
        echo "" >> ${DATA}_reads_trimmed.txt

        mv ${TRIM_ID}_1P $READ.TRIM.125.R1.fq
        mv ${TRIM_ID}_2P $READ.TRIM.125.R2.fq

        gzip $READ.TRIM.125.R1.fq
        gzip $READ.TRIM.125.R2.fq

        rm ${TRIM_ID}_[1-2]U
        rm $OUTFILE
done
