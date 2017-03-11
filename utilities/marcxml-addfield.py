# -*- coding: UTF-8 -*-

# parsing MARCXML using pymarc in order to add a field based on a
# piped in tsv file

import logging,csv
from pymarc import XMLWriter, JSONWriter, marcxml, Field, Record, MARC8ToUnicode
import xml.etree.ElementTree as ET
import unicodedata
import six

XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
MARC_XML_NS = "http://www.loc.gov/MARC21/slim"
MARC_XML_SCHEMA = "http://www.loc.gov/MARC21/slim http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd"

class NSMarcXml(marcxml.XmlHandler):

	def record_to_xml(self,record, quiet=False, namespace=False):
	    node = self.record_to_xml_node(record, quiet, namespace)
	    return ET.tostring(node)

	def record_to_xml_node(self,record, quiet=False, namespace=False):
	    """
	    converts a record object to a chunk of xml

	    # include the marcxml namespace in the root tag (default: False)
	    record_to_xml(record, namespace=True)
	    """
	    # helper for converting non-unicode data to unicode
	    # TODO: maybe should set g0 and g1 appropriately using 066 $a and $b?
	    
	    prefix = 'marc:'

	    marc8 = MARC8ToUnicode(quiet=quiet)
	    def translate(data):
	        if type(data) == six.text_type:
	            return data
	        else:
	            return marc8.translate(data)

	    root = ET.Element(prefix+'record')
	    if namespace:
	        root.set('xmlns', MARC_XML_NS)
	        root.set('xmlns:xsi', XSI_NS)
	        root.set('xsi:schemaLocation', MARC_XML_SCHEMA)
	    leader = ET.SubElement(root, prefix + 'leader')
	    leader.text = record.leader
	    for field in record:
	        if field.is_control_field():
	            control_field = ET.SubElement(root, prefix + 'controlfield')
	            control_field.set('tag', field.tag)
	            control_field.text = translate(field.data)
	        else:
	            data_field = ET.SubElement(root, prefix + 'datafield')
	            data_field.set('tag', field.tag)
	            data_field.set('ind1', field.indicators[0])
	            data_field.set('ind2', field.indicators[1])
	            for subfield in field:
	                data_subfield = ET.SubElement(data_field, prefix + 'subfield')
	                data_subfield.set('code', subfield[0])
	                data_subfield.text = translate(subfield[1])

	    return root

# open marcxml file

filename = 'ENDMasterDatasetFull20170309-appended-vols.xml'
# fileout = filename[:-4] + '.tsv'
fileout = filename[:-4] + '.json'

xmlhandle = NSMarcXml()
records = marcxml.parse_xml_to_array(filename,strict=True)


""" sample code for writing out to json """
jsonwriter = JSONWriter(open(fileout,'wt'))
for record in records: jsonwriter.write(record)
jsonwriter.close()


""" sample code for adding a field and subfield and writing out to string """

# with open(filename,'w') as fh:
	# for rec in records:

		# curr_id = rec.get_fields('001')[0].value()
		# curr_vol_stmt = '[' + vols_list[curr_id] + " v.]"

		# if rec['300']: rec['300'].add_subfield('a',curr_vol_stmt)
		# else:
		# 	new300 = Field(

		# 			tag = '300',
		# 			indicators = [' ',' '],
		# 			subfields = ['a', curr_vol_stmt,]

		# 	)

		# 	rec.add_ordered_field(new300)
		# fh.write(str(xmlhandle.record_to_xml(rec,False,False)))