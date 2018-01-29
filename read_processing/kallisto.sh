#!/bin/bash

for i in $(ls -l *TRIM.*.R1.fq.gz); do
        READ=$(basename -s .TRIM.*.R1.fq.gz $i)
	kallisto quant -t 64 --bias -b 100 \
-i /pylon2/mc3bg6p/al2025/mapping_indices/kallisto_HPG_parental_index.idx \
-o ${READ}_kallisto_out $READ.TRIM.*.R1.fq.gz $READ.TRIM.*.R2.fq.gz
done
