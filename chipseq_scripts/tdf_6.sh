INPUTDIR=
OUTPUTDIR=
CHROMSIZESFILE=
cd $INPUTDIR
for f in *.unique.sorted.rmdup.bam
do
BASENAME=$(basename "$f" .unique.sorted.rmdup.bam)
igvtools count $BASENAME.unique.sorted.rmdup.bam $OUTPUTDIR/$BASENAME.unique.sorted.rmdup.tdf $CHROMSIZESFILE
done
