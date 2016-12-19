# END Dataset Documentation

#### About the Project
Early works of fiction often have detailed title pages, plot summaries, complex tables of contents, lengthy titles and endnotes, and elaborate prefaces. The [Early Novels Database (END) project](http://www.earlynovels.org) creates rich bibliographic metadata that captures these features in fields that enable new forms of research on English-language fiction of the long eigtheenth century. 

#### About the Dataset
The Early Novels Dataset contains bibliographic metadata for eighteenth-century works of fiction held in the [Collection of British and American Fiction, 1660-1830 (CBAF)](http://franklin.library.upenn.edu/search.html?filter.author_creator_facet.val=Collection%20of%20British%20and%20American%20Fiction%2C%201660-1830%20%28University%20of%20Pennsylvania%29) at the University of Pennsylvania’s [Kislak Center for Special Collections, Rare Books and Manuscripts](http://www.library.upenn.edu/kislak/), as well as other regional repositories. It consists of MARC catalog records enriched with custom subfields designed to offer new kinds of structured data about early fiction in English. 

The END dataset is comprised of high-quality, human-generated metadata that captures a much fuller range edition- and copy-specific information about early novels than traditional library catalog records. The END metadata schema builds on library-standard MARC records with custom-designed subfields that use both controlled and discursive vocabularies to describe a range of bibliographic features outside the scope of traditional cataloging. These include important bibliographic details such as authority statements, full and half title, accurate and controlled place of publication, and edition statement. They capture both copy-specific information about marginalia, inscriptions, and bookplates as well as title-level data on narrative form. And finally, they record the presence of important paratextual features like authors’ notes, epigraphs, footnotes, and indices, which can be found in many works of early fiction but have never been cataloged in a systematic way that would enable faceted search across a corpus. 

As of late 2016, the Early Novels Dataset numbers 1046 records, which represent all of Penn Libraries’ Collection of British and American Fiction holdings published between 1700-1789. The dataset also includes selected holdings from other Philadelphia-area and regional repositories, including the Library Company of Philadelphia, the Rosenbach, the Swarthmore Libraries Rare Book Room, and Bryn Mawr College Special Collections. These 1046 works of fiction likely represent about 14% of existing titles of fiction in English published during this period. They range from the canonical to the almost-unknown, and while some clearly announce themselves to be “novels,” others are aligned with the wider-ranging genres (romances, fables, adventure stories) that contributed to the rise of the novel.

#### Background on the Collection
Penn Libraries’ Collection of British and American Fiction is comprised of nearly three thousand works of early fiction in English. Its core is the Singer-Mendenhall Collection, built through the combined efforts of a University of Pennsylvania graduate student and professor in the first half of the twentieth century. Godfrey F. Singer and John C. Mendenhall focused their collecting efforts on epistolary fiction, and the Singer-Mendenhall collection today has particular strengths in non-canonical epistolary fiction by female and anonymous authors. 

#### Data Formats
END records build on standard MARC library catalog records by adding custom, nonstandard MARC subfields. See the [Library of Congress MARC 21 schema](https://www.loc.gov/marc/bibliographic/), as well as the [Library of Congress guidelines for working with MARCXML](https://www.loc.gov/standards/marcxml/). 

The custom END MARC schema, which includes a number of nonstandard subfields, can be found below. 

The END dataset is also available in json. Tabular subsets are currently in progress and will be available in csv and tsv formats in early 2017. 

****

## END Custom MARC Schema
0xx Fields: (Derived from base catalog records, mostly from Penn Libraries OPAC. Not all END records are built on top of base records, however, so in some END records only the 001 field is present). 

- 001: END Control Number: Control numbers in the 001 field follow different systems depending on the year in which the work was cataloged, but all are unique. Each record in the dataset has a unique identifier. 
  - All records cataloged to 2013 have randomly-generated sequential ID numbers in the 001 field. Most from Penn include Franklin BibIDs are included in the 035 field, but many do not include OCLC numbers. These were cataloged from several different institutions: Penn RBML (now Kislak), Swarthmore College, Bryn Mawr, Library Company, etc.
  - All records cataloged in the summer of 2014 were cataloged in google sheets and converted to XML. They are missing some of the automated fields that are present in the records that used Franklin catalog records as base entries. They have been remediated to have ID numbers in the 001 field, these follow the sequential schema of the voyager records from 2013 and before.
  - Records cataloged from the summer of 2015 and from the 2015-2016 academic year have Franklin BibIDs in the 001 field. Duplicate BibIDs are denoted with a -1 -2 etc.
  - Records cataloged during the summer of 2016 at Penn have Franklin BibIDs in the 001 field. They also have Franklin back-end holdings numbers in the 035 field (not among metadata imported from Franklin--these had to be pulled from the holdings database and collated to individual copies).
  - Records cataloged during the summer of 2016 at NYU have OCLC numbers in the 001 field.
- 008: Publication Date, along with other fixed-length data elements 
  - Publication date for record is in 008 field, positions[bytes] 7-10.
    - E.g. in <marc:controlfield tag="008">860203s1813        enk               00001 eng d</marc:controlfield> “1813” is the pub date. 
  - Single pub dates are designated with an “s” in position[byte] 6. A pub date range is designated with an “m” in position[byte?] 6.
     - E.g. in <marc:controlfield tag="008">851011m18161817enkc              00010aeng d</marc:controlfield> “1816” - “1817” is the pub date range. 
  - To sort on pub date, pull only the first date in positions[bytes] 7-10. 
 - 035: System Control Number (local control numbers - usually Penn BibID, Call Number, OCLC, etc. Not all records have entries in the 035 field.)
- 040: Location ID (For records with Franklin base entries, this is PU, MARC organization code for University of Pennsylvania)
- 041: Language code
$a language of the text (eng for English)
$h language of the original text (if translated)
- 043: Geographic area code
- 090: Locally-assigned call number[f] (Obsolete--not part of standard MARC 21 Bibliographic format)

1xx Fields (Derived from base catalog records)
- 100: Author name
$a Last Name, First Name
$c Title (EX: Sir, Dr., etc)
$d dates of birth and death
- 130: Uniform Title

2xx Fields (Derived from base catalog records)
- 245: Title as cataloged 
$a Title 
$b Subtitle
$c Statement of Responsibility
$n Number of part/section of work

- 246: Title as it appears on title page (there is a separate 246 field for each title page in the work; for instance, a seven-volume novel with a full title page in each volume would have seven repeating 246 fields)
$a Direct transcription of title as it appears on title page, including all punctuation, volume information (e.g. “Vol. I”, “In two parts.” etc.), and authorial indicators (e.g. “By a lady,” “By the author of...”, etc.). Only the first word of the title and proper nouns are capitalized. 
$d Print type of volume [Controlled terms: “Letter-press,” “Engraving,” “Manuscript”]
$g Title page extent [Controlled terms: “Half”, “Full”] Half title pages typically include the title of the work without the publication information, epigraphs, etc., while full title pages include all of this data.
$v volume in which it is located [Controlled terms: “v.1,” “v.2,” etc.]
$x priority—what entity the title page describes [Work, Volume, Section]

- 246 ind1=0 ind2=7: Running title—make two datafields
$a Transcription of running title in full across verso and recto
$v relevant volumes
246 Ind1=0 Ind2=7
$a running title on verso (verso)
$a running title on recto (recto)
$v relevant volumes

- 250: Edition statement
$a transcription of full edition statement
$b controlled term for transcribed edition statement [“First edition,” “Second edition,” etc.]
$c authorized edition number if different or absent from $a/$b
$x transcriptions of edition/revision language in other paratext

- 260: Publication and distribution
$a city of publication as it appears in the text 
$b transcription of publisher names and qualifying terms
$c date of publication as appears; in roman numerals if applicable
$c [SECOND SUBFIELD c] date of publication as appears, converted to arabic numerals
$v volume(s) $x notes

- 261: Printer info [if “printed by” is different from “printed for”]
$b transcription
$f printer name(s)

- 300: Physical bibliographic features
$a extent—how many pages or volumes
$b illustrations [“Ill.”, “Ill. (frontispiece),” “Col. Ill.”, “Port.”, “Map”] 
$c dimensions
$x format, controlled term [“Folio,” “Duodecimo,” etc.]
$z work qualifiers such as“In two volumes,” “in five parts” 

- 490: Ind1=0 Collection 
$a title of collection
$x notes explaining relation between work and collection

- 500: General notes—new datafield for each note
$a Notes that do not fit into other categories, such as bookplates, library marginalia, interesting material characteristics, etc. 

- 520: Paratext
        $a type of paratext, controlled
$b transcribe paratext heading
$c location [“Front,” “Middle”, “Back”]
$v volume
$x notes; transcribe interesting quotations and first line of paratext.

- 591: Epigraph
$a transcription
$1 source of epigraph as written
$2 author of epigraph as written
$b source if known
$c author if known
$d translation
$v volume 
$x notes; include source of translation


- 592: Narrative form
$a primary [“Epistolary”, “First-person,” “Third-person,” “Dramatic dialogue.”
$b additional narrative forms
$c non-prose [“Poems,” “Sheet music”]
$d oddities

- 593: Subscriber’s list
$a subscriber names, or the first few if the list is multiple pages
$x if the list is too long to record, note that here

- 594: Inscription information and provenance markings
$a for any inscriptions, transcribe names, dates, messages, etc.
$b inscription medium [“Ink”, “Pencil”]
$x notes; including location
$v volume

- 595: Marginalia
$a medium [“Ink”, “Pencil”]
$b content description [“Words,” “Drawings”, “Editorial markings,” “Numbers”]
$v volume
$x notes: transcribe or further describe marginalia


- 596: Translation, Abridgment, Adaptation information Claim
$a type of source claim [“Translation,” “Abridgment”, “Adaptation”, “Revision”]
$b location of claim
$c direct source language
$d indirect source language
$e transcribe the claim as it appears


- 599: Authorship claim (only claims in paratext: for claims in text, make a 500 $a note).
$a author claim type [“Author (text)”, “Author (paratext)”, “Editor (text)”, “Translator (text),” etc.]
$b author claim description [“Initials”, “Generic/Descriptive”, “Reference to other works”, “Proper name”]
$2 author claim transcription
$3 location of author claim
$5 author gender claim [“Female,” “Male,” “Indeterminate”]
$6 actual author gender if known [“Female,” “Male,” “Unknown”]
$7 notes about author claims by fictional characters, transcriptions of relevant quotations

- 656: Advertisements (create a datafield for each section of ads with a separate heading)
$a advertisement genre [“Fiction”, “Non-fiction”, “Drama,” “Poetry,” “Periodical,” “Mixed Genre”, “Miscellaneous”]. 
$b Location of advertisement [“Front,” “Middle,” “Back”].
$c advertisement’s relation to work [“Same publisher”, “Same genre,” “Same author,” or “No relation”
$v volume $x notes

- 700: Personal name authorization from VIAF
$a name
$d dates of birth and death according to VIAF/worldcat
$4 relation to work [“Author (text),” “Author (paratext),” “Editor (text),” “Translator (text),” “Translator (paratext),” “Printed for”, “Printed by”, “Sold by”, “Author (epigraph)”, “Inscribed by”, “Author (bookplate),” “Author (source text),” “Author (illustration),” “Dedicatee”]
$5 authorization [“Authorized”, “Unauthorized”]

- 710: Corporate Name
$a name of corporation or multiple persons
$4 relation to work [“Printed for”, “Printed by”]
$5 authorization [“Authorized”, “Unauthorized”]
710 ind1="2" ind2=" ": Database 
$a “Early Novels”
$5 housing institution [“University of Pennsylvania,” “Library Company,” etc.]

- 989: Enhanced title field keywords 
$1 titles of other works
$2 nouns in singular form
$3 adjectives
$4 place names
$5 personal names
$6 verbs in infinitive form [“Write” for “writing”, etc.]
$7 material objects
$8 adverbs

- 999: Signature of END cataloger
$a cataloger initials: Follow the form XX or XXX, e.g. “MJR”.
$b date cataloged month/day/2-digit year, e.g. 7/6/11.
$c cataloger’s home institution, e.g. Swarthmore College
$d initials of quality control editor

***

### Subfields in tabular data subsets (in progress)

1. Most minimal version: titles (first full 246), authors, and dates 
2. Fullest version (below)

-Catalog title [field name?]:
Concatenate (single field) catalog title, catalog subtitle, catalog statement of responsibility (245 a, 245 b, 245 c)

-Full title: 
First 246a where 246g=”full[c]”

-Half title: 
First 246a where 246g=”half” if exists 

[-Running titles - first 246a where 246g=”running title” OR “running title verso” or “running title recto”?]

-Number of volumes: Last integer in 246$v is number of volumes. If no integer in field, number of volumes = 1. 

-Edition statement from title page
250$a: transcription of full edition statement

-Controlled edition statement 
250$b controlled version of transcribed edition statement [“First edition,” “Second edition,” etc.]

-City of publication 
260$a

-Publisher
710$$ where value = “printed for” 
If no 710, use 700$4 where value = “printed for”

-Printer
710$4 where value = “printed by” 
If no 710, use 700$4 where value = “printed by”

-Bookseller 
710$4 where value = “sold by” 
If not 710, 700$4 where value = “sold by” 

-Date of publication 
008=[bytes 7-10]: Master Pub Date [LINK TO EXPLANATION IN SCHEMA BELOW]

260: Publication and distribution

-Place of publication 
260 $a city of publication as it appears in the text 
[if multiple volumes, use volume 1][additional places of publication may exists if multiple volumes]

-Publisher name transcription from title page 
260 $b transcription of publisher names and qualifying terms

-Date of publication on title page
260 $c date of publication as appears; in roman numerals if applicable [grab FIRST subfield c]
[if multiple volumes, use volume 1][additional places of publication may exists if multiple volumes]

-cataloger notes on publication and distribution 
260 $x notes
[if multiple volumes, use volume 1]

Format
-300$x [Controlled terms]

Number of volumes: 
$a
[If there is a "v" in 200$a field, grab integer before it. If no "v," work is 1 vol.]

Illustrations: 
$b illustrations [“Ill.”, “Ill. (frontispiece),” “Col. Ill.”, “Port.”, “Map”] 
[add note: not standardized  - populated field = presence] 

Title of series or collection:
-490: Ind1=0 Collection  $a title of collection

General cataloger notes: 
500: General notes—new datafield for each note
$a Notes that do not fit into other categories, such as bookplates, library marginalia, interesting material characteristics, etc. 
[concatinate all $500a notes - there may be multiple - into a single field]

Paratexts
520: Paratext-new datafield for each paratext
$a type of paratext, controlled
$b transcribed paratext heading (from all volumes)
$v volume
$x notes; transcribe interesting quotations and first line of paratext.
