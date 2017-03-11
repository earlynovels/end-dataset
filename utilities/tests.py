#!/usr/bin/env python

import csv,string, re
from pymarc import marcxml,Record,Field
from sys import argv


def main(filename1):


    collection1 = marcxml.parse_xml_to_array(filename1,strict=True)
    index = 0
    fields = ['520','591','594','595','656']

    def vol_out(field,record):

        line_out = ""

        if record[field]:

            fields = record.get_fields(field)
            num_values = len(fields)

            num_vols = 0
            for f in fields:
                if f['v']: num_vols += 1

            if num_values != num_vols:
                line_out += "\t"

                line_out += field + ": "
                line_out += str(num_vols) + "/" + str(num_values)
                return line_out

    p1 = re.compile("(\d+)\s?v\.?")
    p2 = re.compile("v\.?\s?(\d+)")
    p3 = re.compile("\[(\d+)\sv\.\]")

    for record in collection1:

        index += 1

        line_out = str(index)
        line_out += "\t"
        line_out += record['001'].value()

        paratexts = record.get_fields('520')

        for para in paratexts:

            line_out += "\ta: "
            line_out += str(len(para.get_subfields('a')))

            line_out += "  b: "
            line_out += str(len(para.get_subfields('b')))

            line_out += "  c: "
            line_out += str(len(para.get_subfields('c')))

            line_out += "  v: "
            line_out += str(len(para.get_subfields('v')))

            line_out += " x: "
            line_out += str(len(para.get_subfields('x')))

        print(line_out)
        # if record['300'] and record['300']['a']:

        #     values = []
        #     values_z = []
        #     for field in record.get_fields('300'):

        #         curr_subfields = record['300'].get_subfields('a')
        #         for subfield in curr_subfields:
        #             values.append(subfield)
        #         curr_subfields = record['300'].get_subfields('z')
        #         for subfield in curr_subfields:
        #             values_z.append(subfield)

        #     vol = ' | '.join(values)
        #     if p1.search(vol):
        #         vol = p1.findall(vol)
        #         line_out += "\t p1:"
        #         line_out += str(max(vol))

        #     elif p2.search(vol):
        #         vol = p2.findall(vol)
        #         line_out += "\t p2:"
        #         line_out += str(max(vol))

        #     if (values_z) and ("two volumes" not in values_z[0] and max(vol) != 2) and ("three volumes" not in values_z[0] and max(vol) != 3) and ("four volumes" not in values_z[0] and max(vol) != 4) and ("five volumes" not in values_z[0] and max(vol) != 5):
        #         line_out += "\t"
        #         line_out += str(values_z)
        #         print(line_out)
            # else:
            #     vol = '1'
            # line_out += "\t"
            # line_out += vol
            # print(line_out)

 

        #     curr_subfields = record['300'].get_subfields('a')
        #     curr_a =""
        #     for subfield in curr_subfields:
        #         curr_a += " " + subfield
        # line_out += "\t" + curr_a

        # for field in fields:

        #     result = vol_out(field,record)
        #     if result: line_out += result

        # cols = re.findall('\t',line_out)
        # if len(cols) > 2 : fh.write(line_out+'\n')


    # with open('paratext-vol-comparison.tsv','w') as fh:
    #     for record in collection:

    #         index += 1
    #         line_out = str(index)
    #         line_out += "\t"
    #         line_out += record['001'].value()

    #         if record['300']:
    #             curr_subfields = record['300'].get_subfields('a')
    #             curr_a =""
    #             for subfield in curr_subfields:
    #                 curr_a += " " + subfield
    #         line_out += "\t" + curr_a

    #         for field in fields:

    #             result = vol_out(field,record)
    #             if result: line_out += result
    #             else: line_out += '\t'

    #         cols = re.findall('\t',line_out)
    #         fh.write(line_out+'\n')
                
        # if record['040']:
        #     line_out += "\t"
        #     line_out += record['040'].value()
        #     print(line_out)

        # p1 = re.compile("^(\d+)\s?v\.?.*")
        # p2 = re.compile(".*v\.?\s?(\d+)[\s.:;]?")

        # if record['300'] and record['300']['a']:
        #     vol = ""
        #     if p1.match(record['300']['a']):
        #         vol = p1.match(record['300']['a']).groups()[0]
        #     elif p2.match(record['300']['a']):
        #         vol = p2.match(record['300']['a']).groups()[0]
        #     line_out += '\t'
        #     num = len(record['300'].get_subfields('a'))

        #     if num > 1:

        #         vols=[]

        #         for subfield in record['300'].get_subfields('a'):

        #             vol = ""
        #             if p1.match(subfield):
        #                 vol = p1.match(subfield).groups()[0]
        #             elif p2.match(subfield):
        #                 vol = p2.match(subfield).groups()[0]
        #             vols.append(vol)

        #         line_out += "\t"
        #         line_out += str(max(vols))
        #         # print(line_out)
 
        # fields = record.get_fields('246')
        # vols = []
        # if fields:
        #     # loop through 246 fields
        #     line_out += "\t"
        #     line_out += str(len(fields))

        #     for field in fields:
        #         subfields = field.get_subfields('v')
        #         if subfields:
        #             # loop through 'v' subfields

        #             line_out += "\t"
        #             line_out += str(len(subfields))
        #             for subfield in subfields:
        #                 # grab all integers from 'v' value
        #                 num_vols = re.findall("\d+",subfield)
        #                 if num_vols:
        #                     # append to num_vols list
        #                     for vol in num_vols: vols.append(int(vol))

        #     line_out += '\t'
        #     line_out += str(max(vols)) if vols else ""
        #     # if len(fields) > 1: print(line_out)

        # if record['520']:
        #     fields = record.get_fields('520');

        #     vols = [];
        #     for field in fields:

        #         if record['300'] and record['300']['a']:
        #             vol = ""
        #             if p1.match(record['300']['a']):
        #                 vol = p1.match(record['300']['a']).groups()[0]
        #             elif p2.match(record['300']['a']):
        #                 vol = p2.match(record['300']['a']).groups()[0]
        #             line_out += '\t'
        #             num = len(record['300'].get_subfields('a'))

        #             if num > 1:

        #                 vols=[]

        #                 for subfield in record['300'].get_subfields('a'):

        #                     vol = ""
        #                     if p1.match(subfield):
        #                         vol = p1.match(subfield).groups()[0]
        #                     elif p2.match(subfield):
        #                         vol = p2.match(subfield).groups()[0]
        #                     vols.append(vol)



        # if record.get_fields('246'):
        #     vols = []
        #     for field in record.get_fields('246'):
        #         if field.get_subfields('v'):
        #             print(len(field.get_subfields('v')))
                    # num_vols = re.findall("\d+",field['v'])
                    # if num_vols:
                    #     for vol in num_vols: vols.append(int(vol))

        # line_out += "\t"
        # line_out += str(vols)
        # line_out += "\t"
        # line_out += str(max(vols)) if vols else ""
        # line_out += "\t"

        ## re for 2 v. in 1
        #       match = re.match("^\d+\s+v.*in\s+\d.*",value)

        # re for 2 v. (p. 3223);
        ##      match = re.match("^(\d+)\s+v\.\s+(\(.*\))\s+[:;].*",value)

        # re for 19 v. ; (806 records)
        ##
        ##      match = re.match(".*(v\.+\s+[:;])$",value)

        ## the following for matching .* v. 2 (around 54 records)
        ##      match = re.match(".*v\.+\s?\d+$",value)



        # if record['246']:
        #     curr_fields = record.get_fields('246')
        #     for field in curr_fields:
        #         if field['v']:
        #             line_out += "\t"
        #             for subfield in field.get_subfields('v'):
        #                 line_out += subfield
        #                 line_out += "  "

            # line_out += "\t"
        # line_out += "\n"
        # print(line_out)
    return 0

if __name__ == '__main__':

    # main('sub.xml')
    # main('end-dataset-full-20161219.xml')
    main('file.xml')
