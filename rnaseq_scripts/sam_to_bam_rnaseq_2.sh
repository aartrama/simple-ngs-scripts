INPUTDIR=
OUTPUTDIR=
cd $INPUTDIR
for f in *.sam
do
BASENAME=$(basename "$f" .sam)
samtools view -Sb $BASENAME.sam > $OUTPUTDIR/$BASENAME.bam
rm $BASENAME.sam
done
