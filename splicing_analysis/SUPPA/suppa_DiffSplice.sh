# suppa_DiffSplice.sh
# Andrew S. Lang
# Created: 26MAR2018
# Last Modified: 26MAR2018

# This script performs the SUPPA differential splicing analyses on any two patterns given as 2nd and 3rd cmd line args (sex_tissue_treatment)

# Execute this script as follows from the /pylon5/mc3bg6p/al2025/isoform/SUPPA/ directory
# sh /pylon5/mc3bg6p/al2025/isoform/SUPPA/scripts/suppa_DiffSplice.sh Sex_tissue_treatment-1 sex_tissue_treatment-2

PATTERN1=$1
first=$(name=`echo ${PATTERN1} | cut -d "_" -f1 | tr '[:lower:]' '[:upper:]'`&& echo ${name:0:1})
second=$(name=`echo ${PATTERN1} | cut -d "_" -f2 | tr '[:lower:]' '[:upper:]'`&& echo ${name:0:1})
third=$(name=`echo ${PATTERN1} | cut -d "_" -f3 | tr '[:lower:]' '[:upper:]'`&& echo ${name:0:1})
ShortPat1=$(echo ${first}${second}${third})

PATTERN2=$2
first=$(name=`echo ${PATTERN2} | cut -d "_" -f1 | tr '[:lower:]' '[:upper:]'`&& echo ${name:0:1})
second=$(name=`echo ${PATTERN2} | cut -d "_" -f2 | tr '[:lower:]' '[:upper:]'`&& echo ${name:0:1})
third=$(name=`echo ${PATTERN2} | cut -d "_" -f3 | tr '[:lower:]' '[:upper:]'`&& echo ${name:0:1})
ShortPat2=$(echo ${first}${second}${third})

CommaListPat1=$(for i in $(ls /pylon5/mc3bg6p/al2025/isoform/SUPPA/colLiv-v2_*salmon_mapping/*/*_${PATTERN1}*_v2 -d | sed 's/.*\///'); do list+="$i,";done && echo "${list::-1}" && list="")
CommaListPat2=$(for i in $(ls /pylon5/mc3bg6p/al2025/isoform/SUPPA/colLiv-v2_*salmon_mapping/*/*_${PATTERN2}*_v2 -d | sed 's/.*\///'); do list+="$i,";done && echo "${list::-1}" && list="")

echo
echo ~~~~~~~~~~~~ Extracting Expression Data for Desired Treatments from Expression File ~~~~~~~~~~~~~
echo

Rscript /pylon5/mc3bg6p/al2025/storage/SUPPA-master/scripts/split_file_edit.R \
/pylon5/mc3bg6p/al2025/isoform/SUPPA/v2_iso_TPM_ALL.txt \
$(echo $CommaListPat1) \
$(echo $CommaListPat2) \
psi_tpm_files/${ShortPat1}.tpm psi_tpm_files/${ShortPat2}.tpm

echo
echo ~~~~~~~~~~~~~~~~~~~ Extracting PSI Data for Desired Treatments from PSI File ~~~~~~~~~~~~~~~~~~~~
echo

Rscript /pylon5/mc3bg6p/al2025/storage/SUPPA-master/scripts/split_file_edit.R \
/pylon5/mc3bg6p/al2025/isoform/SUPPA/All_events_parental.psi \
$(echo $CommaListPat1) \
$(echo $CommaListPat2) \
psi_tpm_files/${ShortPat1}.psi psi_tpm_files/${ShortPat2}.psi

echo
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Performing Differential Splicing Analysis ~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo

python3 /pylon5/mc3bg6p/al2025/storage/SUPPA-master/suppa.py diffSplice \
--method empirical --gene-correction \
--ioe /pylon5/mc3bg6p/al2025/isoform/SUPPA/ColLiv_V2_events/ColLiv_V2_forSUPPA.allevents.ioe \
--psi /pylon5/mc3bg6p/al2025/isoform/SUPPA/psi_tpm_files/${ShortPat1}.psi /pylon5/mc3bg6p/al2025/isoform/SUPPA/psi_tpm_files/${ShortPat2}.psi \
--expression-files /pylon5/mc3bg6p/al2025/isoform/SUPPA/psi_tpm_files/${ShortPat1}.tpm /pylon5/mc3bg6p/al2025/isoform/SUPPA/psi_tpm_files/${ShortPat2}.tpm \
--output /pylon5/mc3bg6p/al2025/isoform/SUPPA/diffsplice_out/${ShortPat1}-${ShortPat2}_diffsplice\
&&\
python3 /pylon5/mc3bg6p/al2025/isoform/SUPPA/scripts/sig_genes_suppa.py \
/pylon5/mc3bg6p/al2025/isoform/SUPPA/diffsplice_out/${ShortPat1}-${ShortPat2}_diffsplice.dpsi

echo
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Alternatively Spliced Gene IDs Extracted ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo

mv spliced_genes-SUPPA-${ShortPat1}-${ShortPat2}.tsv /pylon5/mc3bg6p/al2025/isoform/SUPPA/spliced_genes_files
