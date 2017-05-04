#!/usr/bin/env python

import csv
import endmarcxml as emx
from pymarc import marcxml,Record,Field
from sys import argv

"""Utility for extracting values from individual fields from END marcxml
*** tested with python 3.5

usage: $ python marcfield-to-tsv.py [path to xml].xml

Generates .tsv files based on DATAFIELDS constant list. For each repeatable
datafield in DATAFIELDS, create data row per field, concatenating multiple
subfield values into lists.

desc - name of field (and generated file suffix)
tag - marc tag number
headers - (optional) human readable headers that correspond to subfield codes
codes - marc codes of subfields to extract values



"""

"""Main"""

DATAFIELDS = [

    {
        "desc": "paratexts",
        "tag": "520",
        "headers": ["type","transcription","notes","position","vol"],
        "codes": ["a","b","x","c","v"]
    },

    # {
    #     "desc": "epigraphs",
    #     "tag": "591",
    #     "codes": ["a","d","1","b","2","c","x","v"]
    # },

    # { 
    #     "desc": "marginalia",
    #     "tag": "595",
    #     "codes": ["a","b","v","x"]
    # },

    # {
    #     "desc": "inscriptions",
    #     "tag": "594",
    #     "codes": ["a","b","x","v"]
    # },

    # {
    #     "desc": "authorship",
    #     "tag": "599",
    #     "codes": ["a","b","2","3","5","6","7"]
    # },

    # {
    #     "desc": "translation",
    #     "tag": "596",
    #     "codes": ["a","b","c","d","e"]
    # },

    # {
    #     "desc": "forms",
    #     "tag": "592",
    #     "codes": ["a","b","c","d"]
    # },

    {
        "desc": "title-pos-ne",
        "tag": "989",
        "headers": ["other works","nouns","adjectives","places","persons","verbs","material objects","adverbs"],
        "codes": ["1","2","3","4","5","6","7","8"]
    }
]

# * * * * * * * * * * * * * * * * * *

def main(filename,out_filename=""):


    def field_to_tsv(field,collection):

        out_path = emx.get_out_filename(filename,field['desc'])

        with open(out_path,'w',newline='') as fh:
        # open output file
            
            columns = emx.COLUMNS_WORK + field['codes']

            csv.register_dialect('marcxmltotsv',delimiter='\t',quoting=csv.QUOTE_NONE,quotechar='',doublequote=False,escapechar=None)
            csv_writer = csv.DictWriter(fh,fieldnames=columns,dialect='marcxmltotsv')

            headers = {}
            headers_list = []
            headers_list += emx.COLUMNS_WORK
            if 'headers' in field: headers_list += field['headers']
            else: headers_list += field['codes']

            i = 0
            for column in columns:
                headers[column] = headers_list[i]
                i += 1

            index = 0

            csv_writer.writerow(headers)

            for record in collection:
                index += 1

                curr_work = emx.get_work_metadata(record)
                curr_fields = record.get_fields(field['tag'])

                if curr_fields and field['tag'] == '989':
                    curr_row = emx.get_field_989_values(curr_fields,field['codes'],curr_work)
                    csv_writer.writerow(curr_row)
                else:
                    for curr_field in curr_fields:

                        curr_row = curr_work
                        curr_row = emx.get_field_vol_values(curr_field,field['codes'],curr_row)
                        csv_writer.writerow(curr_row)
                    
        return 0

    
    # parse xml
    collection = marcxml.parse_xml_to_array(filename,strict=True)

    for datafield in DATAFIELDS:

        field_to_tsv(datafield,collection)

if __name__ == '__main__':

    if len(argv) > 2: main(argv[1],argv[2])
    else: main(argv[1])
