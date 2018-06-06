INPUTDIR=
OUTPUTDIR=
GTFFILE=
cd $INPUTDIR
for f in *.sorted.bam
do
BASENAME=$(basename "$f" .sorted.bam)
htseq-count -f bam -s no $BASENAME.sorted.bam $GTFFILE > $OUTPUTDIR/$BASENAME.counts.txt
done

