# This script will run the mergeNovelSplices function of Qorts.jar to compare count files of two treatment groups. 
# It is executed as follows
# 1st cmd line arg: name for directory (eg. maleH_SvC)
# 2nd cmd line arg: pattern to search for (e.g male_hypothalamus)
# 3rd cmd line arg: what aspect to compare between (1= bird ID, 2= sex, 3= tissue, 4= treatment)

mkdir /pylon2/mc3bg6p/al2025/isoform/JunctionSeq_analysis/qorts_files/counts/$1

echo -e sample.ID"\t"group.ID > /pylon2/mc3bg6p/al2025/isoform/JunctionSeq_analysis/qorts_files/counts/$1/${1}_decoder_file.txt 
for i in $(ls -d /pylon2/mc3bg6p/al2025/isoform/JunctionSeq_analysis/qorts_files/rawCts/*_${2}*); do
        SAMPLE=`basename $i`
        GROUP=`echo $SAMPLE | cut -d "_" -f $3`
        echo -e $SAMPLE"\t"$GROUP >> /pylon2/mc3bg6p/al2025/isoform/JunctionSeq_analysis/qorts_files/counts/$1/${1}_decoder_file.txt
done

java -jar /pylon2/mc3bg6p/al2025/storage/QoRTs.jar mergeNovelSplices \
--minCount 6 \
--stranded \
/pylon2/mc3bg6p/al2025/isoform/JunctionSeq_analysis/qorts_files/rawCts \
/pylon2/mc3bg6p/al2025/isoform/JunctionSeq_analysis/qorts_files/counts/$1/${1}_decoder_file.txt \
/pylon2/mc3bg6p/al2025/isoform/genome_compare/GCF_000337935.1_Cliv_1.0_genomic.gtf \
/pylon2/mc3bg6p/al2025/isoform/JunctionSeq_analysis/qorts_files/counts/$1
