# -*- coding: utf-8 -*-
#for 1827pythonoutput
import re
srcfile = '/home/user/code/oxes_to_sfm/workingdirectory/1827pythonoutput.sfm'

with open(srcfile, 'r') as file:
	filedata = file.read()
	fstrip = re.sub(r'-- selah','--selah',filedata)
	fstrip1 = re.sub(r'\[ ','[',fstrip)
	fstrip2 = re.sub(r'\)\)','\)',fstrip1)
#	fstrip3 = re.sub(r'- Hannân','-Hannân',fstrip2)
	fstrip3 = re.sub(r'anlamına gelen Sifr ü\'l-Mülûk el-evvel diye adlanılır\, 1. ','anlamına gelen Sifr ü\'l-Mülûk el-evvel diye adlanılır\, 1. ve 2. Samuel kitaplarının diğer adları 1. ve 2. ve 2. Krallar olduğu için bu karmaşıklığa uğraşılmıştır}',fstrip2)
	fstrip4 = re.sub(r'v 23 {bk.','v 23 {bk. 22. ayet}',fstrip3)		
	fstrip5 = re.sub(r'Osm metindeki 40:25-33 için bk.','Osm metindeki 40:25-33 için bk. 41:1-9}',fstrip4)

#	fstrip15 = re.sub(r've ola ki saŋa niçỉn âh ėdersin dėdikleri zamân de ki gelen haber içỉn ki','ve ola ki saŋa niçỉn âh \\\\f + \\\\fr EZK.21.7 âh 21:7 \\\\ft feryat, lanet ~ Fa. āh \\\\f* ėdersin dėdikleri zamân de ki gelen haber içỉn ki',fstrip14)
#	fstrip16 = re.sub(r'Ve Allâh Teʿâlâ Mûsâya dėdi firʿavna var da ȯŋa söyle ki ʿİbrânîleriŋ','Ve Allâh Teʿâlâ \\\\f + \\\\fr EXO.9.1 Allâh Teʿâlâ 9:1 \\\\ft İbr. YHWH (Yahweh) = O Var Olan\'dır. Ali Bey, İbr. Yahve\'yi genellikle "Allah Teâlâ" olarak yazmıştır (bk. Tevrat, Tekvin/Yaratılış 21:33; Huruc/Çıkış 3:14). \\\\f* Mûsâya dėdi firʿavna var da ȯŋa söyle ki ʿİbrânîleriŋ',fstrip15)


with open(srcfile, 'w') as file:
	file.write(fstrip5)
