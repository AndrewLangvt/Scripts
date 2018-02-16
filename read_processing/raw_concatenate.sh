# This script is specifically for concatenating the RAW read files from NYGC and NOVO

DIR1=/pylon2/mc3bg6p/al2025/NYGC_NOVO_concatenate_reads/NYGC_reseq_reads
DIR2=/pylon2/mc3bg6p/al2025/NYGC_NOVO_concatenate_reads/NOVO_reseq_reads
OUT_DIR=/pylon2/mc3bg6p/al2025/NYGC_NOVO_concatenate_reads/concatenated_raw_reads

for sample in $(cat /pylon2/mc3bg6p/al2025/NYGC_NOVO_concatenate_reads/concat_raw.txt); do

        # Testing to see if R2 concatenated file already exists. The R2 files will be generated
        # second, so it's presence will be a better metric of progress than the R1 files

        if test -e $OUT_DIR/$sample.NYNO_noTrim.R2.fastq.gz; then
                echo $sample already exists, moving to next
                continue
        else
              	# Concatenating R1 & R2 files, printing filename to stdout to track progress.
                # Also will allow for me to remove any incompletely concatenated reads before
                # restarting script (i.e. when headnode boots me off of the system)

                # I have to refer to the NOVO samples as $sample*R1.fastq.gz because the Lane_18 samples are
                # sample_NOVO.R1.fastq.gz and all reads sequenced at NOVO after Lane 18 do not have _NOVO

                echo now concatenating reads for $sample.R1
                cat $DIR1/$sample.R1.fastq.gz $DIR2/$sample*R1.fastq.gz > $OUT_DIR/$sample.NYNO_noTrim.R1.fastq.gz
                echo $sample.R1 complete
                echo now concatenating reads for $sample.R2
                cat $DIR1/$sample.R2.fastq.gz $DIR2/$sample*R2.fastq.gz > $OUT_DIR/$sample.NYNO_noTrim.R2.fastq.gz
                echo $sample.R1 complete
                echo
        fi
done
