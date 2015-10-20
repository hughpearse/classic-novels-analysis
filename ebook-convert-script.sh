#!/bin/bash

for i in `ls -1`;
do
	ebook-convert ./$i ./text/${i/epub/txt}
done
