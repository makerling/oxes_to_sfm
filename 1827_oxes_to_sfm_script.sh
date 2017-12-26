#! /bin/bash
###############################transformations/conversions###########################################
#run this script which runs the xml to convert .oxes to .sfm, mimmicking the TE export to SFM
#need to install libsaxonb-java in ubuntu
#location of folder/files to process script:
folder="/home/matthias/NetBeansProjects/TE-Paratext-XML/public_html/oxes-text-and-notes-to-SFM-June2017"
output="output.sfm"
source="1827-GEN-June-27-2017_test_footnotes.oxes"
#source="1827-June-27-2017.oxes"
xslt="TE-Paratext-XSLT_main_text_conversion_and_annotations.xsl"
#transform .oxes to .sfm file
saxonb-xslt -o:"$folder"/"$output" -s:"$folder"/"$source" -xsl:"$folder"/"$xslt"
#removes white space
sed -i "s/^ *//" "$folder"/"$output"
#remove 1st line which is blank for some reason
sed -i "1d" "$folder"/"$output"
#remove last line which is blank for some reason
sed -i "$d" "$folder"/"$output"
gnome-open "$folder"/"$output"
