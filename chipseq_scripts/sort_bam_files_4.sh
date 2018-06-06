INPUTDIR=
OUTPUTDIR=
cd $INPUTDIR
for f in *.unique.bam
do
BASENAME=$(basename "$f" .unique.bam)
samtools sort $BASENAME.unique.bam -o $OUTPUTDIR/$BASENAME.unique.sorted.bam
done
