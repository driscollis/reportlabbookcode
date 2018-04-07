# page_number_total_main.py

from custom_canvas import PageNumCanvas
from header3 import header
from lxml import objectify
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer


def parse_xml(xml_file):
    with open(xml_file) as f:
        xml = f.read()
        
    root = objectify.fromstring(xml)
    return root


def main(pdf_file, xml_file, logo):
    doc = SimpleDocTemplate(
        pdf_file,
        rightMargin=72, leftMargin=36,
        topMargin=125, bottomMargin=36)
    
    xml = parse_xml(xml_file)
    
    doc.xml = xml
    doc.logo_path = logo
    
    elements = []
    
    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
    styles = getSampleStyleSheet()
    for line in range(150):
        paragraph = Paragraph(txt, styles["Normal"])
        elements.append(paragraph)
    
    doc.build(elements, onFirstPage=header, 
              onLaterPages=header, 
              canvasmaker=PageNumCanvas)
    
if __name__ == '__main__':
    main(pdf_file='page_number_total_main.pdf',
         xml_file='eob.xml',
         logo='snakehead.jpg')