#!/bin/bash

# This script will error correct, trim, and map reads using r_corrector.pl, trimmomatic, and salmon respectively.
# Make sure to set DATA and ADAPTERS to reflect correct dataset

DATA=$1

ADAPTERS=/home/al2025/linuxbrew/.linuxbrew/Cellar/trimmomatic/0.36/share/trimmomatic/adapters/NEB-PE.fa
#ADAPTERS=/home/al2025/linuxbrew/.linuxbrew/Cellar/trimmomatic/0.36/share/trimmomatic/adapters/TruSeq3-PE-2.fa

PIGEON_ASSEMBLY=/pylon2/mc3bg6p/al2025/parental_assembly/RockDove.HPG.v1.1.1.fasta
SALMON_DIR=/pylon2/mc3bg6p/al2025/storage/salmon-0.8.2/bin
SALMON_INDEX=/pylon2/mc3bg6p/al2025/mapping_indices/salmon_index/HPG_parental_index

ID_LIST=`ls -l *fastq.gz | awk '{print $9}' | sed 's/[\.]R[1-2][\.].*//g;s/.*[\/]//g' | sort -u`

IFS=' ' read -r -a LIST_ARRAY <<< $ID_LIST

LIST_ALL=`echo ${LIST_ARRAY[@]:0}`

declare -a READ_SETS=("$LIST_ALL")

echo ""
echo "~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~"
echo ""
echo "----------------------------------------------Now correcting reads----------------------------------------------"
echo ""
echo "~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~"
echo ""

for LIST in "${READ_SETS[@]}";
        do

	LREADS_COM=""
        RREADS_COM=""
        LREADS_LIST=""
        RREADS_LIST=""

        for READ in $LIST; do
                LREADS_LIST+=`ls ${READ}.*R1.fastq.gz`,
                RREADS_LIST+=`ls ${READ}.*R2.fastq.gz`,
        done

	#trimming the comma off the end of the list
        LREADS_COM=`echo ${LREADS_LIST::-1}`
        RREADS_COM=`echo ${RREADS_LIST::-1}`

        echo "" #simply a space to separate the correction runs

        perl /pylon2/mc3bg6p/al2025/storage/rcorrector/run_rcorrector.pl -k 31 -t 40 -1 $LREADS_COM -2 $RREADS_COM 2>&1 | tee -a temp_${DATA}_error_correct.txt

        #concatenate current output with previous output, cleanup, and move to location with reads
        cat temp_${DATA}_error_correct.txt >> ${DATA}_error_correct.txt
        rm temp_${DATA}_error_correct.txt
done

echo ""
echo "~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~"
echo ""
echo "-----------------------------------------------Now Trimming reads-----------------------------------------------"
echo ""
echo "~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~"
echo ""

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

	mv ${TRIM_ID}_1P $READ.TRIM.R1.fq
	mv ${TRIM_ID}_2P $READ.TRIM.R2.fq

	gzip $READ.TRIM.R1.fq
	gzip $READ.TRIM.R2.fq

	rm ${TRIM_ID}_[1-2]U
	rm $OUTFILE
done

echo ""
echo "~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~"
echo ""
echo "-----------------------------------------------Now Mapping reads-----------------------------------------------"
echo ""
echo "~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~%~~"
echo ""

#if index is previously generated, the script can access the index file variable $SALMON_INDEX
#defined above.  If index needs to be generated, uncomment the below command to generate
#an index file for the desired assembly. 

#$SALMON_DIR/salmon index --type quasi --threads 28 --index ${DATA}_index -t $PIGEON_ASSEMBLY

SALMON_OUT=${DATA}_salmon_mapping
mkdir ${SALMON_OUT}

for SAMPLE in $ID_LIST;do

	OUTFILE_SALMON=${SAMPLE}_maps.txt
	mkdir ${SALMON_OUT}/salmon_$SAMPLE

	$SALMON_DIR/salmon quant -i $SALMON_INDEX -l A \
	-1 $SAMPLE.TRIM.R1.fq.gz \
	-2 $SAMPLE.TRIM.R2.fq.gz \
	-p 32 --gcBias --seqBias --output ${SALMON_OUT}/salmon_${SAMPLE}/$SAMPLE 2>&1 | tee -a $OUTFILE_SALMON
        echo ""

        cat $OUTFILE_SALMON >> ${DATA}_mapping_output.txt
        echo "" >> ${DATA}_mapping_output.txt
	rm $OUTFILE_SALMON
done

mv ${DATA}_mapping_output.txt $SALMON_OUT/
