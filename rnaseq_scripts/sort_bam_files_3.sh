INPUTDIR=
OUTPUTDIR=
cd $INPUTDIR
for f in *.bam
do
BASENAME=$(basename "$f" .bam)
samtools sort $BASENAME.bam -o $OUTPUTDIR/$BASENAME.sorted.bam
rm $BASENAME.bam
done
