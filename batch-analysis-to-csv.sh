#!/bin/bash

for i in `ls -1 ./ebooks-text/*.txt`;
do
	title=`echo $i | sed -r -e 's/(.\/ebooks-text\/)(.*)(.txt)/\2/g' | tr '-' ' ' | sed -r -e 's/(.*)( by )(.*)/\1/g'`
	author=`echo $i | sed -r -e 's/(.\/ebooks-text\/)(.*)(.txt)/\2/g' | tr '-' ' ' | sed -r -e 's/(.*)( by )(.*)/\3/g'`
	results=`./analysis.py $i`
	echo "\"$title\",\"$author\",$results" >> ./results.csv
done
