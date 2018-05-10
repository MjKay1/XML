from lxml import etree 


#DTD
dtd_file = open("map1.dtd")
xml1 = open("map1.xml").read()
xml1 = xml1.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
dtd = etree.DTD(dtd_file)
root = etree.XML(xml1)
print(dtd.validate(root))


#XSD
xsd_file = open("map2.xsd")
xml2 = open("map2.xml").read()
xml2 = xml2.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
xsd = etree.XMLSchema(etree.parse(xsd_file))
root = etree.XML(xml2)
print(xsd.validate(root))


#parsing XML:
root = etree.XML(xml1)		# Where xml1 is XML text
print (root.tag)       		# "map"
print (root[0].tag)			# "polygon"
print (root[0].get("id"))	# "p1"
print (root[0][0].tag)		# "points"
print (root[0][0].text)		# "100,100 200,100" etc.


#generate XML
root = etree.XML(xml1)      				# Could start from nothing
p2 = etree.Element("polygon")				# Create polygon
p2.set("id", "p2");	        	      		# Set attribute
p2.append(etree.Element("points"))			# Append points
p2[0].text = "100,100 100,200 200,200 200,100"	# Set points text
root.append(p2)             				# Append polygon
print (root[1].tag)             			# Check


#transform
xsl3 = open("map3.xsl").read()          	# Read stylesheet
xsl3 = xsl3.replace('<?xml version="1.0" encoding="UTF-8"?>',"")
xslt_root = etree.XML(xsl3)             	# Parse stylesheet
transform = etree.XSLT(xslt_root)   		# Make transform
result_tree = transform(root)		     	# Transform some XML root
transformed_text = str(result_tree)

print(transformed_text)
"""
writer = open('map3.html', 'w')	    	# Normal writer
writer.write(transformed_text)
"""
with open ('map3.html', 'w') as f1:
    f1.write(transformed_text)
    