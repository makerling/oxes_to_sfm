#! /bin/bash
###############################transformations/conversions###########################################
#run this script which runs the xml to convert .oxes to .sfm, mimmicking the TE export to SFM
#need to install libsaxonb-java in ubuntu
#location of folder/files to process script:
folder=$(pwd)
output="output.sfm"
#source="joined1827allbooks.oxes"
#source="joined1665allbooks.oxes"
source="1827-GEN-June-27-2017_test_footnotes.oxes"
xslt="TE-Paratext-XSLT_main_text_conversion_and_annotations_v2_filtering_misc_categories.xsl"
#xslt="TE-Paratext-XSLT_main_text_conversion_and_annotations_v2.xsl"
#xslt="TE-Paratext-XSLT_main_text_conversion_and_annotations.xsl"
#remove wycliffe namespace, doesn't work otherwise
sed -i "s/ xmlns=\"http:\/\/www.wycliffe.net\/scripture\/namespace\/version_1.1.4\"//" "$folder"/"$source"
#transform .oxes to .sfm file
saxonb-xslt -o:"$folder"/"$output" -s:"$folder"/"$source" -xsl:"$folder"/"$xslt"
#removes white space
sed -i "s/^ *//" "$folder"/"$output"
#remove 1st line which is blank for some reason
sed -i "1d" "$folder"/"$output"
#remove last line which is blank for some reason
sed -i "$d" "$folder"/"$output"
gnome-open "$folder"/"$output"
