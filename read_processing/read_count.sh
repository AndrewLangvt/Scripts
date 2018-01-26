#!/bin/bash
#Andrew S Lang
#28JUL2017

DATA=$1
LOOK_DIR=$2

for i in $(ls -l $LOOK_DIR | awk '{print $9}');
        do
	echo gunzip -t $LOOK_DIR/$i >> ${DATA}_gzip_test.txt
        gunzip -t $LOOK_DIR/$i 2>&1 | tee -a ${DATA}_gzip_test.txt
done

echo "READ_ID READ_COUNT SIZE READ_ID_CONFIRM" > ${DATA}_stats1.txt

zgrep -c "@H" $LOOK_DIR/*.gz >> ${DATA}_counts.txt

sed 's/.*\///;s/:/ /' ${DATA}_counts.txt > ${DATA}_counts_trimmed.txt

ls -lh $LOOK_DIR/*.gz | awk '{print $5 " " $9}' >> ${DATA}_size1.txt

sed 's/\/.*\///' ${DATA}_size1.txt > ${DATA}_size.txt

paste ${DATA}_counts_trimmed.txt ${DATA}_size.txt > ${DATA}_stats2.txt

cat ${DATA}_stats1.txt ${DATA}_stats2.txt > ${DATA}_stats.txt

rm ${DATA}_size1.txt
rm ${DATA}_stats1.txt
rm ${DATA}_stats2.txt
rm ${DATA}_counts_trimmed.txt
rm ${DATA}_size.txt

mv ${DATA}_gzip_test.txt $LOOK_DIR
mv ${DATA}_counts.txt $LOOK_DIR
mv ${DATA}_stats.txt $LOOK_DIR
