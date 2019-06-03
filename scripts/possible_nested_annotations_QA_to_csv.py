# -*- coding: utf-8 -*-
#run using python 3 to handle unicode automatically
#rm -f workingdirectory/possible_nested_annotations_QA.csv && python3 scripts/possible_nested_annotations_QA_to_csv.py 2>&1 | tee -a workingdirectory/possible_nested_annotations_QA.csv
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
#create empty file for processing
Path(workfile).touch()
#with open(workfile, 'w') as clearfile:
	#print('clearing ' + workfile + ' file')
#strip newlines before \p then after script put them back
with open(srcfile, 'r') as file:
	filedata = file.read()
fstrip = re.sub(r'\n\\p','-\\p',filedata)
with open(srcfile, 'w') as file:
	file.write(fstrip)

with open(srcfile, 'r') as file:	
	for fileline in file:
		matchesv = re.match(r'\\\\v\*\*\\\\v \d+==[^#]', fileline)
		matchesmt = re.match(r'\\\\mt\*\*\\\\mt \d+==[^#]', fileline)
		#print ('#### verse or mt is ####: ',fileline)
		if matchesv or matchesmt:
			linesplit = fileline.split('==####')
			line2 = linesplit[0]
			line1 = line2.replace(' ','##').replace('\\\\','\\').replace('##-','## ')
			#print ('39 #### working line sfm file	####: ',fileline)
			#print ('40 #### verse spaces removed	####: ',line1)
			line = unicodedata.normalize('NFC',line1)
			versetext1 = linesplit[1]
			versetext2 = versetext1.rstrip('\n')
			versetext = unicodedata.normalize('NFC',versetext2)
			#print ()
			#print ('44 #### bare verse normalized	####: ',versetext)
			#sanitize variable - https://stackoverflow.com/questions/8237647/clear-variable-in-python
			cars = None
			#cars = dict(x.split('**') for x in line.split('==')) - old try, but makes values into str, needs to be list so I an append suffixes later
			#https://stackoverflow.com/questions/4627981/creating-a-dictionary-from-a-string - key thing here is the [v] which turns it into a list
			cars = dict((k, [v]) for k, v in (e.split('**') for e in line.split('==')))
			#only for debugging log			
			#print ('51 #### annots as dict keys	####: ', cars.keys())			
			newlist = []
			for key in cars:
			#	print (key, 'corresponds to', cars[key])
				newlist.append(key)
			#print ('newlist is: ', newlist).rstrip('\n')
			for x in newlist:
				for key in cars:
					if (x in key and x != key):
						#print ()
						#print ('60 #### nested annotation	####: ',x,' is nested in: ',key)
						nStr = versetext
						pattern = x
						count =0
						flag=True
						start=0
						while flag:
							a = nStr.find(pattern,start)  # find() returns -1 if the word is not found, 
										  #start i the starting index from the search starts(default value is 0)
							if a==-1:          #if pattern not found set flag to False
								flag = False
							else:               # if word is found increase count and set starting index to a+1
								count+=1        
								start=a+1
						#print('75 #### counting nested annots	####: ',x,'is found: ',count,' time(s) in verse')
						#getting the verse reference with regex
						m = re.search('[A-Z]{3}\.[0-9]+\.[0-9]+',fileline)
						if m:
							found = m.group(0)							
						#cleaning up list of annotations
						newlist2 = ' *** '.join(str(p) for p in newlist) 
						newlist3 = newlist2.replace('##',' ')
						newlist4 = newlist3.replace('\\v *** ','')
						newlist5 = newlist4.replace(' *** \\v','')						
						pattern2 = pattern.replace('##',' ')
						print(found,'@',count,'@',pattern2,'@nested term@',versetext,'@',newlist5)
			


