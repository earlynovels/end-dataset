#!/usr/bin/env python

import csv, re
import endmarcxml as emx
from pymarc import marcxml,Record,Field
from sys import argv

"""

Scripts for transforming MARCXML to tabular data
*** tested with python 3.5

Dependencies: pymarc

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

"""Main"""

# * * * * * * * * * * * * * * * * * *

def main(filename,out_filename=""):

    # check stdin
    if type(filename) is str:
        out_path = emx.get_out_filename(filename) if not out_filename else out_filename
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
                curr_row[col] = emx.get_value(col,record)
            print(index)
            csv_writer.writerow(curr_row)

    return 0

if __name__ == '__main__':

    if len(argv) > 2: main(argv[1],argv[2])
    else: main(argv[1])
