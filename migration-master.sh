#! /bin/bash
#sets debugging
#set -x
###################
#### QA SCRIPT ####
###################
ABSOLUTEPATH="/home/user/code/oxes_to_sfm"

############################################################
#### find oxes file to transform to sfm, copy to source ####
############################################################
#for logging
LOGFILEOUTPUT=""$ABSOLUTEPATH"/workingdirectory/logfile"
{
echo
echo "******************************************************"
echo
if [[ $# -eq 0 ]] ; then echo "No project specificed in script. Place project number as parameter when you run the script. E.g. bash migration-master.sh 1665. Exiting..." ; exit 1 ; fi
PROJECTNUM="$1"

QUBESINCOMINGSRCFILE="/home/user/QubesIncoming/win7/joined"$PROJECTNUM"allbooks.oxes"
OXESSRCFILE=""$ABSOLUTEPATH"/source/joined"$PROJECTNUM"allbooks.oxes"

if [[ -f "$QUBESINCOMINGSRCFILE" ]] && [[ -f "$OXESSRCFILE" ]]
then 
	while true; do
	    read -p "source file found in Qubesincoming folder, do you want to overwrite the source folder oxes file with the file in Qubesincoming? (answer y or n)" yn
	    case $yn in
		[Yy]* ) mv "$QUBESINCOMINGSRCFILE" "./source/" && echo "moving and overwriting..."; break;;
		[Nn]* ) echo "keeping original file in project source folder, not overwriting"; break;;
		* ) echo "Please answer y or n.";;
	    esac
	done
elif [[ -f "$QUBESINCOMINGSRCFILE" ]] && [[ ! -f "$OXESSRCFILE" ]]
then
	echo "source file found in Qubesincoming folder, copying to source folder..."
	mv "$QUBESINCOMINGSRCFILE" "source/"
elif [[ ! -f "$QUBESINCOMINGSRCFILE" ]] && [[ -f "$OXESSRCFILE" ]]
then 
	echo "source file found in project source folder, continuing..."
elif [[ ! -f "$QUBESINCOMINGSRCFILE" ]] && [[ ! -f "$OXESSRCFILE" ]] 
then
	echo "source file not found in Qubesincoming folder, transfer it from win7 machine. Exiting..."
	exit 1
fi
##########################################
#### count how many notes/annotations ####
##########################################

echo
OXESANNOTTOTAL=$(pcregrep -o "<annotation" "$OXESSRCFILE" | wc -l)
OXESANNOTNONOTE=$(pcregrep -o "<category xml:lang=\"tr\">NoNote" "$OXESSRCFILE" | wc -l)
OXESANNOTMISC=$(pcregrep -o "<category xml:lang=\"tr\">Misc" "$OXESSRCFILE" | wc -l)
#finds number of annotations where notationCategories doesn't exist
OXESANNOTNONOTCAT=$(xmllint --shell "$OXESSRCFILE"<<< "xpath (//annotation[not(notationCategories)])" | grep -Po "(?<=content=)[A-Z]{3}\.\d+\.\d+" | wc -l)
#found edge case where nonote and misc are both indicated for same annotation so are counted twice but should only count once therefore adding it rather than subtracting
OXESANNOTNONOTMISCSAME=$(pcregrep -M "<notationCategories>\\n\\s+<category xml:lang=\"[a-z]+\">(Misc|NoNote)<\/category>\n\s+<category xml:lang=\"[a-z]+\">(Misc|NoNote)<\/category>" "$OXESSRCFILE" | grep notationCategories | wc -l)
OXESANNOTNUMB=$(($OXESANNOTTOTAL - $OXESANNOTNONOTE - $OXESANNOTMISC - $OXESANNOTNONOTCAT + $OXESANNOTNONOTMISCSAME))
echo "Total Annotations to process: $OXESANNOTNUMB"

##################################################################
# cleanup commands // run python and XSLT transform scripts   ####
##################################################################

