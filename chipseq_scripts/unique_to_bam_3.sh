INPUTDIR=
OUTPUTDIR=
cd $INPUTDIR
for f in *.unique.sam
do
BASENAME=$(basename "$f" .unique.sam)
samtools view -Sb $BASENAME.unique.sam > $OUTPUTDIR/$BASENAME.unique.bam
done
