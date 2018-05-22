# -*- coding: utf-8 -*-
#https://docs.python.org/3.0/whatsnew/3.0.html
#https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set
#https://stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-%C2%A3
import unicodedata #for normalizing (NFC composing unicode diacritics)
import re # for regext find/replace

############### 1 - split string into dictionary
#https://www.fir3net.com/Programming/Python/python-split-a-string-into-a-dictionary.html
#https://stackoverflow.com/questions/16467479/normalizing-unicode - because xy is decomposed, but in versetext is composed, therefore replace doesn't work
print ()
#line2 = u'\\v**\\v 4==ism-illâh**GEN.13.4==istidʿâ**GEN.13.4==mezbah ve**GEN.13.4'
line2 = u'\\v**\\v 5==tesmiye**GEN.1.5==ahşâm**GEN.1.5==sabâh**GEN.1.5==evvelki**GEN.1.5==ahşâm**GEN.1.5==eyle**GEN.1.5==gėce**GEN.1.5'
line1 = line2.replace(' ','##')
print ('line 14',line1)
print()
line = unicodedata.normalize('NFC',line1)
versetext1 = u've Allâh aydınlığını gün ve karaŋlığı gėce tesmiye eyledi ve ahşâm ve sabâh olunca evvelki gün oldu'
versetext = unicodedata.normalize('NFC',versetext1)
#sanitize variable - https://stackoverflow.com/questions/8237647/clear-variable-in-python
cars = None
#cars = dict(x.split('**') for x in line.split('==')) - old try, but makes values into str, needs to be list so I an append suffixes later
#https://stackoverflow.com/questions/4627981/creating-a-dictionary-from-a-string - key thing here is the [v] which turns it into a list
cars = dict((k, [v]) for k, v in (e.split('**') for e in line.split('==')))
print ("line 21", cars)
print ()

############### 2 - extract verse number and verse text into variables, delete from dictionary
#how to get key by value in dictionary ("" is the notation for null): https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary also has python 3 option
#delete verse text from dictionary: https://stackoverflow.com/questions/29218750/what-is-the-best-way-to-remove-a-dictionary-item-by-value-in-python
#https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string - using join because it returns a list
versenum = ''.join((cars['\\v']))
#https://stackoverflow.com/questions/5844672/delete-an-item-from-a-dictionary
if '\\v' in cars:
	del cars['\\v']

############### 3 - creating list and appending versetext to that. In each for loop iteration I can use the last list item and at the end, the last item will include all replaced strings
# also isolating and marking suffix to be moved back at end of script
#https://www.thegeekstuff.com/2013/06/python-list/
verselist = None
verselist = []
verselist.append(versetext)
for x in cars:	
	##need to figure out how to put ## in between spaces of x in cars if space exists
	##works: line2 = re.sub('==([\S\s]+)==',r'===\1===',line)
	xy = re.sub('##', ' ', x)	
	print ('** x is: ',x,' ** xy is: ',xy)
	lastverse = verselist[-1]
	verseupdated = lastverse.replace(xy, "==" + xy + "==",1)
	verseupdated2 = verseupdated.replace(xy,x)
	verselist.append(verseupdated2)
# isolate suffix with regex so at end of script the isolated suffix can be moved back to right place
#https://docs.python.org/3.5/library/re.html
suffixisolate = re.sub('(?<=\S)==(?=\S)', '== @@', verseupdated2) #check to make sure this regex is right, is non-space really going to catch everything? seems to, catches string at beginning of line...
print ('line 47', suffixisolate)
print ()

