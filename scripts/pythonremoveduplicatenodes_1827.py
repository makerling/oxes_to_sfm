# -*- coding: utf-8 -*-
#for 1827 remove duplicate annotations (removing 2nd one, only some have exact notationDiscussion content)
import re
import xml.etree.ElementTree as ET

file = '/home/user/code/oxes_to_sfm/source/joined1827allbooks.oxes'
tree = ET.parse(file)

ref = 'EXO.34.28'
find = 'yemedin'
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
print ('finished: ', find)


#################################################################################
#################################################################################

#ref = 'GEN.8.21'
#find = 'min-baʿd'
#replace = 'Min-baʿd'
#test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#for idx,x in enumerate(test):
#	idx = idx + 1
#	if find in x:
#		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
#		tree.find(string).text = replace
#print ('finished: ', replace)

ref = 'GEN.11.8'
find = 'babel'
replace = 'Babel'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'GEN.24.5'
find = 'ol'
replace = 'Ol'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'EXO.12.50'
find = 'pes'
replace = 'Pes'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

#ref = 'EXO.19.24'
#find = 'var'
#replace = 'Var'
#test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#for idx,x in enumerate(test):
#	idx = idx + 1
#	print ('idx is: ',idx)
#	if find in x:
#		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
#		print ('string is: ',string)
#		tree.find(string).text = replace
#print ('finished: ', replace)

ref = 'EXO.23.18'
find = 'hamîr'
replace = 'Hamîr'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'LEV.17.3'
find = 'beyt-i İsrâʾîl'
replace = 'Beyt-i İsrâʾîl'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'NUM.1.1'
find = 'Benî İsrâʾîl'
replace = 'benî İsrâʾîl'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'DEU.16.18'
find = 'sıbt'
replace = 'Sıbt'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = '1KI.4.1'
find = 'melik'
replace = 'Melik'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = '1CH.17.16'
find = 'melik'
replace = 'Melik'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'EZR.7.27'
find = 'babalarımızıŋ Allâhı Rabb'
replace = 'Babalarımızıŋ Allâhı Rabb'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

#ref = 'NEH.7.65'
#find = 'akdes'
#replace = 'Akdes'
#test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#for idx,x in enumerate(test):
#	idx = idx + 1
#	if find in x:
#		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
#		tree.find(string).text = replace
#print ('finished: ', replace)

ref = 'JER.2.8'
find = 'Baʿâl'
replace = 'baʿâl'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'AMO.6.1'
find = 'Beyt-i İsrâʾîl'
replace = 'beyt-i İsrâʾîl'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'MIC.1.5'
find = 'Beyt-i İsrâʾîl'
replace = 'beyt-i İsrâʾîl'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'ZEC.8.4'
find = 'ʿasâ'
replace = 'ʿAsâ'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

ref = 'MAT.6.22'
find = 'cesed'
replace = 'Cesed'
test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
for idx,x in enumerate(test):
	idx = idx + 1
	if find in x:
		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
		tree.find(string).text = replace
print ('finished: ', replace)

#ref = 'MAT.27.9'
#find = 'otuz sikl güműşü aldılar'
#replace = 'Otuz sıkl güműşü aldılar'
#test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#for idx,x in enumerate(test):
#	idx = idx + 1
#	if find in x:
#		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
#		tree.find(string).text = replace
#print ('finished: ', replace)

#ref = 'ACT.3.11'
#find = 'revâk'
#replace = 'Revâk'
#test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#for idx,x in enumerate(test):
#	idx = idx + 1
#	if find in x:
#		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
#		tree.find(string).text = replace
#print ('finished: ', replace)

#ref = 'TIT.1.3'
#find = 'Hallâsımız Allâh'
#replace = 'hallâsımız Allâh'
#test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#for idx,x in enumerate(test):
#	idx = idx + 1
#	if find in x:
#		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
#		tree.find(string).text = replace
#print ('finished: ', replace)

#ref = '1PE.3.10'
#find = 'hayâtı sevmek ve íyỉ günler görmek isteyen'
#replace = 'Hayâtı sevmek ve íyỉ günler görmek isteyen'
#test = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#for idx,x in enumerate(test):
#	idx = idx + 1
#	if find in x:
#		string = ('.//annotation[@oxesRef=\"' + ref + '\"][' + str(idx) + ']/notationQuote/para/span')
#		tree.find(string).text = replace
#print ('finished: ', replace)

print ('done')

print ('writing')
tree.write(file, encoding="unicode", method="xml", xml_declaration=True)
print ('done')

#print
#final = ([test.text for test in tree.findall('.//annotation[@oxesRef="' + ref + '"]/notationQuote/para/span')])
#print ('all annotations in node:', final)
