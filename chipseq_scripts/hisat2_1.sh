INPUTDIR=
OUTPUTDIR=
INDEX=
cd $INPUTDIR
for f in *_R1_001.fastq.gz
do
BASENAME=$(basename "$f" _R1_001.fastq.gz)
hisat2 -p 15 -s -x $INDEX -1 ${BASENAME}_R1_001.fastq.gz -2 ${BASENAME}_R2_001.fastq.gz -S $OUTPUTDIR/$BASENAME.sam 2> $OUTPUTDIR/$BASENAME
done
