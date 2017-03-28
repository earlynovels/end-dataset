#!/usr/bin/env python

import csv, re, json
from pymarc import marcxml,Record,Field
from sys import argv

"""Utility for extracting paratext fields from END marcml
*** tested with python 3.5

usage: $ python end-extract-paratext.py [path to xml].xml

Creates a .tsv with the following fields: id | type | x | b | v

"""
COLUMNS_WORK = [
        "id",
        "title",
        "author",
        "date",
        "type"
        ]

COLUMNS_CODES = [
        "b",
        "x",
        "c",
        "v"
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

def get_pymarc_subfield_value(tag,code,record):
    """default function for returning string of marc field value"""
    
    if record[tag] and record[tag][code]: return record[tag][code]
    else: return ""

def get_concatenated_subfield_values(tag,code,record):
    """default function for returning a concatenated string of subfield values"""

    values = []
    fields = record.get_fields(tag)
    if fields:
        for field in fields:
            for subfield in field.get_subfields(code):
                values.append(subfield)
    return ' | '.join(values)

def get_list_subfield_values(tag,code,record):
    """default function for returning a concatenated string of subfield values"""

    values = []
    fields = record.get_fields(tag)
    if fields:
        for field in fields:
            for subfield in field.get_subfields(code):
                values.append(subfield)
    return values

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

def get_vols(record):
    """return number of volumes based on END modified 300$a field"""

    subfields = get_list_subfield_values('300','a',record)
    p1 = re.compile('\[(\d+) v\.\]')

    for subfield in subfields:

        result = p1.match(subfield)
        if result: return result.groups()[0]

    return ""

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

def get_vols_from_300(record):
    """return number of volumes based on 'a' subfield regex patterns"""

    ## following patterns catch almost all vol references in 300$a (942 records)

    p1 = re.compile("(\d+)\s?v\.?")
    p2 = re.compile("v\.?\s?(\d+)")

    vol_a = get_concatenated_subfield_values('300','a',record)
    vol_v = get_concatenated_subfield_values('300','v',record)

    vol = vol_a + ' | ' + vol_v if vol_v else vol_a

    def get_max(list):
        values = []
        for item in list: values.append(int(item))
        return max(values)

    if vol:
        if p1.search(vol):
            vol = get_max(p1.findall(vol))
        elif p2.search(vol):
            vol = get_max(p2.findall(vol))
        else: vol = '1'
        return vol
    else: return ""

def get_persons(relator,record):
    """return concatenated string of persons based on relator subfield / 710$a or 700$a"""

    persons = []

    corp_names = record.get_fields('710')
    for name in corp_names:
        if name['a'] and name['4'] and relator in name['4'].lower():
            persons.append(name['a'])
    if not persons:
        pers_names = record.get_fields('700')
        for name in pers_names:
            if name['a'] and name['4'] and relator in name['4'].lower():
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

def get_field_paratext_values(field,row):
    """return dictionary of paratext values based on current paratext field"""

    row['type'] = field['a']

    codes = COLUMNS_CODES

    def get_subfield_values_list(field,code):

        values = []
        for subfield in field.get_subfields(code):
            values.append(subfield.replace('\\',''))

        return values if values else ""

    for code in codes: row[code] = str(get_subfield_values_list(field,code))

    return row

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
        return filename[:-4] + '-paratexts.tsv'
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
        if case("title"): return get_pymarc_field_value('245',record)
        if case("author"): return get_pymarc_subfield_value('100','a',record)
        if case("date"): return get_pymarc_field_value('008',record)[7:11]

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
        
        columns = COLUMNS_WORK + COLUMNS_CODES

        csv.register_dialect('marcxmltotsv',delimiter='\t',quoting=csv.QUOTE_NONE,quotechar='',doublequote=False,escapechar=None)
        csv_writer = csv.DictWriter(fh,fieldnames=columns,dialect='marcxmltotsv')
        csv_writer.writeheader()

        # parse xml
        collection = marcxml.parse_xml_to_array(filename,strict=True)

        index = 0

        for record in collection:
            index += 1

            curr_work = {}

            for field in COLUMNS_WORK:
                curr_work[field] = get_value(field, record)

            paratexts = record.get_fields('520')


            for paratext in paratexts:

                curr_row = {}

                for field in COLUMNS_WORK:
                    curr_row[field] = curr_work[field]

                curr_row = get_field_paratext_values(paratext,curr_row)
                csv_writer.writerow(curr_row)
                
    return 0

if __name__ == '__main__':

    if len(argv) > 2: main(argv[1],argv[2])
    else: main(argv[1])