echo
echo "Initial transformation from .oxes to .sfm..."
#remove wycliffe namespace, doesn't work otherwise
sed -i "s/ xmlns=\"http:\/\/www.wycliffe.net\/scripture\/namespace\/version_1.1.4\"//" "$OXESSRCFILE"
#combine some tags per Steve Woodard
sed -i "s/OsmLugat2/OsmLugat/" "$OXESSRCFILE"
sed -i "s/OsmLugat3/OsmLugat/" "$OXESSRCFILE"
sed -i "s/BTSozluk2/BTSozluk/" "$OXESSRCFILE"
sed -i "s/BTSozluk3/BTSozluk/" "$OXESSRCFILE"
#removing following character sequence so it doesn't conflict with python script
sed -i "s/==//g" "$OXESSRCFILE"

#run pythonremoveduplicatenodes_1665.py
OXESDUPANNOTSREMOVE=""$ABSOLUTEPATH"/scripts/pythonremoveduplicatenodes_"$PROJECTNUM".py"
#only working for 1665 now
echo "running pythonfindreplacenodes_$PROJECTNUM"
python3 "$OXESDUPANNOTSREMOVE"

SFMOUTPUT=""$ABSOLUTEPATH"/workingdirectory/sfmoutput"$1"_1.sfm"
XSLT=""$ABSOLUTEPATH"/scripts/TE-Paratext-XSLT_main_text_conversion_and_annotations_v2_filtering_misc_categories_forannotationQA.xsl"
##XSLT transformation - need to install libsaxonb-java in ubuntu
saxonb-xslt -o:"$SFMOUTPUT" -s:"$OXESSRCFILE" -xsl:"$XSLT"

SFMOUTPUT2=""$ABSOLUTEPATH"/output.xml"
XSLT2=""$ABSOLUTEPATH"/scripts/TE-Paratext-XSLT_test.xsl"
##XSLT transformation - need to install libsaxonb-java in ubuntu
saxonb-xslt -o:"$SFMOUTPUT2" -s:"$OXESSRCFILE" -xsl:"$XSLT2"

#more cleanup after transformation script
#removes white space
sed -i "s/^ *//" "$SFMOUTPUT"
#remove 1st line which is blank for some reason
sed -i "1d" "$SFMOUTPUT"
#remove last line which is blank for some reason
sed -i "$d" "$SFMOUTPUT"
#gnome-open "$SFMOUTPUT"
echo

##########################################################
# in new file count how many annotations/notes it has ####
##########################################################

SFMANNOTNUMB=$(pcregrep -o ".\\\\f \+ \\\\fr" "$SFMOUTPUT" | wc -l)
SFMANNOTMISSING=$(($OXESANNOTNUMB - $SFMANNOTNUMB))
echo "Total Annotations in .sfm file: $SFMANNOTNUMB"
echo "Total Annotations not in .sfm file: $SFMANNOTMISSING"
echo

##################################################
# compare old and new to see if numbers match ####
##################################################

#create comparison file .oxes
SFMSORTEDDIFFOUTPUT=""$ABSOLUTEPATH"/workingdirectory/sfmoutput"$1"_1_sortedfordiff.sfm"
cat "$SFMOUTPUT" | uconv -x Any-NFC | pcregrep -o "(?<=\\\\f \+ \\\\fr )[A-Z0-9]{3}\.\d+\.\d+ .+?(?=\d)" | sort -t " " -k2 -k1 > "$SFMSORTEDDIFFOUTPUT"

#create comparison file .oxes
OXESDIFFOUTPUT=""$ABSOLUTEPATH"/workingdirectory/oxesoutput"$1"_1_sortedfordiff.sfm"
OXESDIFFXSLT=""$ABSOLUTEPATH"/scripts/QA-only-term-reference-oxes.xsl"
OXESDIFFOUTPUT=""$ABSOLUTEPATH"/workingdirectory/oxesoutput"$1"_1_fordiff.sfm"
OXESSORTEDDIFFOUTPUT=""$ABSOLUTEPATH"/workingdirectory/oxesoutput"$1"_1_sortedfordiff.sfm"
saxonb-xslt -o:"$OXESDIFFOUTPUT" -s:"$OXESSRCFILE" -xsl:"$OXESDIFFXSLT"
cat "$OXESDIFFOUTPUT" | uconv -x Any-NFC | sort -t " " -k2 -k1 > "$OXESSORTEDDIFFOUTPUT"

