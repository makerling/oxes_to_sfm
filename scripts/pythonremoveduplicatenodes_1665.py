# -*- coding: utf-8 -*-
#for 1665 remove duplicate annotations (removing 2nd one, only some have exact notationDiscussion content)
import re
import xml.etree.ElementTree as ET

file = '/home/user/code/oxes_to_sfm/source/joined1665allbooks.oxes'
tree = ET.parse(file)

ref = 'JOL.1.9'
find = 'beyt-ullâh'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = '1SA.17.2'
find = 'cemʿ'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'ROM.3.27'
find = 'fahr'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'MAT.8.24'
find = 'fûrtuna'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'AMO.6.2'
find = 'Ġât'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'JOS.12.2'
find = 'Ġilʿâd'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'JHN.5.36'
find = 'hâlâ'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'HEB.9.14'
find = 'Hayy-Ullâh'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'PSA.74.21'
find = 'hicâb'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'DEU.13.13'
find = 'ihâlî'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'LUK.20.9'
find = 'iktirâ'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = '1PE.3.7'
find = 'kâb'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'ROM.12.2'
find = 'kanġı'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'HAB.1.12'
find = 'Kavî'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'LUK.20.21'
find = 'mâhiyyet'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = '1CO.4.5'
find = 'memdûh'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'PSA.87.4'
find = 'Mısr'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'EXO.21.19'
find = 'müberrâ'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = '2CO.11.7'
find = 'müften'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'JDG.20.7'
find = 'müşâvere'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'EZK.27.31'
find = 'nevha'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'ROM.16.20'
find = 'Selâmetiŋ Velîsi Allâh Teʿâlâ'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'LEV.0.0'
find = 'Sifr'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)
final = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
print ('all annotations in node:', final)


ref = 'EXO.14.17'
find = 'sipâh'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'LEV.22.5'
find = 'şul'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'LUK.1.25'
find = 'şul'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = '1PE.4.19'
find = 'tefvîz'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'EZR.6.2'
find = 'tezkîr'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'EXO.2.19'
find = 'vâfir'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'MAT.10.15'
find = 'yevmi\'d-dîn'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)


ref = 'DEU.4.6'
find = 'ʿâkil'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)

#need to do 3rd instead of second for this one because there are 3 matches
ref = 'LEV.0.0'
find = 'Leviyyîn'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 3:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)

#this is a nested annotation that needs to be removed
ref = '2CO.2.4'
find = 'efzûn'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
num = 0
#print ('all annotations in node:', test)
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		num = num + 1
		if num == 2:
			#print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2,' removing this second annotation')
			parents = tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/..')
			string = ('annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']')
			for parent in parents:
				parent.remove(parent.find(string))
		else:
			print ('x is: ', x)
			test2 = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"][' + str(idx) + ']/notationDiscussion/para/span')])
			print ('notationDiscussion is: ',test2)
#print ('finished: ', find)
#################################################################################
#################################################################################

ref = 'EXO.30.12'
find = 'benî İsrâʾîl'
replace = 'Benî İsrâʾîl'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)
		
ref = 'LEV.7.23'
find = 'benî İsrâʾîl'
replace = 'Benî İsrâʾîle'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

#not working, creating errors
#ref = 'NUM.6.2'
#find = 'Benî İsrâʾîl'
#replace = 'benî İsrâʾîle'
#test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#for idx,x in enumerate(test):
#	idx = idx + 1
#	if find in x:
#		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
#		tree.find(string).text = replace
#print ('finished: ', replace)

ref = '1SA.25.25'
find = 'nâbâl'
replace = 'Nâbâl'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = '1KI.1.1'
find = 'pes'
replace = 'Pes'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = '1KI.17.17'
find = 'hastelıḡı'
replace = 'hasteliḡi'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'EZR.6.22'
find = 'Âsûr Pâdişâh'
replace = 'Âsûr pâdişâh'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'JOB.14.1'
find = 'ʿavrat'
replace = 'ʿAvrat'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'PSA.57.1'
find = 'El-teshet'
replace = 'El-Teshet'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'PSA.57.1'
find = 'rahm'
replace = 'Rahm'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'ISA.14.28'
find = 'Âhâz Pâdişâh öldüḡü yıl'
replace = 'Âhâz pâdişâh öldüḡü yıl'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'JER.31.27'
find = 'Beyt-i İsrâʾîli ve Beyt-i Yahûdâyı'
replace = 'beyt-i İsrâʾîli ve beyt-i Yahûdâyı'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'DAN.9.24'
find = 'kudüs'
replace = 'Kudüs'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'MRK.10.52'
find = 'Var'
replace = 'var'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'MRK.11.17'
find = 'Mastûr'
replace = 'mastûr'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'LUK.7.24'
find = 'Beriyye'
replace = 'beriyye'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'ACT.9.15'
find = 'Var'
replace = 'var'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'ACT.22.21'
find = 'Var'
replace = 'var'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'ROM.10.20'
find = 'Beni aramayan kimselerden bulundum'
replace = 'beni aramayan kimselerden bulundum'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = '1CO.15.47'
find = 'İkinci Âdem'
replace = 'ikinci Âdem'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = '2CO.1.21'
find = 'mesîh'
replace = 'Mesîh'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'EPH.4.14'
find = 'tıfıl'
replace = 'tifil'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'HEB.1.7'
find = 'Ol ki meleklerini'
replace = 'ol ki meleklerini'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'HEB.13.20'
find = 'Selâmetiŋ Velîsi'
replace = 'selâmetiŋ velîsi'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

print ('replacing few misc')
with open(file, 'r') as oxesfile:
	filedata = oxesfile.read()
	fstrip = re.sub(r'<userCS type=\"Paragraph\">',r'',filedata)
	print ('finished fstrip1')	
	fstrip2 = re.sub(r'</userCS>',r'',fstrip)
	print ('finished fstrip2')	
	#fstrip3 = re.sub(r'<\/p>.*<p>.*<labelTr>.*<\/labelTr>\s<verseEnd.*ID=\"NUM.14.4\".*\/>','<verseEnd ID=\"NUM.14.4\" /></p><p>',fstrip2,flags=re.DOTALL)
	#print ('finished fstrip3')
	#fstrip4 = re.sub(r'<\/p>.*<\/section>.*<section>.*<sectionHead>.*<trGroup>.*<tr>On\sdokuzuncu\sbâb<\/tr>.*<\/trGroup>.*<\/sectionHead>.*<p>.*<verseEnd\sID=\"PRO.18.24\".*\/>.*<chapterEnd\sID=\"PRO.18\"\s\/>.*<\/p>','<verseEnd ID=\"PRO.18.24\" />\n<chapterEnd ID=\"PRO.18\" />\n</p>\n</section>\n<section>\n<sectionHead>\n<trGroup>\n<tr>On dokuzuncu bâb</tr>\n</trGroup>\n</sectionHead>\n<p>',fstrip3,flags=re.DOTALL)		
	#print ('writing file')

print ('done')

print ('writing')
tree.write(file, encoding="unicode", method="xml", xml_declaration=True)
print ('done')

#print
#final = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#print ('all annotations in node:', final)
