# main4.py

import sys

from header3 import header
from lxml import objectify
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph


def parse_xml(xml_file):
    with open(xml_file) as f:
        xml = f.read()
        
    root = objectify.fromstring(xml)
    return root

def main(pdf_file, xml_file, logo):
    doc = SimpleDocTemplate(
        pdf_file,
        rightMargin=72, leftMargin=36,
        topMargin=125, bottomMargin=18)
    
    xml = parse_xml(xml_file)
    
    elements = []
    
    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
    styles = getSampleStyleSheet()
    paragraph = Paragraph(txt, styles["Normal"])
    elements.append(paragraph)
    
    doc.xml = xml
    doc.logo_path = logo

    doc.build(elements, onFirstPage=header)
    
if __name__ == '__main__':
    logo_path = sys.argv[1]
    main(pdf_file='main4.pdf', xml_file='eob.xml', 
         logo=logo_path)