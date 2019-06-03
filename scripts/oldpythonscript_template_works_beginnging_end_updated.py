# -*- coding: utf-8 -*-
#run using python 3 to handle unicode automatically
#rm -fr workingdirectory/oldpythonscript_template_works_beginnging_end_updated_log && python3 scripts/oldpythonscript_template_works_beginnging_end_updated.py 1665 | tee -a workingdirectory/oldpythonscript_template_works_beginnging_end_updated_log
#https://docs.python.org/3.0/whatsnew/3.0.html
#https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set
#https://stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-%C2%A3
import unicodedata #for normalizing (NFC composing unicode diacritics)
import re # for regext find/replace
import sys #for passing variable arguments to script - OSM project number e.g. 1665
from pathlib import Path

############### 1 - split string into dictionary
#https://www.fir3net.com/Programming/Python/python-split-a-string-into-a-dictionary.html
#https://stackoverflow.com/questions/16467479/normalizing-unicode - because xy is decomposed, but in versetext is composed, therefore replace doesn't work

projectnum1=sys.argv[1]
projectnum=str(projectnum1)

srcfile = '/home/user/code/oxes_to_sfm/workingdirectory/sfmoutput' + projectnum + '_1.sfm'
workfile = '/home/user/code/oxes_to_sfm/workingdirectory/' + projectnum + 'pythonoutput.sfm'
QAfile = '/home/user/code/oxes_to_sfm/workingdirectory/pythonsfmoutput' + projectnum + 'fordiff.sfm'
#create empty file for processing
Path(workfile).touch()
with open(workfile, 'w') as clearfile:
	print('clearing ' + workfile + ' file')
with open(QAfile, 'w') as clearfile:
	print('clearing ' + QAfile + ' file')
#strip newlines before \p then after script put them back
with open(srcfile, 'r') as file:
	filedata = file.read()
fstrip = re.sub(r'\n\\p',' &&\\p',filedata)
with open(srcfile, 'w') as file:
	file.write(fstrip)

