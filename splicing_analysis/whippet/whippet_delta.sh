"""This script compare all psi files with the two given patterns via whippet-delta.jl"""

#!bin/bash

TREATMENT1=$1
TREATMENT2=$2

SET_A=""
SET_B=""

for i in $(ls /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/quant/*_${TREATMENT1}*.psi.gz); do
        SET_A+=$i,
done

for i in $(ls /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/quant/*_${TREATMENT2}*.psi.gz); do
        SET_B+=$i,
done

julia /opt/packages/whippet/Whippet.jl-0.8/bin/whippet-delta.jl \
-a $SET_A \
-b $SET_B \
-d /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/quant \
-o /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/diff_files/${TREATMENT1}_${TREATMENT2}_comparison
