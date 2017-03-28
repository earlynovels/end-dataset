#!/usr/bin/env python

import csv, re
from pymarc import marcxml,Record,Field
from sys import argv

"""Utilities for transforming MARCXML to tabular data
*** tested with python 3.5

usage: $ python marcxml-to-tsv.py [path to xml].xml

Creates a .tsv with same name as input data file in current directory.
COLUMNS constant list can be reordered or fields can be commented out and
they will not appear in output file.

TODO:
- abstract so not so tightly bound to END marcXML needs
- reconsider the problem of volumes
- data checking, has not been tested robustly for accuracy
"""

COLUMNS = [
        "id",
        "orig language (base)",
        "author name",
        "author dates",
        "author transcribed",
        "title catalog",
        "title full",
        "title half",
        "title series",
        # "246$v vols",
        # "300$a vols",
        # "300$a",
        "vols",
        "edition trans",
        "pub date",
        "pub date transcribed",
        "pub location",
        "pub",
        "pub transcribed",
        "printer",
        "bookseller",
        "pub notes",
        "format",
        "illustrations",
        "pub cataloger notes",
        "para:preface",
        "para:dedication",
        "para:advertisement",
        "para:to the reader",
        "para:intro",
        "para:note",
        "para:other",
        "para:footnotes",
        "epigraph source transcribed",
        "narrative form primary",
        "narrative form secondary",
        "subscriber list",
        "inscription",
        "marginalia",
        "author claim",
        "author claim type",
        "author gender claim",
        "author gender",
        "advertisement genres",
        "title words:other works",
        "title words:singular nouns",
        "title words:place names",
        "holding institution"
        ]

PARA_TYPES = [
        "preface",
        "dedication",
        "advertisement",
        "to the reader",
        "introduction",
        "note",
        "footnote"
        ]

"""General utility functions"""

# * * * * * * * * * * * * * * * * * *

def get_pymarc_field_value(tag,record):
    """default function for returning string of marc field value"""

    if record[tag]: return record[tag].format_field()
    else: return ""

def get_pymarc_subfield_value(tag,subfield,record):
    """default function for returning string of marc field value"""
    
    if record[tag] and record[tag][subfield]: return record[tag][subfield]
    else: return ""

def get_concatenated_subfield_values(tag,subfield,record):
    """default function for returning a concatenated string of subfield values"""

    # below is code for concatenating with '|' character

    # values = []
    # fields = record.get_fields(tag)

    # if fields:
    #     for field in fields:
    #         if field[subfield]: values.append(field[subfield])


    # return ' | '.join(values)

    values = []
    fields = record.get_fields(tag)

    if fields:
        for field in fields:

            for subfield in field.get_subfields(subfield):
                values.append(subfield.replace('\\',''))

    return str(values) if values else ""


"""Specific functions for particular fields"""

# * * * * * * * * * * * * * * * * * *

def get_original_language(record):
    """return original language code / 041$h"""

    lang = get_pymarc_subfield_value('041','h',record)
    return lang if lang else 'eng'

def get_author(record):
    """return creator of work"""
    relators = ['author (text)','author(text)']
    author = get_pymarc_subfield_value('100','a',record)
    if author: return author
    else:
        pers_names = record.get_fields('700')
        for name in pers_names:
            if name['a'] and name['4'] and any(relator in name['4'].lower() for relator in relators):
                return name['a']
            else: return ""

def get_title_full(record):
    """return full title / 246$a"""
    fields = record.get_fields('246')
    if fields:
        for field in fields:
            if field['g'] and field['a'] and "full" in field['g'].lower():
                return field['a']
    else: return ""

def get_title_half(record):
    """return half title / 246$a"""
    fields = record.get_fields('246')
    if fields:
        for field in fields:
            if field['g'] and field['a'] and "half" in field['g'].lower():
                return field['a']
    else: return ""

