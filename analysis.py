#!/bin/python

import sys, string, os
from textstat.textstat import textstat

inputfile = ''
test_data = ""

script_name = sys.argv[0]
inputfile = sys.argv[1]

with open(inputfile) as myfile:
	test_data="".join(line.rstrip() for line in myfile)

var1 = str(textstat.flesch_reading_ease(test_data))
var2 = str(textstat.smog_index(test_data))
var3 = str(textstat.flesch_kincaid_grade(test_data))
var4 = str(textstat.coleman_liau_index(test_data))
var5 = str(textstat.automated_readability_index(test_data))
var6 = str(textstat.dale_chall_readability_score(test_data))
var7 = str(textstat.difficult_words(test_data))
var8 = str(textstat.linsear_write_formula(test_data))
var9 = str(textstat.gunning_fog(test_data))
var10 = str(textstat.readability_consensus(test_data))
var11 = str(textstat.syllable_count(test_data))
var12 = str(textstat.lexicon_count(test_data, 1))
var13 = str(textstat.sentence_count(test_data))

print(var1 + ',' + var2 + ',' + var3 + ',' + var4 + ',' + var5 + ',' + var6 + ',' + var7 + ',' + var8 + ',' + var9 + ',' + var10 + ',' + var11 + ',' + var12 + ',' + var13)
