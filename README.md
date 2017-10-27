# END Dataset Documentation

[About the Project](#about-the-project)<br>
[END Custom MARC Schema](#end-custom-marc-schema)<br>
[Tutorial and Visualization Demos](#tutorial-and-visualization-demos)

#### About the Project
Early works of fiction often have detailed title pages, plot summaries, complex tables of contents, lengthy titles and endnotes, and elaborate prefaces. The [Early Novels Database (END) project](http://www.earlynovels.org) creates rich bibliographic metadata that captures these features in fields that enable new forms of research on English-language fiction of the long eighteenth century. 

<br>
<img src="https://github.com/earlynovels/end-dataset/blob/master/Tutorial%20Images/END%20Title%20Page%20Pic.png" alt="Shows a photo of title page with various fields labeled by name, such as title, illustration, etc." width="500">
<br>

#### About the Dataset
The Early Novels Dataset contains bibliographic metadata for early works of fiction held in the [Collection of British and American Fiction, 1660-1830 (CBAF)](http://franklin.library.upenn.edu/search.html?filter.author_creator_facet.val=Collection%20of%20British%20and%20American%20Fiction%2C%201660-1830%20%28University%20of%20Pennsylvania%29) at the University of Pennsylvania’s [Kislak Center for Special Collections, Rare Books and Manuscripts](http://www.library.upenn.edu/kislak/), as well as other regional repositories. It consists of MARC catalog records enriched with custom subfields designed to offer new kinds of structured data about early fiction in English. 

The END dataset is comprised of high-quality, human-generated metadata that captures a much fuller range of edition- and copy-specific information about early novels than traditional library catalog records. The END metadata schema builds on library-standard MARC records with custom-designed subfields that use both controlled and discursive vocabularies to describe a range of bibliographic features outside the scope of traditional cataloging. These include important bibliographic details such as authority statements, full and half title, accurate and controlled place of publication, and edition statement. They capture both copy-specific information about marginalia, inscriptions, and bookplates as well as title-level data on narrative form. And finally, they record the presence of important paratextual features like authors’ notes, epigraphs, footnotes, and indices, which can be found in many works of early fiction but have never been cataloged in a systematic way that would enable faceted search across a corpus. 

As of September 2017, the complete Early Novels Dataset totals 2,041 records. The core eighteenth-century subset consists of 1,325 records, which represent all of Penn Libraries’ Collection of British and American Fiction holdings published from 1700-1794 and a sampling of holdings published from 1795-1799. The core eighteenth-century subset consists of 1094 records, which represents all of Penn Libraries’ Collection of British and American Fiction holdings published between 1700 and 1789. A sample comparison of the CBAF holdings from the decade of the 1760s with all known fiction in English published during this period suggests that Penn's collection represents approximately 14% of this total corpus. In the core 1700-1789 END dataset, Penn holdings are supplemented by selected holdings from other Philadelphia-area and regional repositories, including the Library Company of Philadelphia, the Rosenbach, the Swarthmore Libraries Rare Book Room, Bryn Mawr College Special Collections, and New York University's Fales Library.

#### Background on the Collection
Penn Libraries’ Collection of British and American Fiction is comprised of nearly three thousand works of early fiction in English. Its core is the Singer-Mendenhall Collection, built through the combined efforts of University of Pennsylvania graduate student Godfrey F. Singer and professor John C. Mendenhall in the first half of the twentieth century. The collection is notable for its has particular stregnths in epistolary fiction, It is notable for its strength in epistolary fiction  and  focused their collecting efforts on epistolary fiction, and the Singer-Mendenhall collection today has particular strengths in non-canonical epistolary fiction by female and anonymous authors. 

#### How to Explore the Dataset
There are several ways to explore the END dataset. The most complete version of END data is encoded in a standard library record format called MARCXML. For ease of use, END data is also available in tabular subsets, which are designed to allow in-depth exploration of a number of specific features. This section will provide an overview of the two data formats and some of the ways you might work with either the full.xml file or the .tsv subsets we provide.

### Guide to Tabular Subsets 
The full.tsv file available here is a pared-down version of the complete END dataset. It includes a curated selection of the data categories we envision as most relevant for most users, and is intended to provide an overview of the kinds of information END records make available. For instance, while the complete END dataset includes detailed information about 41 separate kinds of paratexts (that is, textual matter appended to the main text), most of our paratextual data falls within the top seven categories: Preface, Dedication, Advertisement, To the Reader, Introduction, Note, and Footnote. The full.tsv indicates whether any given record has information in these seven categories, and users interested in delving deeper can turn to the tabular subsets devoted exclusively to paratexts. These targeted subsets offer a more complete version of our data for these categories. 

In addition the full.tsv and the associated tabular subsets that offer detailed information about each category of paratext, we have also broken down the data by period to enable users to examine the eighteenth and nineteenth centuries separately. So while the full.tsv contains records for works published as early as 1660 and as late as 1853, you can choose the 18c-full.tsv to look only at records published from 1700-1799, and the 19c-full.tsv for records with publication dates from 1800-1853. We also offer the full range of paratextual subsets broken down by eighteenth and nineteenth centuries. 

The simplest ways to open and view our .tsv files will most likely be Google Sheets or Microsoft Excel. For either, simply open the file and choose "tab" when you are prompted for the delimiter. 

###Explore .tsv subsets with Excel Pivot Tables
See our Excel Pivot Tables tutorial below for a demonstration of how you might begin to explore the data. [Note, however, that it is using data categories not included in our full.tsv; you can simply choose different column headers to work with.]

###Explore .tsv subsets with Google Fusion Tables
If you are interested in using Google Fusion Tables to explore END data, one place to start is END PI Rachel Buurma's digital assignment[ rise-2017/Assignments/Rise_assignment_6.md ] for the students in her Rise of the Novel course at Swarthmore College. 

###Work with MARCXML in OpenRefine
Below are instructions for importing and exporting our full.xml file in OpenRefine. Doumentation and tutorials for using OpenRefine are widely available. 

#IMPORT into MarcEdit/OpenRefine
[1]MarcEdit
[2]MarcTools [MARCXML=>MARC]
make sure output path is selected (*.mrc)
choose UTF8 encoding
no translation selected
[3]MarcEdit main menu
Tools -> OpenRefine -> Export Data to
rename output *.tsv
OpenRefine
choose *.tsv file
make sure everything interpreted as strings
deselect (if selected) quotation around columns with escaped characters

#EXPORT from OpenRefine/MarcEdit
OpenRefine / export -> tab-separated values
MarcEdit / tools -> openrefine -> import data from …
select output path *.mrc
MARC Tools /
input / openrefine import *.mrc file
output / *.xml output path
select MARC => MARCXML
UTF8 encoding

###Transform MARCXML into Custom Tabular Data

##With MarcEdit
For a thorough introduction to MarcEdit in the context of research applications of library record data, a great place to start is this [screencast tutorial](http://pastispresent.org/2015/digital-humanities-2/converting-marc-records-to-a-spreadsheet-a-screencast-tutorial/) by Molly Hardy, the Director for Digital and Book History Initiatives at the American Antiquarian Society. There are many other tutorials and extensive documentation for MarcEdit available online. 

##With Pymarc
We have included here the working Pymarc scripts developed by END collaborator and Swarthmore Libraries Digital Initiatives Librarian Nabil Kashyap. These are working files not intended for use beyond the very specific and idiosyncratic MARCXML of the END dataset. We provide them solely as models for how you might use Pymarc to extract particular information from END MARCXML fields and subfields.  

###Pair END Data with Fulltext for Topic Modeling
While END’s primary focus is metadata, we are also in the preliminary stages of a fulltext initiative for the CBAF novels digitized by Penn Libraries and available through Print at Penn. We have created fulltext files for each of these texts using OCR; cleanup work is ongoing, both computationally and through hand-correcting. The fulltext is available in our digital-collection repostiory. We have also worked with Penn Libraries' Digital Humanities Specialist Scott Enderle to experiment with topic modeling of this fulltext combined with END metadata. Work-in-progress can be found in our [earlynovels-topic-model repository](https://github.com/earlynovels/earlynovels-topic-model), and Scott's enhanced Topic Modeling Tool, which enables pairing fulltext with metadata, can be found [here](https://github.com/senderle/topic-modeling-tool). 

****

### END Custom MARC Schema
The MARC schema was designed specifically for bibliographic metadata, and when it is encoded as XML, it is the data format that most online library catalogs use. END records build on standard MARC library catalog records by adding custom, nonstandard MARC subfields that allow entirely new kinds of information to be collected. For information on the structure of standard MARC records, see the [Library of Congress MARC 21 schema](https://www.loc.gov/marc/bibliographic/), as well as the [Library of Congress guidelines for working with MARCXML](https://www.loc.gov/standards/marcxml/). 

An explanation of the custom END MARC schema, including both standard and nonstandard subfields, can be found below. 

#### 000 Fields - Bibliographic Data 
Derived from base catalog records, mostly from Penn Libraries OPAC. Not all END records are built on top of base records, however, so in some END records only the 001 field is present. <br>

- 001: END Control Number: Control numbers in the 001 field follow different systems depending on the year in which the work was cataloged, but all are unique. Each record in the dataset has a unique identifier. 
  - All records cataloged to 2013 have randomly-generated sequential ID numbers in the 001 field. Most from Penn include Franklin BibIDs are included in the 035 field, but many do not include OCLC numbers. These were cataloged from several different institutions: Penn RBML (now Kislak), Swarthmore College, Bryn Mawr, Library Company, etc.
  - All records cataloged in the summer of 2014 were cataloged in google sheets and converted to XML. They are missing some of the automated fields that are present in the records that used Franklin catalog records as base entries. They have been remediated to have ID numbers in the 001 field, these follow the sequential schema of the voyager records from 2013 and before.
  - Records cataloged from the summer of 2015 and from the 2015-2016 academic year have Franklin BibIDs in the 001 field. Duplicate BibIDs are denoted with a -1 -2 etc.
  - Records cataloged during the summer of 2016 at Penn have Franklin BibIDs in the 001 field. They also have Franklin back-end holdings numbers in the 035 field (not among metadata imported from Franklin--these had to be pulled from the holdings database and collated to individual copies).
  - Records cataloged during the summer of 2016 at NYU have OCLC numbers in the 001 field.
- 008: Publication Date
  - Publication date for record is in 008 field, positions[bytes] 7-10. In this example,"1813" is the pub date:
    ```
    <marc:controlfield tag="008">860203s1813        enk               00001 >eng d</marc:controlfield>
    ```
  - Single pub dates are designated with an “s” in position/byte 6. A pub date range is designated with an “m” in position/byte 6. In this example, “1816-1817” is the pub date range:
    ```
    <marc:controlfield tag="008">851011m18161817enkc              00010aeng d</marc:controlfield>
    ```
  - To sort on pub date, pull only the first date in positions/bytes 7-10. 
- 035: System Control Number (local control numbers - usually Penn BibID, Call Number, OCLC, etc. Not all records have entries in the 035 field.)
- 040: Location ID (For records with Franklin base entries, this is PU, MARC organization code for University of Pennsylvania)
- 041: Language code
$a language of the text (eng for English)
$h language of the original text (if translated)
- 043: Geographic area code
- 090: Locally-assigned call number (Obsolete--not part of standard MARC 21 Bibliographic format)

#### 100 Fields - Standardized author/title information (Derived from base catalog records)
- 100: Author name
$a Last Name, First Name
$c Title (EX: Sir, Dr., etc)
$d dates of birth and death
- 130: Uniform Title

#### 200 Fields - Title Data (Derived from base catalog records)
- 245: Title as cataloged <br>
$a Title <br>
$b Subtitle<br>
$c Statement of Responsibility<br>
$n Number of part/section of work

- 246: Title as it appears on title page (there is a separate 246 field for each title page in the work; for instance, a seven-volume novel with a full title page in each volume would have seven repeating 246 fields)<br>
$a Direct transcription of title as it appears on title page, including all punctuation, volume information (e.g. “Vol. I”, “In two parts.” etc.), and authorial indicators (e.g. “By a lady,” “By the author of...”, etc.). Only the first word of the title and proper nouns are capitalized. <br>
$d Print type of volume [Controlled terms: “Letter-press,” “Engraving,” “Manuscript”]<br>
$g Title page extent [Controlled terms: “Half”, “Full”] Half title pages typically include the title of the work without the publication information, epigraphs, etc., while full title pages include all of this data.<br>
$v Volume in which it is located [Controlled terms: “v.1,” “v.2,” etc.]<br>
$x Priority—what entity the title page describes [Work, Volume, Section]<br>

- 246 ind1=0 ind2=7: Running title—appears as two datafields<br>
$a Transcription of running title in full across verso and recto<br>
$a Running title on verso (verso)<br>
$a Running title on recto (recto)<br>
$v Relevant volumes

- 250: Edition statement<br>
$a Transcription of full edition statement, including such terms as “revised,” “enlarged,” “annotated,” etc.<br>
$b Controlled term for transcribed edition statement [“First edition,” “Second edition,” etc.]<br>
$c Authorized edition number if different or absent from $a/$b<br>
$x Transcriptions of edition/revision language in other paratext

- 260: Publication and distribution<br>
$a City of publication as it appears in the text <br>
$b Transcription of publisher names and qualifying terms<br>
$c Date of publication as appears; in roman numerals if applicable<br>
$c [SECOND SUBFIELD c] Date of publication as appears, converted to arabic numerals<br>
$v Volume(s) <br>
$x Notes

- 261: Printer info [if “printed by” is different from “printed for”]<br>
$b Transcription of the printer information if it is in a different location from the publisher information<br>
$f Printer name(s)

#### 300 Fields - Physical Information
- 300: Physical bibliographic features<br>
$a Extent—the number of pages or volumes<br>
$b Illustrations, if any included in work [“Ill.”, “Ill. (frontispiece),” “Col. Ill.”, “Port.”, “Map”]. Descriptions appear in 500 "General Notes" field. <br>
$c Dimensions<br>
$x Format, controlled term [“Folio,” “Duodecimo,” etc.]<br>
$z Work qualifiers such as “In two volumes,” “in five parts” 

#### 400 Fields - Collections
- 490: Ind1=0 Collections (Published Collection, as in “Collected works of ---” or the like, not the library collection.) <br>
$a Title of collection<br>
$x Notes explaining relation between work and collection

#### 500 Fields - Added fields, interpretive and analytic metadata, copy-specific metadata
- 500: General notes—new datafield for each note<br>
$a Notes that do not fit into other categories, such as bookplates, library marginalia, interesting material characteristics, etc. 

- 520: Paratext<br>
$a Type of paratext. Standardized terms so far include [About the Author, To the Author, Advertisement [only used if the “Advertisement” is actually a paratextual essay], Afterword,  Apology, Appendix, Character information, Character note, Colophon, Conclusion, Copyright statement, Dedication, Endnotes, Epilogue, Errata, Essay, Footnotes, Glossary, Index, Introduction, Key, Letter, License, List of characters, Memoir, Note, Official note, Poem, Postscript, Preface, Prologue, Review, Subscribers' list, Table of contents, To the Booksellers, To the Reader, To the Reviewer, To the Subscriber, Other]<br>
$b Transcription of paratext heading: e.g., “The introduction,” “The editor’s preface,” etc.<br>
$c Location [“Front,” “Middle”, “Back”]<br>
$v Volume<br>
$x Notes. Usually includes transcriptions of interesting quotations and the first line of paratext.<br>

- 591: Epigraph<br>
$a Transcription of epigraph<br>
$1 Epigraph source as it appears in the work: e.g., “Odyss.”, “Merchant of Venice”.<br>
$2 Epigraph author as it appears in the work: e.g., “Hom.”, “Virg.”, “Shakespear”<br>
$b Epigraph source if known or discovered<br>
$c Epigraph author if known or discovered<br>
$d Translation of the epigraph. If the epigraph is untranslated in the book, catalogers searched for a translation and added an $x field indicating the source of the translation and the language of the original (usually a URL). <br>
$v Volume <br>
$x Notes; include source of translation

- 592: Narrative form<br>
One of the few fields that refers to the text itself rather than the paratext, this field records the narrative form of the work, based on a quick scan of the text.<br>
$a Primary narrative form [“Epistolary”, “First-person,” “Third-person,” “Dramatic dialogue”]<br>
$b Additional narrative forms that appear in the text, with same controlled terms as $a. <br>
$c Non-prose forms [“Poems,” “Sheet music,” "Theatrical dialogue"]<br>
$d Oddities. This field is for anything we found remarkably strange regarding the narrative form.

- 593: Subscriber’s list<br>
$a Subscriber names, or the first few if the list is multiple pages<br>
$x Notes, including an indication of whether the list was too long to record

- 594: Inscription information and provenance markings<br>
$a Inscription full transcription, including names, dates, messages, etc.<br>
$b Inscription medium [“Ink”, “Pencil”]<br>
$x Notes; including location<br>
$v Volume

- 595: Marginalia<br>
$a Medium [“Ink”, “Pencil”]<br>
$b Content description [“Words,” “Drawings”, “Editorial markings,” “Numbers”]<br>
$v Volume<br>
$x Notes; includes transcription or further description of marginalia

- 596: Translation, Abridgment, Adaptation information Claim<br>
$a Type of source claim [“Translation,” “Abridgment”, “Adaptation”, “Revision”]<br>
$b Location of claim; e.g., title page, dedication, etc.<br>
$c Direct source language. This is language which this translation, etc. immediately comes from; e.g., "translated from the French." <br>
$d Indirect source language. This is the language that the original work was originally written in, for example, "Chinese" if the title page says, “From the French, originally from the Chinese.”<br>
$e Transcription of the translation, abridgment, or adaptation claim.


- 599: Authorship claim (only claims in paratext: for claims in text, make a 500 $a note).<br>
We include separate 599 field for each claim that appears in the paratext, including claims of both text and paratext authorship and claims for or by fictional characters.<br>
$a Author claim type [“Author (text)”, “Author (paratext)”, “Editor (text)”, “Translator (text),” etc.]<br>
$b Author claim description [“Initials”, “Generic/Descriptive”, “Reference to other works”, “Proper name”]<br>
$2 Author claim transcription<br>
$3 Location of author claim<br>
$5 Author gender claim [“Female,” “Male,” “Indeterminate”]<br>
$6 Actual author gender if known [“Female,” “Male,” “Unknown”]<br>
$7 Notes about author claims by fictional characters, transcriptions of relevant quotations

#### 600 Fields - Advertisements
- 656: Advertisements<br>
This field is for parts of the text that explicitly advertise other works or services.<br>
$a Genre of the works being advertised [“Fiction”, “Non-fiction”, “Drama,” “Poetry,” “Periodical,” “Mixed Genre”, “Miscellaneous”]. <br>
$b Location of advertisement [“Front,” “Middle,” “Back”].<br>
$c Advertisement’s relation to work. This subfield describes why these works are being advertised in this specific work (if there is a reason).  [“Same publisher”, “Same genre,” “Same author,” or “No relation”<br>
$v Volume this section appears in <br>
$x Notes

#### 700 Fields - Names
- 700: Personal name authorization from VIAF <br>
We created separate 700 fields for each nonfictional person identified in the text, and authorized them whenever possible in the <a href="http://viaf.org/">VIAF (Virtual Identity Authority File)</a>.<br>
$a Name <br>
$d Dates of birth and death according to VIAF/WorldCat <br>
$4 Relation to work [“Author (text),” “Author (paratext),” “Editor (text),” “Translator (text),” “Translator (paratext),” “Printed for”, “Printed by”, “Sold by”, “Author (epigraph)”, “Inscribed by”, “Author (bookplate),” “Author (source text),” “Author (illustration),” “Dedicatee”] <br>
$5 Authorization, noting whether we were able to find the person in VIAF [“Authorized”, “Unauthorized”]

- 710: Corporate Name<br>
This field follows the same process as the 700 fields, but this field is only used for “corporate” names (names that refer to a corporate identity, i.e. comprised of multiple people), and mostly is only applicable to books that are printed by or for multiple people</br>
$a Name of corporation or multiple persons <br>
$4 Relation to work [“Printed for”, “Printed by”] <br>
$5 Authorization [“Authorized”, “Unauthorized”] <br>
710 ind1="2" ind2=" ": Database. This field specifies that this record is a part of the Early Novels Database, and not other databases.<br>
$a “Early Novels” <br>
$5 Housing institution [“University of Pennsylvania,” “Library Company,” etc.]

#### 900 Fields - Local Information
- 989: Enhanced title field keywords <br>
This field standardizes and lemmatizes words in the title field. Repeated words are only listed once; irregular spellings are included in both the irregular and standardized spelling.<br>
$1 Titles of other works; e.g. "Pamela" when title field contains "By the author of Pamela." <br>
$2 Nouns in singular form. Includes such words here as “Mr.,” “Miss,” “Esq.”, “Novel,” etc. <br>
$3 Adjectives. We include number qualifications here, for example, the word "two" appears if a title has the qualifier “In two volumes."<br>
$4 Place names<br>
$5 Personal names<br>
$6 Verbs in infinitive form [“Write” for “writing”, etc.]<br>
$7 Material objects. This subfield is primarily for physical/material objects and commodities, for example, "letter." <br>
$8 Adverbs

- 999: Signature of END cataloger<br>
$a Initials of END cataloger; e.g. “MJR”.<br>
$b Date cataloged by END as month/day/2-digit year, e.g. 7/6/11.<br>
$c END cataloger’s home institution, e.g. Swarthmore College<br>
$d Initials of second checker/proofreader


****

#### Tutorial: Explore .tsv subsets with Excel Pivot Tables
The complex, copy-specific nature of the data is designed for thoroughness rather than for quick analysis. In this section, we briefly consider a few way sample applications and uses for the data. We look forward to continuing to explore and hear how people use this data.

### 1. Copy-Specific Information
One strength of END is the it gives researchers the ability to delve deeply into a particular text, volume, or author. For example, if you are interested in Henry Fielding, you can set up a filter to see just his works in our tabular data. From here, it's easier to dig into specific information, such as comparisons in early and later editions of the same work, or between British and American editions.

The following shows how to set up a filter in two variables. (We use Excel here, but this will also work in Google Sheets, etc.) 

![Shows using a filter on two variables in Excel. Click on "filter," choose variables at the top of the columnns.](https://github.com/earlynovels/end-dataset/blob/master/Tutorial%20Images/END%20Filter%20Demo%203.gif "Filters Demo")


### 2. Comparative Information
Pivot tables, which can be created quickly in Microsoft Excel or Google Sheets, allow you to compare multiple variables. Please note that depending on the field and your question, the data may need to be cleaned and organized first (we recommend <a href="http://openrefine.org/">OpenRefine</a>). 

Here, we imagine that the scholar is interested in seeing details of how the database was created, recorded in our 999 fields. 

First, we highlight the information that interests us, and create the pivot table. 

![Show how to create a pivot table. Highlight columns, right click, "Insert pivot table," add new sheet.](https://github.com/earlynovels/end-dataset/blob/master/Tutorial%20Images/END%20Create%20Pivot.gif "Pivot Table Create Demo")

Next, we add the data to different fields to compare information, and then we create a chart. 

![Show how to go from pivot table to chart. Pick rows and values, then click in table, Insert -> chart. (Pie chart in demo.)](https://github.com/earlynovels/end-dataset/blob/master/Tutorial%20Images/END%20Pivot%20to%20Chart.gif "Pivot Table to Chart Demo")

With the pivot table, we're able to create a couple of different types of visuals by manipulating the variables in different columns. 

For example, we examine dates vs. schools (drag 999$b to "rows" and 999$c to "columns" and "values") to create the following visual on the institutional affiliation of our catalogers. In this, you can see that the END project has recently expanded to a broader set of institutions.
<br>
<img src="https://github.com/earlynovels/end-dataset/blob/master/Tutorial%20Images/END%20Pic%20Schools%20Over%20Time.png" alt="Schools over time: shows how END project has expanded to different institutions." width="500">
<br>


Next, we examined catalogers vs. schools (999$c to "rows" and "values") to show how many catalog records we have from each of our different institutions. NYU is new to the project, but has already added a significant number of records, for example. 
<br>
<img src="https://github.com/earlynovels/end-dataset/blob/master/Tutorial%20Images/END%20Pic%20Catalogers%20by%20Institution.png" alt="Catalogers by institution: shows different institutions involved." width="500">
<br>


Finally, we chart our individual catalogers, who all sign by initial, to see which people are the most frequent contributers to the database (999$d to "rows" and "values"). The main takeaway: this database is a deeply collaborative effort.
<br>
<img src="https://github.com/earlynovels/end-dataset/blob/master/Tutorial%20Images/END%20Pic%20Catalogers%20by%20Initials.png" alt="Catalogers by initial: it takes a lot of people to make a database!" width="500">
<br>

Enjoy exploring!