def get_vols_from_246(record):
    """return number of volumes based on highest 'v' subfield across 246"""
    fields = record.get_fields('246')
    vols = []
    if fields:
        # loop through 246 fields
        for field in fields:
            subfields = field.get_subfields('v')
            if subfields:
                # loop through 'v' subfields
                for subfield in subfields:
                    # grab all integers from 'v' value
                    num_vols = re.findall("\d+",field['v'])
                    if num_vols:
                        # append to num_vols list
                        for vol in num_vols: vols.append(int(vol))

        return str(max(vols)) if vols else ""
    
    else: return ""

def get_vols(record):
    """return number of volumes based on modified 300$a field"""

    p = re.compile("\[(\d+) v.\]")

    if record['300'] and record['300']['a']:

        curr_subfields = record['300'].get_subfields('a')
        for subfield in curr_subfields:
            if p.fullmatch(subfield): return p.fullmatch(subfield).groups()[0]

    else: return ""

def get_vols_from_300(record):
    """return number of volumes based on 'a' subfield regex patterns"""

    ## following patterns catch almost all vol references in 300$a (942 records)

    p1 = re.compile("^(\d+)\s?v\.?.*")
    p2 = re.compile(".*v\.?\s?(\d+)[\s.:;]?")

    if record['300'] and record['300']['a']:

        vol = ""
        curr_subfields = record['300'].get_subfields('a')
        for subfield in curr_subfields:
            vol += " " + subfield
        vol = vol.lstrip()

        if p1.match(record['300']['a']):
            vol = p1.match(record['300']['a']).groups()[0]
        elif p2.match(record['300']['a']):
            vol = p2.match(record['300']['a']).groups()[0]
        return vol
    else: return ""


def get_persons(relator,record):
    """return concatenated string of persons based on relator subfield / 710$a or 700$a"""

    persons = []

    corp_names = record.get_fields('710')
    for name in corp_names:
        if name['a'] and name['4'] and relator.lower() in name['4'].lower():
            persons.append(name['a'])

    pers_names = record.get_fields('700')
    for name in pers_names:
        if name['a'] and name['4'] and relator.lower() in name['4'].lower():
            persons.append(name['a'])

    return ' | '.join(persons)

def get_paratext(para_type,record):
    """return first instance of paratext type from work / 520$x or boolean"""

    paratexts = record.get_fields('520')

    if para_type == 'other':
        for field in paratexts:
            if field['a'] and not any(para in field['a'].lower() for para in PARA_TYPES):
                return 'true'
        else: return ""

    for field in paratexts:
        if field['a'] and para_type in field['a'].lower():
            return field['x'] if field['x'] else 'true'
    else: return ""

def get_epigraph_source_transcribed(record):
    """return epigraph source and author as transcribed / 591$1 + 591$2"""
    epigraph_source = ""
    epigraph_source += get_pymarc_subfield_value('591','1',record)
    author = get_pymarc_subfield_value('591','2',record)
    epigraph_source += " | " + author if author else ""
    return epigraph_source

def get_institution(record):
    """return the holding institution of record / 710$5"""
    indicators = ['2',' ']
    corp_names = record.get_fields('710')
    for name in corp_names:
        if name['5'] and name.indicators == indicators: return name['5']
    return ""

def get_out_filename(filename):
    """return tabular out filename"""
    if type(filename) is str:
        return filename[:-4] + '.tsv'
    else:
        return 1

"""Parent switch function"""

# * * * * * * * * * * * * * * * * * *

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

