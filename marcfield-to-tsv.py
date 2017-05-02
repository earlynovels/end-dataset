#!/usr/bin/env python

import csv
import endmarcxml as emx
from pymarc import marcxml,Record,Field
from sys import argv

"""Utility for extracting paratext fields from END marcml
*** tested with python 3.5

usage: $ python end-extract-paratext.py [path to xml].xml

Creates a .tsv with the following fields: id | type | x | b | v

"""

"""Main"""

FIELDS = [

    {
        "desc": "paratexts",
        "tag": "520",
        "headers": ["type","transcription","notes","position","vol"],
        "codes": ["a","b","x","c","v"]
    },

    {
        "desc": "epigraphs",
        "tag": "591",
        "codes": ["a","d","1","b","2","c","x","v"]
    }
]

# * * * * * * * * * * * * * * * * * *

def main(filename,out_filename=""):


    def field_to_tsv(field,collection):

        out_path = emx.get_out_filename(filename,field['desc'])

        with open(out_path,'w',newline='') as fh:
        # open output file
            
            columns = emx.COLUMNS_WORK
            columns += field['headers'] if 'headers' in field else field['codes']

            csv.register_dialect('marcxmltotsv',delimiter='\t',quoting=csv.QUOTE_NONE,quotechar='',doublequote=False,escapechar=None)
            csv_writer = csv.DictWriter(fh,fieldnames=columns,dialect='marcxmltotsv')
            csv_writer.writeheader()

            index = 0

            for record in collection:
                index += 1

                curr_work = emx.get_work_metadata(record)

                curr_fields = record.get_fields(field['tag'])

                for curr_field in curr_fields:

                    curr_row = curr_work
                    curr_row = emx.get_field_vol_values(curr_field,field['codes'],curr_row)
                    csv_writer.writerow(curr_row)
                    
        return 0

    
    # parse xml
    collection = marcxml.parse_xml_to_array(filename,strict=True)

    for field in FIELDS:

        field_to_tsv(field,collection)

if __name__ == '__main__':

    if len(argv) > 2: main(argv[1],argv[2])
    else: main(argv[1])
