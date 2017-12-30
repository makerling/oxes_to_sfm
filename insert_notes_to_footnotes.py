#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set
#https://stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-%C2%A3
#using python 2

############### 1 - split string into dictionary
#https://www.fir3net.com/Programming/Python/python-split-a-string-into-a-dictionary.html
#orig example: line = "abc**123==xyz**456"
line = "\\v**\\v 5==tesmiye**GEN.1.5==ahşâm**GEN.1.5==sabâh**GEN.1.5==evvelki**GEN.1.5==eyle**GEN.1.5==gėce**GEN.1.5==ve Allâh aydınlığını gün ve karaŋlığı gėce tesmiye eyledi ve ahşâm ve sabâh olunca evvelki gün oldu **"
#https://stackoverflow.com/questions/8237647/clear-variable-in-python
print
cars = None
cars = dict(x.split('**') for x in line.split('=='))
print "cars dictionary is: ", cars
print

############### 2 - extract verse number and verse text into variables, delete from dictionary
#how to get key by value in dictionary ("" is the notation for null): https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary also has python 3 option
versetext = cars.keys()[cars.values().index("")]
#delete verse text from dictionary: https://stackoverflow.com/questions/29218750/what-is-the-best-way-to-remove-a-dictionary-item-by-value-in-python
for key, value in dict(cars).items():
	if value == "":
	    del cars[key]
#https://www.tutorialspoint.com/python/dictionary_get.htm
versenum = cars.get('\\v')
#https://stackoverflow.com/questions/5844672/delete-an-item-from-a-dictionary
if '\\v' in cars:
    del cars['\\v']
print "cars dictionary is: ", cars
print "Verse line: ", versenum, versetext
print

############### 3 -  
print "testing for loop"
for x in cars:
	print versetext.replace(x, "==" + x + "==")

############### 3 - do a for loop of dictionary, 
############### 	find contents of each key in versetext
############### 	replace with delimiter '=='
############### 	some code to check is ==\w exists, 
############### 		if exists do add following to string "== @@suffix" (later we can connect this back to the morpheme)
############### find/replace whitespace in versetext with == delimiter
############### find/replace ==== with == in versetext
############### split newversetext into list with == as delimiter
############### for loop of dictionary again
############### 	match dictionary key to list
############### 	if match is exact add value to list entry
############### 	(need to figure out what to do with multiples, add to 1st?)
############### result should be list with annotations added as footnotes	
############### detokenize list
############### find @@suffix and merge it back to morpheme to the left

