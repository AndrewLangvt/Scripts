zcat /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/quant/*psi.gz | awk '{print $3}' | sort -u | sed 's/Coord//g' | sed '1d' >> TOT_IDs

python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/R-W7_female_pituitary_stress.psi.gz FPS-1 > psi_matrix/FPS-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/R-W7_female_hypothalamus_stress.psi.gz FHS-1 > psi_matrix/FHS-1_psi_COL
#python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/R-W7_female_gonad_stress.psi.gz FGS-1 > psi_matrix/FGS-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/R-W44_female_pituitary_control.psi.gz FPC-1 > psi_matrix/FPC-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/R-W44_female_hypothalamus_control.psi.gz FHC-1 > psi_matrix/FHC-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/R-W44_female_gonad_control.psi.gz FGC-1 > psi_matrix/FGC-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/R-Blu12_female_pituitary_stress.psi.gz FPS-2 > psi_matrix/FPS-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/R-Blu12_female_hypothalamus_stress.psi.gz FHS-2 > psi_matrix/FHS-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/R-Blu12_female_gonad_stress.psi.gz FGS-2 > psi_matrix/FGS-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/r6-x_female_pituitary_control.psi.gz FPC-2 > psi_matrix/FPC-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/r6-x_female_hypothalamus_control.psi.gz FHC-2 > psi_matrix/FHC-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/r6-x_female_gonad_control.psi.gz FGC-2 > psi_matrix/FGC-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-R3_male_pituitary_control.psi.gz MPC-1 > psi_matrix/MPC-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-R3_male_hypothalamus_control.psi.gz MHC-1 > psi_matrix/MHC-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-R3_male_gonad_control.psi.gz MGC-1 > psi_matrix/MGC-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-R2_male_pituitary_stress.psi.gz MPS-1 > psi_matrix/MPS-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-R2_male_hypothalamus_stress.psi.gz MHS-1 > psi_matrix/MHS-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-R2_male_gonad_stress.psi.gz MGS-1 > psi_matrix/MGS-1_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-O116_male_pituitary_stress.psi.gz MPS-2 > psi_matrix/MPS-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-O116_male_hypothalamus_stress.psi.gz MHS-2 > psi_matrix/MHS-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-O116_male_gonad_stress.psi.gz MGS-2 > psi_matrix/MGS-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-G107_male_pituitary_control.psi.gz MPC-2 > psi_matrix/MPC-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-G107_male_hypothalamus_control.psi.gz MHC-2 > psi_matrix/MHC-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-G107_male_gonad_control.psi.gz MGC-2 > psi_matrix/MGC-2_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-Blu13_male_pituitary_control.psi.gz MPC-3 > psi_matrix/MPC-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-Blu13_male_hypothalamus_control.psi.gz MHC-3 > psi_matrix/MHC-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/L-Blu13_male_gonad_control.psi.gz MGC-3 > psi_matrix/MGC-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/g105-x_male_pituitary_stress.psi.gz MPS-3 > psi_matrix/MPS-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/g105-x_male_hypothalamus_stress.psi.gz MHS-3 > psi_matrix/MHS-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/g105-x_male_gonad_stress.psi.gz MGS-3 > psi_matrix/MGS-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/blu-o-x-ATLAS_female_pituitary_control.psi.gz FPC-3 > psi_matrix/FPC-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/blu-o-x-ATLAS_female_hypothalamus_control.psi.gz FHC-3 > psi_matrix/FHC-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/blu-o-x-ATLAS_female_gonad_control.psi.gz FGC-3 > psi_matrix/FGC-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/blu7-x_female_pituitary_stress.psi.gz FPS-3 > psi_matrix/FPS-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/blu7-x_female_hypothalamus_stress.psi.gz FHS-3 > psi_matrix/FHS-3_psi_COL
python3 /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/matrix_psi.py TOT_IDs quant/blu7-x_female_gonad_stress.psi.gz FGS-3 > psi_matrix/FGS-3_psi_COL

echo "Treatment" | cat - TOT_IDs > temp && mv temp TOT_IDs
echo "Tissue" | cat - TOT_IDs > temp && mv temp TOT_IDs
echo "Sex" | cat - TOT_IDs > temp && mv temp TOT_IDs
echo "ID" | cat - TOT_IDs > temp && mv temp TOT_IDs

paste psi_matrix/*_psi_COL > psi_matrix/subset_psi_matrix_samp_cols.tsv
paste TOT_IDs psi_matrix/subset_psi_matrix_samp_cols.tsv > psi_matrix/subset_psi_matrix.tsv
mv TOT_IDs psi_matrix
