#!/bin/python

import sys, string, os
from textstat.textstat import textstat

inputfile = ''
test_data = ""

script_name = sys.argv[0]
inputfile = sys.argv[1]

with open(inputfile) as myfile:
	test_data="".join(line.rstrip() for line in myfile)

print textstat.flesch_kincaid_grade(test_data)
print textstat.gunning_fog(test_data)
print textstat.coleman_liau_index(test_data)
print textstat.smog_index(test_data)
print textstat.automated_readability_index(test_data)

print "---------"

print textstat.flesch_reading_ease(test_data)
print textstat.smog_index(test_data)
print textstat.flesch_kincaid_grade(test_data)
print textstat.coleman_liau_index(test_data)
print textstat.automated_readability_index(test_data)
print textstat.dale_chall_readability_score(test_data)
print textstat.difficult_words(test_data)
print textstat.linsear_write_formula(test_data)
print textstat.gunning_fog(test_data)
print textstat.readability_consensus(test_data)

