# main_config.py

import configparser
import os

from header3 import header
from lxml import objectify
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate

def get_logo_from_config():
    cfg_path = 'config.ini'
    if os.path.exists(cfg_path):
        config = configparser.ConfigParser()
        config.read(cfg_path)
        logo_path = config.get('General', 'logo_path')
        return logo_path
    else:
        return None

def parse_xml(xml_file):
    with open(xml_file) as f:
        xml = f.read()
        
    root = objectify.fromstring(xml)
    return root


def main(pdf_file, xml_file):
    doc = SimpleDocTemplate(
        pdf_file,
        rightMargin=72, leftMargin=36,
        topMargin=125, bottomMargin=18)
    
    xml = parse_xml(xml_file)
    
    doc.xml = xml
    doc.logo_path = get_logo_from_config()
    
    elements = []

    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
    styles = getSampleStyleSheet()
    paragraph = Paragraph(txt, styles["Normal"])
    elements.append(paragraph)
    
    doc.build(elements, onFirstPage=header)
    
if __name__ == '__main__':
    main(pdf_file='main_config.pdf', xml_file='eob.xml')