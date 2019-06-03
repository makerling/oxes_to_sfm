<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
      version="2.0" exclude-result-prefixes="#all">
    <xsl:output method="text" encoding="UTF-8"/>
	<!--************************************************************************************************-->
	<!--* This stylesheet works on the output produced by FieldWorks Translation Editor, specifically the .oxes file.		*-->
	<!--* The oxesa file does not contain enough information to produce the fields needed by ParaTExt Translator's Notes. 	*-->
	<!--* Prior to running this conversion do the following:						*-->
	<!--* 1) Export the TE Project into Paratext. Make sure to leave annotations unchecked			*-->
	<!--* 2) The categories in TE need to be created as Note Tags in the Paratext project. The first 'To Do' tag should be kept.         *-->
	<!--* If a Note Tag is deleted make sure to change the numbering in the CommentTags.xml file so that they are sequential. 	*-->
	<!--* This ensures that the proper numbering is converted. 					*-->
	<!--* 3) The project needs to be exported as an oxes file in TE.					*-->
	<!--* 4) After the conversion, rename file to Comments_imported.xml and place in My Paratext Projects/Project folder   	*-->
	<!--* ***********************************************************************************************-->
	<!--* To make regexp matching work with different-but-equivalent encodings normalize-unicode function needs to be used.	*-->
	<!--* Because normalize-unicode function only works with 1 match, [1] has be specified in some or the arguments.	*-->
	<!--************************************************************************************************-->
<!-- The $categories variable is used to store the categories of TE as an index. These need to be typed in manually from the TE categories section (the ones that have been used in the project).-->
<xsl:variable name="categories" select="('To Do','GL-yer-ismi','GL-ozel-ad','GL-allah-ismi','GL-isa-ismi','TF-ilahiyat','TF-baglamdan','TF-KK-KM','OsmLugat','OsmLugat2','OsmLugat3','BTSozluk','BTSozluk2','BTSozluk3','NoNote','errata','baski-hatasi','terc-hatasi','osm-belirsiz','1665-Ali-Bey','ALINTI-OT','ANA-METiN','edebiyat','gramer','imla','Misc','1827-Kieffer')"/>
<xsl:template match="oxes">
    <xsl:for-each select="//annotation">
          
            <xsl:variable name="verseRef" select="@oxesRef"/>
            <!-- This variable stores the bare text of a verse with one trGroup paragraph node 
            this one for sure: annotation[@oxesRef="EXO.15.8"]/following-sibling::trGroup/tr
            -->
            <xsl:variable name="bareVerse" select="normalize-unicode(string-join((./preceding-sibling::verseStart[1]/@n, .[@oxesRef=$verseRef]/following-sibling::trGroup/tr), ' '))"/>
            <!-- This variable stores the text of a verse with one trGroup paragraph node as formatted in Paratext -->
            <xsl:variable name="VerseComplete" select="normalize-unicode(string-join(('\v', ./preceding-sibling::verseStart[1]/@n, .[matches(@oxesRef, $verseRef)]/following-sibling::trGroup[1]/tr), ' '))"/>
            <!-- This variable stores part of the verses after the paragraph split if it exists   -->
            <xsl:variable name="Verseand2ndPara" select="string-join((../../p[preceding-sibling::p/verseStart/@ID=$verseRef and 
                following-sibling::p/verseEnd/@ID=$verseRef]/trGroup/tr, ../../p[verseEnd/@ID=$verseRef]/trGroup[1]/tr), '\p ')"/>
            <!-- This variable is used to determine if the trGroup node has a paragraph tag in between the verseEnd node -->
            <xsl:variable name="acrossPara" select="../../p[verseStart/@ID=$verseRef and verseEnd/@ID=$verseRef]/verseEnd"/>
            <!-- This variable is used to store  the notationQuote word or words-->
            <xsl:variable name="selectedText" select="normalize-unicode(notationQuote/para/span[1])"/>

            <xsl:number value="position()" format="00000001"/><xsl:choose>
            <xsl:when test ="../../title">
                <xsl:value-of select="../../../@ID"/> 1:0<xsl:value-of select="$selectedText"/><xsl:text>&#x0A;</xsl:text>
            </xsl:when>
            <xsl:otherwise>
            <!-- Converts the verse reference from this format: GEN.1.1 to this format: GEN 1:1 -->
            <xsl:analyze-string select="normalize-space($verseRef)" regex="([A-Z1-3]+)\.([0-9]+)\.([0-9]+)">
                <xsl:matching-substring>
                    <xsl:value-of select="regex-group(1)"/>
                    <xsl:text> </xsl:text>
                    <xsl:value-of select="regex-group(2)"/>
                    <xsl:text>:</xsl:text>
                    <xsl:value-of select="regex-group(3)"/>
                </xsl:matching-substring>
            </xsl:analyze-string><xsl:value-of select="$selectedText"/><xsl:text>&#x0A;</xsl:text>
            </xsl:otherwise>
            </xsl:choose>
    </xsl:for-each>
</xsl:template>
</xsl:stylesheet>

<!--
========================================================================================
Revision History
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
13-Mar-2015    Stevan Vanderwerf created initial draft for Ottoman Transcription project
========================================================================================
-->