with open(srcfile, 'r') as file:	
	for fileline in file:
		matchesv = re.match(r'\\\\v\*\*\\\\v \d+==[^#]', fileline)
		matchesmt = re.match(r'\\\\mt\*\*\\\\mt \d+==[^#]', fileline)
		print ('this line is: ',fileline)
		if matchesv or matchesmt:
			#generating list to compare missing notations with oxes file
			#QAlineremovequotes = re.sub("\"","\\\"",fileline)
			#print ('QAlineremovequotes is: ',QAlineremovequotes)
			QAline = re.findall('(?<=\\\\fr )[A-Z0-9]{3}\.\d+\.\d+ .+?(?=\d)',fileline) #(?<=\\f \+ \\fr )[A-Z0-9]{3}\.\d+\.\d+ .+?(?=\d)
			print ('QAline is: ',QAline)
			with open(QAfile,'a') as f:
				f.write('\n'.join(QAline))
			print ('wrote to file')			
			linesplit = fileline.split('==####')
			line2 = linesplit[0]
			line1 = line2.replace(' ','##').replace('\\\\','\\').replace('##-','## ')
			print ('line 35',line1)
			print()
			line = unicodedata.normalize('NFC',line1)
			versetext1 = linesplit[1]
			print ('line 39',versetext1)
			print()
			##versetext1 = u'yaʿnî evvelde orada mezbah ve yapdığı yere dek ve Âbrâm orada ism-illâha istidʿâ ėtdi '
			versetext = unicodedata.normalize('NFC',versetext1)
			#sanitize variable - https://stackoverflow.com/questions/8237647/clear-variable-in-python
			cars = None
			#cars = dict(x.split('**') for x in line.split('==')) - old try, but makes values into str, needs to be list so I an append suffixes later
			#https://stackoverflow.com/questions/4627981/creating-a-dictionary-from-a-string - key thing here is the [v] which turns it into a list
			cars = dict((k, [v]) for k, v in (e.split('**') for e in line.split('==')))
			print ("line 48", cars)
			print ()

			############### 2 - extract verse number and verse text into variables, delete from dictionary
			#https://stackoverflow.com/questions/5844672/delete-an-item-from-a-dictionary
			if '\\v' in cars:
				#how to get key by value in dictionary ("" is the notation for null): https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary also has python 3 option
				#delete verse text from dictionary: https://stackoverflow.com/questions/29218750/what-is-the-best-way-to-remove-a-dictionary-item-by-value-in-python
				#https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string - using join because it returns a list
				versenum = ''.join((cars['\\v']))
				del cars['\\v']
			if '\\mt' in cars:
				versenum = ''.join((cars['\\mt']))
				del cars['\\mt']		

			############### 3 - creating list and appending versetext to that. In each for loop iteration I can use the last list item and at the end, the last item will include all replaced strings
			# also isolating and marking suffix to be moved back at end of script
			#https://www.thegeekstuff.com/2013/06/python-list/
			verselist = None
			verselist = []
			verselist.append(versetext)

			print ('#####################################################################################################################')
			print ('#######################################start testing error catching##################################################')
			print ('#####################################################################################################################')

			newlist = []
			for key in cars:
				print (key, 'corresponds to', cars[key])
				newlist.append(key)
			print ('newlist is: ', newlist)#.rstrip('\n')

			keystodelete = []
			for x in newlist:
				for key in cars:
					print ('key is: ',key)
					print ('x is: ',x)
					print ('is ',x,'in ',key,'and ',x,'not equal to ',key,'?')					
					n = re.findall(x,key,re.I)
					print ('count is: ',len(n))
					if (len(n) == 1 and x != key):
						#print ()
						#print ('60 #### nested annotation	####: ',x,' is nested in: ',key)
						n = re.findall(x,key,re.I)
						print ('Yes! ',x,'is nested in ',key,'and ',x,' is not equal to ',key,'.')						
						print ('count is: ',len(n))
						print (x,' is nested in ',key)
						keystodelete.append(x)

			#terms to delete from cars dictionary
			for r in keystodelete:
				del cars[r]
				print ('deleting ',r,'from cars dictionary')
				print ('updated cars is: ',cars)
						
			print ('#####################################################################################################################')
			print ('#######################################end testing error catching####################################################')
			print ('#####################################################################################################################')

			for x in cars:	
				##need to figure out how to put ## in between spaces of x in cars if space exists
				##works: line2 = re.sub('==([\S\s]+)==',r'===\1===',line)
				xy = re.sub('##', ' ', x)	
				print ('** x is: ',x,' ** xy is: ',xy)
				lastverse = verselist[-1]
				print ('lastverse is: ',lastverse)
				#need to add the space before xy because otherwise it catches the term in larger words if it is a small word (eg. ah - padishah)
				# old way via replace, but this didn't have case insensitive option - verseupdated = lastverse.replace(xy, " ==" + xy + "== ",1)#replace(' ' + xy, " ==" + xy + "== ",1).replace(xy, " ==" + xy + "== ",1)
				#also needs to catch word boundary or parentheses (uses backreferences to replace parentheses in the right place)
				verseupdated = re.sub('((\\b)|(\()|(\{))' + xy, r"\1 ==" + xy + "==", lastverse, count=1, flags=re.I)
				print ('verseupdated: ',verseupdated)
				verseupdated2 = verseupdated.replace(xy,x)
				print ('verseupdated2: ',verseupdated2)
				verselist.append(verseupdated2)
				print ('verselist: ',verselist)
			# isolate suffix with regex so at end of script the isolated suffix can be moved back to right place
			#https://docs.python.org/3.5/library/re.html
			suffixisolate = re.sub('(?<=\S)==(?=\S)', '== @@%%', verseupdated2) #check to make sure this regex is right, is non-space really going to catch everything? seems to, catches string at beginning of line...
			print ('line 87', suffixisolate)
			print ()

			############### 4 - dealing with the isolated suffix (@@__), decided to insert it into the dictionary value list in position 0, so that when it can be re-attached later
			suffixisolatesplit = suffixisolate.split()
			#https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops
			for index, x in enumerate(suffixisolatesplit, start=0):
				#http://forums.devshed.com/python-programming-11/partial-match-search-list-python-661117.html
				if x.startswith("@@"):
					x_cleaned = re.sub('@', '#', x)
					print ('x_cleaned is: ','\"',x_cleaned,'\"')
					#https://stackoverflow.com/questions/17686809/how-to-find-word-next-to-a-word-in-python	
					previous_word_number = (index - 1)	
					print ('previous_word_number is: ',previous_word_number)
					previous_word = suffixisolatesplit[previous_word_number] #https://learnpythonthehardway.org/book/ex34.html
					print ('previous_word is: ',previous_word)
					previous_word_cleaned1 = re.sub('==', '', previous_word)
					print ('previous_word_cleaned1 is: ',previous_word_cleaned1)
					previous_word_cleaned = unicodedata.normalize('NFC',previous_word_cleaned1)
					print ('previous_word_cleaned is: ','\"',previous_word_cleaned,'\"')					
					#https://stackoverflow.com/questions/20585920/how-to-add-multiple-values-to-a-dictionary-key-in-python
					#https://stackoverflow.com/questions/21939652/insert-at-first-position-of-a-list-in-python
					#inserting suffix into list as beginning position
					cars[previous_word_cleaned].insert(0,x_cleaned)
					print ('line 111', cars)
					#generating the QA file
					#\\f##+##\\fr##GEN.1.1##İbtidâ##
					print ()

			############### 5 - create new list and isolate annotations with delimiters so that next for loop will catch annotation text, including ones that are multiple words
			#print ("suffixisolate is: ",suffixisolate)
			whitespacedelimit = suffixisolate.replace(r' ', r'##') #replace(r' @@',r'').
			print ('line 117', whitespacedelimit)
			print ()
			#print ("whitespacedelimit is: ",whitespacedelimit)
			isolatedannotations = whitespacedelimit.split("==")
			#https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings - removing empty string if exists at beginning of line caused when annotation exists as first word...
			#...whitespacedelimit regex fails because if annotation is at beginnging of line there is not space to add ##
			isolatedannotations2 = [x for x in isolatedannotations if x]
			print ('isolatedannotations2 is: ',isolatedannotations2)

			for key, value in cars.items():
				value2 = '##'.join(value)	
				cars[key] = value2

			############### 6 - 
			fixedverselist = None
			fixedverselist = []
			fixedverselist.append(isolatedannotations2)
			print ('line 133',fixedverselist)
			print ('line 135 cars is: ',cars)
			for y in cars:
				#normalization to composed not necessary for this for loop for some reason
				lastfixedverse = fixedverselist[-1]
				#https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python - list comprehension and the ternary operator
				#https://docs.quantifiedcode.com/python-anti-patterns/correctness/not_using_get_to_return_a_default_value_from_a_dictionary.html
				editedlist = [y + "##" + cars.get(y, "ERROR") if x==y else x for x in lastfixedverse]
				#editedlist = [y + "##" if x==y else x for x in lastfixedverse]
				#make note of places that normalized composed vs decomposed works - not sure if I should output y or xy in beginning of string above? - could also normalize to composed the whole document before/after script
				fixedverselist.append(editedlist)
				print ("line 140 y is: ",y,"fixedverselist is: ",fixedverselist)	
			#print ("fixedverselist is: ",fixedverselist)
			finallastfixedverse = fixedverselist[-1]
			print ("line 146 ",finallastfixedverse)
	
			############### 7 - 
			#https://stackoverflow.com/questions/493819/python-join-why-is-it-string-joinlist-instead-of-list-joinstring
			joinstring2 = (''.join(finallastfixedverse))
			joinstring = re.sub('####', '##', joinstring2)
			print ("line 151 ",joinstring)

			##### - what's left to do is reattach suffixes to morpheme: e.g. gėce (GEN.1.5)##@@dı needs to look like: gėcedı (GEN.1.5)##
			cleanedstring2 = re.sub('####', ' ', joinstring)
			cleanedstring1 = cleanedstring2.replace('##', ' ').replace(' %%','')
			print ("line 156 ",cleanedstring1)
			cleanedstring3 = re.sub(' @@\S+?(?=( )|(-))', '', cleanedstring1)
			cleanedstring4 = re.sub(' @@%%(\S*)?(?=\))', '',cleanedstring3)
			cleanedstring5 = re.sub(r'\\f\*-(\S)*', r'\\f*',cleanedstring4)
			cleanedstring = re.sub(' @@%%(\S*)?','',cleanedstring5)
			print ("line 157 ",cleanedstring)
			#final string:
			finalstring = versenum + ' ' + cleanedstring
			versenumcleaned = versenum.replace('##',' ')
			print ('finalstring is: ',finalstring)
			print ()
			with open(workfile,'a') as f:
				f.write(finalstring)
			print ('wrote to file')
		else:			
			print ('doesnt match')
			print (fileline)
			with open(workfile,'a') as f:
				f.write(fileline)
print ('finished')
with open(workfile,'r') as final:
	finalf = final.read()

finalf = re.sub(r' &&\\\p',r'\n\\p',finalf)
#finalf = re.sub(r'    ',r'   ',finalf)
finalfinalf = finalf.replace(r'==####',' ').replace(r'##',' ').replace(r'\\v**\\v',r'\v').replace('  ',' ').replace(r'\\mt**\\mt',r'\mt').replace(r'\mt 0',r'\mt').replace(r'{ ',r'{').replace(r'( ',r'(') #replace " \f" with "\f"
with open(workfile, 'w') as final:
	final.write(finalfinalf)


#QA 1665
##ROM.9.11 - takdîr==i needs to be corrected

#QA 1827
##Gen 14:1 tâʾife==leriŋ (not fixed in latest)
##ISA.1.24 Rabbü'l-ʿAsâkir==iŋ (not fixed in latest)
##HEB.10.22 yayka==nmış
##PRO.5.19 "letâfet " has extra space, needs to be deleted



############### find "\n\\p" replace: " \\\p"
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

