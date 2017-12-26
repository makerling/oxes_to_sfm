<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    version="2.0" exclude-result-prefixes="#all">
      <!--removed namespaces from oxes file, need to add these back for final version xmlns:oxes="http://www.wycliffe.net/scripture/namespace/version_1.1.4"
      xpath-default-namespace="http://www.wycliffe.net/scripture/namespace/version_1.1.4"-->      
    <xsl:output method="text" encoding="UTF-8" indent="no"/>
    <!-- remove whitespace currently bash script does \\ some notationCategories missing in TE, find them with this regex: "<resolved />\n +?<notationQuote"
    \\ need to edit 3 places which are caused by bk. creating an extra line/paragraph break: Job40:24 add "41:1-9}" and NEH.4.23 add "22. ayet} ∞ " 
    and 2SA.24.25 add " ve 2. Samuel kitaplarının diğer adları 1. ve 2. Krallar olduğu için bu karmaşıklığa uğraşılmıştır.}"    \\ 
    winmerge finds 5 remaining differences - some \m - \p paragraph continuation - tags instead of \p tags, I think these are just mistakes, also 1 section of mixup between \c \s \p, 
    but I think this is a just a mistake too " -->
<xsl:template match="oxes">
    <xsl:for-each select="oxesText/canon/book">
        \id <xsl:value-of select="@ID"/>
        \h <xsl:value-of select="titleGroup/@short"/>
        \mt <xsl:value-of select="titleGroup/title/trGroup/tr"/>
        <xsl:for-each select="section">
            <xsl:if test="p/chapterStart">
                \c <xsl:value-of select="p/chapterStart/@n"/>             
            </xsl:if>
            <xsl:if test="sectionHead">
                <xsl:for-each select="sectionHead"><!--\s needs to be outside of under \p processing to catch areas that have multiple \s and Psa 119-->
                    \s <xsl:value-of select="trGroup/tr"/>
                </xsl:for-each>
            </xsl:if>          
            <xsl:for-each select="p"><!--puts \p tags but avoids trGroups without verseStart i.e Psalms, or \p nodes where trGroup is the first element, those are done manually below (line 33)-->
                <xsl:if test="verseStart and name(./*[1]) = 'verseStart' or name(./*[1]) = 'verseEnd' or name(./*[1]) = 'chapterStart'">
                    \<xsl:value-of select ="name(.)"/>
                </xsl:if>
                <xsl:for-each select="./*"><!--for loop on each node under \p-->
                    <xsl:variable name="nodePosition2" select="position()" /><!--variable to catch position of nodes under \p-->
                    <xsl:if test="name(.) = 'trGroup' and $nodePosition2 = 1"><!--catching \p nodes where trGroup is first node, i.e a verse spanning multiple paragraphs, or only node-->
                        \p<xsl:text> </xsl:text><xsl:value-of select="tr"/>
                    </xsl:if>
                    <xsl:if test="name(.) = 'verseStart'"><!--finds verse number and the following first sibling of the first trGroup, the rest of the verse gets handles by line 33-->
                        <xsl:variable name="versenumb" select="@ID" /><!--reserving versenum to only process annotation for current verse-->
                        \v <xsl:value-of select="@n"/>
                        <xsl:text> annotation:**</xsl:text>
                        <xsl:for-each select="../*">
                            <!--versenumb is:<xsl:value-of select="$versenumb"/> oxesRef is:<xsl:value-of select="@oxesRef"/>-->
                            <xsl:if test="@oxesRef=$versenumb"> 
                                <xsl:value-of select="$versenumb"/>*<xsl:value-of select="notationQuote/para/span"/><xsl:text>**</xsl:text>
                            </xsl:if>
                        </xsl:for-each>
                        <xsl:text>** </xsl:text>
                        <xsl:value-of select="./following-sibling::trGroup[1]/tr"/>
                    </xsl:if>
                </xsl:for-each>
            </xsl:for-each>
        </xsl:for-each>
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