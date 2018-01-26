#!/bin/bash

DATA=$1

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
                LREADS_LIST+=${READ}.R1.fastq.gz,
                RREADS_LIST+=${READ}.R2.fastq.gz,
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
