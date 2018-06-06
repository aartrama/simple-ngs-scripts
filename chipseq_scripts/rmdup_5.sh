INPUTDIR=
OUTPUTDIR=
cd $INPUTDIR
for f in *.unique.sorted.bam
do
BASENAME=$(basename "$f" .unique.sorted.bam)
samtools rmdup $BASENAME.unique.sorted.bam $OUTPUTDIR/$BASENAME.unique.sorted.rmdup.bam 2> $OUTPUTDIR/$BASENAME
done
