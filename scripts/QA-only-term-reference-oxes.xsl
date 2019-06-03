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
    <xsl:for-each select="//annotation">
	<xsl:if test="notationCategories/category != 'NoNote' and notationCategories/category != 'Misc'">
		<!--<xsl:value-of select="@oxesRef"/><xsl:text> #### </xsl:text><xsl:value-of select="notationQuote/para/span"/><xsl:text> #### </xsl:text><xsl:value-of select="./following-sibling::trGroup[1]/tr"/><xsl:text>&#x0A;</xsl:text> -->
	<xsl:value-of select="@oxesRef"/><xsl:text> </xsl:text><xsl:value-of select="notationQuote/para/span"/><xsl:text> </xsl:text><xsl:text>&#x0A;</xsl:text>
	</xsl:if>
    </xsl:for-each>
</xsl:template>
</xsl:stylesheet>
