# -*- coding: utf-8 -*-
#for 1665pythonoutput
import re
srcfile = '/home/user/code/oxes_to_sfm/workingdirectory/1665pythonoutput.sfm'

with open(srcfile, 'r') as file:
	filedata = file.read()
	fstrip = re.sub(r'-- selah','--selah',filedata)
	fstrip1 = re.sub(r'\[ ','[',fstrip)
	fstrip2 = re.sub(r'\)\)','\)',fstrip1)
	fstrip3 = re.sub(r'- Hannân','-Hannân',fstrip2)
	fstrip4 = re.sub(r'- Leviyyîn','-Leviyyîn',fstrip3)
	fstrip5 = re.sub(r'- Aʿdâd','-Aʿdâd',fstrip4)
	fstrip6 = re.sub(r'- müsennâ','-müsennâ',fstrip5)
	fstrip7 = re.sub(r'- ender-hatt','-ender-hatt',fstrip6)
	fstrip8 = re.sub(r'- ender-selâmda','-ender-selâmda',fstrip7)
	fstrip9 = re.sub(r'- ender-kat','-ender-kat',fstrip8)
	fstrip10 = re.sub(r'- Maʿmadânîniŋ','-Maʿmadânîniŋ',fstrip9)
	fstrip11 = re.sub(r'- Fenikî','-Fenikî',fstrip10)
	fstrip12 = re.sub(r'- Maʿmadânî','-Maʿmadânî',fstrip11)
	fstrip13 = re.sub(r'- Miġdalâniyye','-Miġdalâniyye',fstrip12)
	fstrip14 = re.sub(r'- mühlik','-mühlik',fstrip13)

	fstrip15 = re.sub(r've ola ki saŋa niçỉn âh ėdersin dėdikleri zamân de ki gelen haber içỉn ki','ve ola ki saŋa niçỉn âh \\\\f + \\\\fr EZK.21.7 âh 21:7 \\\\ft feryat, lanet ~ Fa. āh \\\\f* ėdersin dėdikleri zamân de ki gelen haber içỉn ki',fstrip14)
	fstrip16 = re.sub(r'Ve Allâh Teʿâlâ Mûsâya dėdi firʿavna var da ȯŋa söyle ki ʿİbrânîleriŋ','Ve Allâh Teʿâlâ \\\\f + \\\\fr EXO.9.1 Allâh Teʿâlâ 9:1 \\\\ft İbr. YHWH (Yahweh) = O Var Olan\'dır. Ali Bey, İbr. Yahve\'yi genellikle "Allah Teâlâ" olarak yazmıştır (bk. Tevrat, Tekvin/Yaratılış 21:33; Huruc/Çıkış 3:14). \\\\f* Mûsâya dėdi firʿavna var da ȯŋa söyle ki ʿİbrânîleriŋ',fstrip15)
	fstrip17 = re.sub(r'Allâh Teʿâlâdan bir haber işitdik','Allâh Teʿâlâdan \\\\f + \\\\fr OBA.1.1 Allâh Teʿâlâ 1:1 \\\\ft İbr. YHWH (Yahweh), \'O Var Olandır\' anlamına gelir (bk. Tevrat, Tekvin/Yaratılış 21:33; Huruc/Çıkış 3:14). Ali Bey, İbr. Yahve\'yi genellikle Ar. "Allah" veya "Allah Teâlâ" olarak yazmıştır. \\\\f* bir haber işitdik ',fstrip16)
	fstrip18 = re.sub(r'beriyyede imtihân gününde','beriyyede \\\\f + \\\\fr HEB.3.8 beriyye 3:8 \\\\ft çöl, kır ~ Ar. beriyye \\\\f* imtihân gününde',fstrip17)
	fstrip19 = re.sub(r'nâm şehrine çıkdı zîrâ o beyt ve âl-i Dâvûddan','nâm şehrine çıkdı zîrâ o beyt \\\\f + \\\\fr LUK.2.4 beyt 2:4 \\\\ft ev ~ Ar./İbr. bay(i)t \\\\f* ve âl-i Dâvûddan',fstrip18)
	fstrip20 = re.sub(r've on âdam bile Ahîkâm oğlu Ġadâliyâya Mispâya geldiler ve orada Mispâda','ve on âdam bile \\\\f + \\\\fr JER.41.1 bile 41:1 \\\\ft birlikte, beraber ~ Osm.Tü. bile &lt; E.Tü. birle &lt; bir + ile \\\\f* Ahîkâm oğlu Ġadâliyâya Mispâya geldiler ve orada Mispâda',fstrip19)
	fstrip21 = re.sub(r'karşᵼ komak içỉn cemʿ olan cemʿiyyetde','karşᵼ komak içỉn cemʿ \\\\f + \\\\fr NUM.27.3 cemʿ 27:3 \\\\ft çöl, kır ~ Ar. beriyye \\\\f* olan cemʿiyyetde',fstrip20)
	fstrip22 = re.sub(r'cemʿ olsun ve haziretiŋiz de cenge gidesin','cemʿ \\\\f + \\\\fr 2SA.17.11 cemʿ 17:11 \\\\ft toplama, toplanma ~ Ar. camʿ &lt; camaʿa = topladı, bir araya getirdi \\\\f* olsun ve haziretiŋiz de cenge gidesin',fstrip21)
	fstrip23 = re.sub(r'Hazret-i Mesîh o kadar efdal hizmete nâʾil','Hazret-i Mesîh o kadar efdal \\\\f + \\\\fr HEB.8.6 efdal 8:6 \\\\ft daha iyi, en faziletli ~ Ar. afḍal &lt; faḍl = fazla \\\\f* hizmete nâʾil',fstrip22)
	fstrip24 = re.sub(r'ben hâk ve hâkister','ben hâk \\\\f + \\\\fr GEN.18.27 hâk 18:27 \\\\ft toprak ~ Fa. ḫāk \\\\f* ve hâkister',fstrip23) 
	fstrip25 = re.sub(r've ikisi de bir lahm olalar şöyle ki artᵼk iki olmayalar illâ yek','ve ikisi de bir lahm \\\\f + \\\\fr MRK.10.8 lahm 10:8 \\\\ft et, beden ~ Ar. laḥm = insanın fiziksel varlığı \\\\f* olalar şöyle ki artᵼk iki olmayalar illâ yek',fstrip24)
	fstrip26 = re.sub(r'hem Yaʿkûbuŋ ve Yosēniŋ anası diḡer Meryem hem Zebedo','hem Yaʿkûbuŋ ve Yosēniŋ anası diḡer Meryem \\\\f + \\\\fr MAT.27.56 Meryem 27:56 \\\\ft İncil-i Şerif\'te Meryem adında bir kaç kadın var. Maġdalânlı ya da Mecdelli Meryem, Hz. İsa tarafından yedi kötü rûhu kovulup şifa bulmuş olan Meryem\'dir (bk. Luka 8:1-3).\\\\f* hem Zebedo',fstrip25)
	fstrip28 = re.sub(r've diḡer Meryem makbereyi görmeḡe geldiler idi','ve diḡer Meryem \\\\f + \\\\fr MAT.28.1 Meryem 28:1 \\\\ft İncil-i Şerif\'te Meryem adında bir kaç kadın var. Mecdelli Meryem, Hz. İsa tarafından yedi kötü rûhu kovulup şifa bulmuş olan Meryem\'dir (bk. Luka 8:1-3). \\\\f* makbereyi görmeḡe geldiler idi',fstrip26)
	fstrip29 = re.sub(r'pes onlarıŋ sözleri Hamora ve Hamor oğlu Seheme','pes \\\\f + \\\\fr GEN.34.18 pes 34:18 \\\\ft ondan sonra, ardınca, işte ~ Fa. pes (bağlaç) \\\\f* onlarıŋ sözleri Hamora ve Hamor oğlu Seheme',fstrip28)
	fstrip30 = re.sub(r'gelinceye dek Mısrıŋ karşᵼsında olan Sûra dek sâkin oldular','gelinceye dek Mısrıŋ karşᵼsında olan Sûra \\\\f + \\\\fr GEN.25.18 Sûr 25:18 \\\\ft \'Duvar, kale suru\' demektir. Şûr\'un Filistin ile Mısır arasındaki yolunda olduğu Hz. Hacer\'in seferinden bilinir (Tevrat, Tekvin/Yaratılış 20:1). Lübnan\'daki Sûr şehriyle karıştırılmamalı. Ancak Osm metinde yazılmış olan "Âsûr" ayetin başındaki Âsûr ile karıştırılmış olan bir müstensih hatasıdır. \\\\f* dek sâkin oldular',fstrip29)
	fstrip31 = re.sub(r'Sûrdan gidince tâ Mısır diyârına dek sâkin idiler','Sûrdan \\\\f + \\\\fr 1SA.27.8 Sûr 27:8 \\\\ft Lübnan\'daki Sûr şehri veya Filistin ile Mısır arasındaki Sûr (Şûr) kalesi kastedilmiş olabilir. \\\\f* gidince tâ Mısır diyârına dek sâkin idiler',fstrip30)
	fstrip32 = re.sub(r'âvâzını işitdim ve onlarıŋ ʿadedi ulûf ulûf rebavâtıŋ','âvâzını işitdim ve onlarıŋ ʿadedi ulûf ulûf \\\\f + \\\\fr REV.5.11 ulûf 5:11 \\\\ft binler ~ Ar. ulûf &lt; ʾelf = bin \\\\f* rebavâtıŋ',fstrip31)
	fstrip33 = re.sub(r'urup ȯnủ ve içinde olan her şeyʾi ve davarlarını','urup \\\\f + \\\\fr DEU.13.15 ur 13:15 \\\\ft E.Tü. ur- = vurmak, saldırmak \\\\f* ȯnủ ve içinde olan her şeyʾi ve davarlarını',fstrip32)
	fstrip34 = re.sub(r'sende ve davarlarıŋda ne ʿâkır ne','sende ve davarlarıŋda ne ʿâkır \\\\f + \\\\fr DEU.7.14 ʿâkır 7:14 \\\\ft kısır ~ Ar. ʿāḳir &lt; ʿuḳr/ʿaḳret = kısırlık (bk. Sami, s. 41) \\\\f* ne',fstrip33)

with open(srcfile, 'w') as file:
	file.write(fstrip34)