################################################################
# run QA scripts to identify which ones aren't being caught ####
################################################################

#nested annotations only 0 and 1 are probably nested, 2+ probably not
QANESTEDANNOTATIONSCHECK=""$ABSOLUTEPATH"/workingdirectory/"$1"possible_nested_annotations_QA.csv"
QANESTEDANNOTATIONSSCRIPT=""$ABSOLUTEPATH"/scripts/possible_nested_annotations_QA_to_csv.py"
#rm -f "$QANESTEDANNOTATIONSCHECK"
#python3 "$QANESTEDANNOTATIONSSCRIPT" "$PROJECTNUM" > "$QANESTEDANNOTATIONSCHECK"

#running script to determine to identify the annotations that aren't being matched with the verse for various reasons
#reasons: misspelling, duplicate same annotations, nonexisting text to match up with annotation, double nested annotations (valid need to do manually)
#QAUNMATCHEDANNOTATIONS=""$ABSOLUTEPATH"/scripts/QA_script_to_find_unmatched_annotations.py"
QAUNMATCHEDANNOTATIONS=""$ABSOLUTEPATH"/scripts/oldpythonscript_template_works_beginnging_end_updated.py"
rm -fr workingdirectory/oldpythonscript_template_works_beginnging_end_updated_log && python3 "$QAUNMATCHEDANNOTATIONS" "$PROJECTNUM" > workingdirectory/oldpythonscript_template_works_beginnging_end_updated_log
PYTHONSFMANNOTNUMB=$(grep -o "\\\f + \\\fr" ""$ABSOLUTEPATH"/workingdirectory/"$1"pythonoutput.sfm" | wc -l)
MISSINGANNOTS=$(($OXESANNOTNUMB - $PYTHONSFMANNOTNUMB))
PYTHONSFMSORTEDDIFFOUTPUT="/tmp/pythonsfmoutput"$1"sortedfordiff.sfm"
UNMATCHEDANNOTATIONS="/tmp/"$1"unmatchedannotations.txt"
UNMATCHEDANNOTATIONSWITHVERSE=""$ABSOLUTEPATH"/workingdirectory/"$1"unmatchedannotationswithverse.txt"
#comparing and sorting unmatched annotations into a list
cat ""$ABSOLUTEPATH"/workingdirectory/"$1"pythonoutput.sfm" | uconv -x Any-NFC | pcregrep -o "(?<=\\\\f \+ \\\\fr )[A-Z0-9]{3}\.\d+\.\d+ .+?(?=\d)" | sort -t " " -k2 -k1 > "$PYTHONSFMSORTEDDIFFOUTPUT"
comm -3 <(sort "$PYTHONSFMSORTEDDIFFOUTPUT") <(sort "$SFMSORTEDDIFFOUTPUT") | sort -t " " -k2 > "$UNMATCHEDANNOTATIONS"
#need to convert file to UTf8 or grep doesn't work
SFMOUTPUTUTF8="/tmp/sfmoutput"$1"_1.sfm"
cat "$SFMOUTPUT" | uconv -x Any-NFC > "$SFMOUTPUTUTF8"
#output final list of terms,references,and verse text with all \p
cat "$UNMATCHEDANNOTATIONS" | uconv -x Any-NFC | while read line; do echo "line is: $line" ; grep "$line" "$SFMOUTPUTUTF8" ; echo "**********************"; done > "$UNMATCHEDANNOTATIONSWITHVERSE"

formatting for csv
rm -rf "$UNMATCHEDANNOTATIONSWITHVERSE".csv
cat "$UNMATCHEDANNOTATIONS" | uconv -x Any-NFC | while read line
do
	ref=$(echo "$line" | cut -d " " -f 1 | sed 's/\t//')
	annot=$(echo "$line" | cut -d " " -f 2-)
	versetext=$(grep "$line" "$SFMOUTPUTUTF8" | pcregrep -Mo "(?<===####).*$")
	allannots=$(grep "$line" "$SFMOUTPUTUTF8" | pcregrep -Mo '(?<===).+?(?=\*\*)' | tr '\n' '*')
	dups=$(grep "$line" "$SFMOUTPUTUTF8" | pcregrep -Mo '(?<===).+?(?=\*\*)' | sort -u | wc -l)
