INPUTDIR=
OUTPUTDIR=
cd $INPUTDIR
for f in *.sam
do
BASENAME=$(basename "$f" .sam)
grep -E 'NH:i:1|@' $BASENAME.sam > $OUTPUTDIR/$BASENAME.unique.sam
done
