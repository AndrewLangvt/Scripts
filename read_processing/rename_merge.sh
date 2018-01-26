#!/bin/bash
#2017JUL28
#Andrew Lang

#This shell file combines all readfiles for R1, and R2 readfiles.  It also strips the "Sample_" prefix
#from the readfile name.  Set OUTDIR to desired output location

OUT=<OUTDIR>

for READ_NAME in $(ls -1 $1);
        do
        NEW_NAME=`echo $READ_NAME | sed 's/Sample_//;s/-male/_male/;s/-female/_female/;s/-hypothalamus/_hypothalamus/;s/-pituitary/_pituitary/;s/-hypo/_hypothalamus/;s/-pit/_pituitary/;s/-ovary/_gonad/;s/-testes/_gonad/;s/-gonad/_gonad/;s/-control/_control/;s/-stress/_stress/;s/_hypothalamus-/_hypothalamus_/;s/_pituitary-/_pituitary_/;s/_gonad-/_gonad_/'`

                if test -d $1/$READ_NAME/fastq/; then
                        cat $(find $1/$READ_NAME/ -name *[.]R1[.]*fastq.gz | sort) > $OUT/$NEW_NAME.R1.fastq.gz
                        cat $(find $1/$READ_NAME/ -name *[.]R2[.]*fastq.gz | sort) > $OUT/$NEW_NAME.R2.fastq.gz
                else
                        cat $(find $1/$READ_NAME/ -name *[_]R1[_]*fastq.gz | sort) > $OUT/$NEW_NAME.R1.fastq.gz
                        cat $(find $1/$READ_NAME/ -name *[_]R3[_]*fastq.gz | sort) > $OUT/$NEW_NAME.R2.fastq.gz
                fi
done