def get_value(col_name,record):

    for case in switch(col_name):
        if case("id"): return get_pymarc_field_value('001',record)
        if case("orig language (base)"): return get_original_language(record)
        if case("author name"): return get_pymarc_subfield_value('100','a',record)
        if case("author dates"): return get_pymarc_subfield_value('100','d',record)
        if case("author transcribed"): return get_pymarc_subfield_value('245','c',record)
        if case("title catalog"): return get_pymarc_field_value('245',record)
        if case("title full"): return get_title_full(record)
        if case("title half"): return get_title_half(record)
        if case("title series"): return get_pymarc_subfield_value('490','a',record)
        if case("246$v vols"): return get_vols_from_246(record)
        if case("300$a vols"): return get_vols_from_300(record)
        if case("300$a"): return get_concatenated_subfield_values('300','a',record)
        if case("vols"): return get_vols(record)
        if case("edition trans"): return get_pymarc_subfield_value('250','a',record)
        if case("pub date"): return get_pymarc_field_value('008',record)[7:11]
        if case("pub date transcribed"): return get_pymarc_subfield_value('260','c',record)
        if case("pub location"): return get_pymarc_subfield_value('260','a',record)
        if case("pub"): return get_persons("Printed for",record),
        if case("pub transcribed"): return get_pymarc_subfield_value('260','b',record)
        if case("printer"): return get_persons("Printed by",record)
        if case("bookseller"): return get_persons("Sold by",record)
        if case("pub notes"): return get_pymarc_subfield_value('260','x',record)
        if case("format"): return get_pymarc_subfield_value('300','x',record)
        if case("illustrations"): return get_pymarc_subfield_value('300','b',record)
        if case("pub cataloger notes"): return get_concatenated_subfield_values('500','a',record)
        if case("para:preface"): return get_paratext(PARA_TYPES[0],record)
        if case("para:dedication"): return get_paratext(PARA_TYPES[1],record)
        if case("para:advertisement"): return get_paratext(PARA_TYPES[2],record)
        if case("para:to the reader"): return get_paratext(PARA_TYPES[3],record)
        if case("para:intro"): return get_paratext(PARA_TYPES[4],record)
        if case("para:notes"): return get_paratext(PARA_TYPES[5],record)
        if case("para:footnotes"): return get_paratext(PARA_TYPES[6],record)
        if case("para:other"): return get_paratext('other',record)
        if case("epigraph source transcribed"): return get_epigraph_source_transcribed(record)
        if case("narrative form primary"): return get_concatenated_subfield_values('592','a',record)
        if case("narrative form secondary"): return get_concatenated_subfield_values('592','b',record)
        if case("subscriber list"): return 'true' if record.get_fields('593') else ''
        if case("inscription"): return 'true' if record.get_fields('594') else ''
        if case("marginalia"): return 'true' if record.get_fields('595') else ''
        if case("author claim"): return get_pymarc_subfield_value('599','a',record)
        if case("author claim type"): return get_pymarc_subfield_value('599','b',record)
        if case("author gender claim"): return get_pymarc_subfield_value('599','5',record)
        if case("author gender"): return get_pymarc_subfield_value('599','6',record)
        if case("advertisement genres"): return get_concatenated_subfield_values('656','a',record)
        if case("title words:other works"): return get_concatenated_subfield_values('989','1',record)
        if case("title words:singular nouns"): return get_concatenated_subfield_values('989','2',record)
        if case("title words:place names"): return get_concatenated_subfield_values('989','4',record)
        if case("holding institution"): return get_institution(record)

"""Main"""

# * * * * * * * * * * * * * * * * * *

def main(filename,out_filename=""):

    # check stdin
    if type(filename) is str:
        out_path = get_out_filename(filename) if not out_filename else out_filename
    else:
        return 1

    with open(out_path,'w',newline='') as fh:
    # open output file
        csv.register_dialect('marcxmltotsv',delimiter='\t',quoting=csv.QUOTE_NONE,quotechar='',doublequote=False,escapechar=None)
        csv_writer = csv.DictWriter(fh,fieldnames=COLUMNS,dialect='marcxmltotsv')
        csv_writer.writeheader()

        # parse xml
        collection = marcxml.parse_xml_to_array(filename,strict=True)

        index = 0

        for record in collection:
            index += 1
            curr_row = {}

            for col in COLUMNS:
                # for each record create row in tsv
                curr_row[col] = get_value(col,record)
            print(index)
            csv_writer.writerow(curr_row)

    return 0

if __name__ == '__main__':

    if len(argv) > 2: main(argv[1],argv[2])
    else: main(argv[1])