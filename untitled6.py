# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 10:15:26 2021

@author: get-a
"""
#import library
import requests
import lxml.html
from lxml import etree
 

url = "http://www.ynet.co.il/Integration/StoryRss2.xml"

resp = requests.get(url)

xslt_doc = etree.parse("tesxslt.txt")

xslt_transformer = etree.XSLT(xslt_doc)
 
source_doc = etree.parse(resp.content)
output_doc = xslt_transformer(source_doc)
 
print(str(output_doc))
output_doc.write("output-toc.html", pretty_print=True)