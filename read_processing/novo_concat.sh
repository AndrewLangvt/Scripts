DIR=$1
OUT_DIR=renamed_reads1

for sample in $(ls $DIR); do

	# Testing to see if R2 concatenated file already exists. The R2 files will be generated
	# second, so it's presence will be a better metric of progress than the R1 files

	if test -e $OUT_DIR/$sample.R2.fastq.gz; then
		echo $sample already exists, moving to next
		continue
	else
		# Concatenating R1 & R2 files, printing filename to stdout to track progress.  
		# Also will allow for me to remove any incompletely concatenated reads before 
		# restarting script (i.e. when headnode boots me off of the system)

		echo now concatenating reads for $sample.R1
		cat $(find $DIR/$sample -name *_1.fq.gz | sort) > $OUT_DIR/$sample.R1.fastq.gz
		echo $sample.R1 complete

            	echo now concatenating reads for $sample.R2
                cat $(find $DIR/$sample -name *_2.fq.gz | sort) > $OUT_DIR/$sample.R2.fastq.gz
                echo $sample.R2 complete
	fi 
done
