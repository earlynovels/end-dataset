#!/usr/bin/env python

import csv, re
from pymarc import marcxml,Record,Field
from sys import argv


vols_corrections = []
with open('vols-246-300-disc-corrected-2232017.tsv','r',newline='') as fh:
    rows = csv.reader(fh,delimiter='\t')
    for row in rows: vols_corrections.append(row)
vols_corrections.pop(0)


vols_list = []
with open('ENDMasterDatasetFull20170309.tsv','r',newline='') as fh:
    rows = csv.reader(fh,delimiter='\t')
    for row in rows: vols_list.append(row)
vols_list.pop(0)


with open('corrected-vols.tsv','w',newline='') as fh:

    corrected_vols = csv.writer(fh,delimiter='\t')

    for row in vols_list:

        if row[1] == '' and row[2] == '': row.append('1')
        else:
            index = 0
            for vol in vols_corrections:
                if row[0] == vol[0]:
                    row.append(vol[1])
                    index += 1
                    vols_corrections.pop(index)
        print(row)
        # corrected_vols.writerow(vol)