#	dupsargument=$(if [ $allannotsnum -ne $dups ] ; then echo "$annot exact duplicate" ; fi)
	nested=$(echo $allannots | tr '*' '\n' | sort -u | while read annotterm; do nestedannotsnum=$(echo "$allannots" | grep -io "$annotterm" | wc -l); if [ $nestedannotsnum -eq 2 ] ; then echo "$annotterm found nested another annotation in $allannots: $nestedannotsnum"; fi ; done )  

	touch "$UNMATCHEDANNOTATIONSWITHVERSE".csv
	echo "$ref,$annot,$versetext,$allannots,$dupsargument,$nested" >> "$UNMATCHEDANNOTATIONSWITHVERSE".csv
done
gnome-open ""$UNMATCHEDANNOTATIONSWITHVERSE".csv"

#gedit code for find/replace all footnotes
# \\f \+ \\fr [A-Z0-9]{3}\.\d+\.\d+ .+?(?=\d)\d+:\d+( |( \\ft)).*?\\f\*

# 1 delete reference from footnotes:
#(\\fr )([A-Z0-9]{3}\.\d+?\.\d+?\s)  - replace with \1
#new find/remove all footnotes regex minus reference (because of regex above)
# \\f \+ \\fr .+?(?=\d)\d+:\d+( |( \\ft)).*?\\f\*
# 2 switch reference and annot term in footnote
#((?<=\\fr).*?(?=\s\d+:))(\s\d+:\d+(?=\s\\ft)) (replace with \2\1
# 3 find all annotation terms and put \fk marker in front of them to separate from footnote reference
#(?<=\\fr)(\s\d+\:\d+) replace with: "\1 \\\fk" (make sure to do with \e too)
# 4 change 0:0 to 1:0
#find: "(\\fr) 0\:0" replace with: "\1 1:0"
# 5 remove space between \f + \fr and annotation term
#"(\s)(\\f \+ \\fr)" - replace with "\2"


#for 1819 in sfm file few changes after initial regex:
#"ve ol ʿavrat Yûnâniyye Sîro- Fenikî" needs to be "ve ol ʿavrat Yûnâniyye Sîro-Fenikî"
#"(Mâkabl + Ali Bey'in parafı))" needs to be "(Mâkabl + Ali Bey'in parafı)"
#\v 4 hem birbirine dėdiler ki eş bir baş dikelim de Mısra dönelim
#\v 5 needs to be: 
#\v 4 hem birbirine dėdiler ki eş bir baş dikelim de Mısra dönelim
#\p
#\v 5
#
#

#JHN.6.69 [el hayy]
#ACT.15.11 Rabb ʿİsâ [el-Mesîh
#REV.1.8 elif ve ye [ibtidâ ve intihâ] benim

#adding corrections to hyphenated prefixes and manual nested annotations
MANUALNESTEDANNOTS=""$ABSOLUTEPATH"/scripts/pythonfindreplacenodes_"$PROJECTNUM"sfm.py"
#only working for 1665 now
echo "running pythonfindreplacenodes_$PROJECTNUMsfm"
python3 "$MANUALNESTEDANNOTS"

#final unicode normalization of file: 
cat ""$ABSOLUTEPATH"/workingdirectory/"$1"pythonoutput.sfm" | uconv -x Any-NFC > ""$ABSOLUTEPATH"/workingdirectory/"$1"pythonoutput_FINAL.sfm"

#check on Sîro-Fenikî Mark 7:26
#what about  &lt;?

##############
# logging ####
##############

} 2>&1 | tee -a "$LOGFILEOUTPUT"
#adding date stamps to logfile
cat "$LOGFILEOUTPUT" | sed -e "s/^/$(date -R) /" >> "$LOGFILEOUTPUT".log
rm -f "$LOGFILEOUTPUT"


