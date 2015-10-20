#!/bin/bash

for i in `ls -1`;
do
	mv ./$i ./${i/txt.txt/txt}
done
