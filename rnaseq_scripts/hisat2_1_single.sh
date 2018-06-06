INPUTDIR=/home/ramaka02/projects/2018/philipp/nac_control_resequence/trimmed_fastq
OUTPUTDIR=/home/ramaka02/projects/2018/philipp/nac_control_resequence/sam
INDEX=/home/ramaka02/resources/ensembl_90/mm10_90/hisat2_index/mm10
cd $INPUTDIR
for f in *_R1_001.trimmed.fastq.gz
do
BASENAME=$(basename "$f" _R1_001.trimmed.fastq.gz)
hisat2 -p 15 -s -x $INDEX -U ${BASENAME}_R1_001.trimmed.fastq.gz -S $OUTPUTDIR/$BASENAME.sam 2> $OUTPUTDIR/$BASENAME
done