############### 4 - dealing with the isolated suffix (@@__), decided to insert it into the dictionary value list in position 0, so that when it can be re-attached later
suffixisolatesplit = suffixisolate.split()
#https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
for index, x in enumerate(suffixisolatesplit, start=0):
	#http://forums.devshed.com/python-programming-11/partial-match-search-list-python-661117.html
	if x.startswith("@@"):
		x_cleaned = re.sub('@', '#', x)
		#https://stackoverflow.com/questions/17686809/how-to-find-word-next-to-a-word-in-python	
		previous_word_number = (index - 1)	
		previous_word = suffixisolatesplit[previous_word_number] #https://learnpythonthehardway.org/book/ex34.html
		previous_word_cleaned1 = re.sub('==', '', previous_word)
		previous_word_cleaned = unicodedata.normalize('NFC',previous_word_cleaned1)
		#https://stackoverflow.com/questions/20585920/how-to-add-multiple-values-to-a-dictionary-key-in-python
		#https://stackoverflow.com/questions/21939652/insert-at-first-position-of-a-list-in-python
		#inserting suffix into list as beginning position
		cars[previous_word_cleaned].insert(0,x_cleaned)
		print ('line 65', cars)
		print ()

############### 5 - create new list and isolate annotations with delimiters so that next for loop will catch annotation text, including ones that are multiple words
#print ("suffixisolate is: ",suffixisolate)
whitespacedelimit = re.sub(' ', '##', suffixisolate)
print ('line 71', whitespacedelimit)
print ()
#print ("whitespacedelimit is: ",whitespacedelimit)
isolatedannotations = whitespacedelimit.split("==")
#https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings - removing empty string if exists at beginning of line caused when annotation exists as first word...
#...whitespacedelimit regex fails because if annotation is at beginnging of line there is not space to add ##
isolatedannotations2 = [x for x in isolatedannotations if x]

for key, value in cars.items():
	value2 = '##'.join(value)	
	cars[key] = value2

############### 6 - 
fixedverselist = None
fixedverselist = []
fixedverselist.append(isolatedannotations2)
print ('line 92',fixedverselist)
print ()
for y in cars:
	#normalization to composed not necessary for this for loop for some reason
	lastfixedverse = fixedverselist[-1]
	#https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python - list comprehension and the ternary operator
	#https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_get_to_return_a_default_value_from_a_dictionary.html
	editedlist = [y + "##" + cars.get(y, "ERROR") if x==y else x for x in lastfixedverse]
	#make note of places that normalized composed vs decomposed works - not sure if I should output y or xy in beginning of string above? - could also normalize to composed the whole document before/after script
	fixedverselist.append(editedlist)
#print ("fixedverselist is: ",fixedverselist)
finallastfixedverse = fixedverselist[-1]
print ("line 104 ",finallastfixedverse)
	
############### 7 - 
#https://stackoverflow.com/questions/493819/python-join-why-is-it-string-joinlist-instead-of-list-joinstring
joinstring = (''.join(finallastfixedverse))
print (joinstring)

##### - what's left to do is reattach suffixes to morpheme: e.g. gėce (GEN.1.5)##@@dı needs to look like: gėcedı (GEN.1.5)##
cleanedstring2 = re.sub('####', '', joinstring)
cleanedstring1 = re.sub('##', ' ', cleanedstring2)
cleanedstring = re.sub(' @@\S*(?= )', '', cleanedstring1)
#final string:
#finalstring = versenum + cleanedstring
versenumcleaned = re.sub('##',' ',versenum)
print (versenumcleaned,cleanedstring)
print ()

############### 3 - do a for loop of dictionary, 
############### 	find contents of each key in versetext
############### 	replace with delimiter '=='
############### 	some code to check is ==\w exists, 
############### 		if exists do add following to string "== @@suffix" (later we can connect this back to the morpheme)
############### 4 - find/replace whitespace in versetext with ## delimiter
############### split newversetext into list with ## as delimiter
############### 5 - for loop of dictionary again
############### 	match dictionary key to list
############### 	if match is exact add value to list entry
############### result should be list with annotations added as footnotes	
############### detokenize list
############### find @@suffix and merge it back to morpheme to the left

##cool feature: https://ide.geeksforgeeks.org/index.php
#http://rogerdudler.github.io/git-guide/

