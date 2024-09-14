#!/bin/bash
for i in {1..2} # twice compressed seems to be the best.. i ran it from 1 to 300 maybe there is a better but 2nd was the best
do
  gzip --best $1
#  sleep 1
  mv $1.gz $1
  cp $1 $1-$i
  echo $i # this is just to see the progress.
done
# cleanup 
mv $1 test.gz.gz
rm $1*
mv test.gz.gz $1.gz.gz
