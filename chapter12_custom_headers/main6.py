# main6.py

import argparse

from header3 import header
from lxml import objectify
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate

def get_args():
    parser = argparse.ArgumentParser(
            description="Custom PDF Header with Logos")
    parser.add_argument('-l', '-logo', '--logo', 
                            action='store',
                            required=True,
                            help="The logo's file path",
                            dest='logo')
    parser.add_argument('-d', '--data_file', 
                            action='store',
                            required=True,
                            help="The data file path",
                            dest='data_file')
    parser.add_argument('-f', '-filepath', '--filepath',
                            action='store',
                            required=True,
                            help="The file path",
                            dest='path')
    arguments = parser.parse_args()

    return arguments


def parse_xml(xml_file):
    with open(xml_file) as f:
        xml = f.read()
        
    root = objectify.fromstring(xml)
    return root


def main():
    arguments = get_args()
    doc = SimpleDocTemplate(
        arguments.path,
        rightMargin=72, leftMargin=36,
        topMargin=125, bottomMargin=18)
    
    xml = parse_xml(arguments.data_file)
    
    elements = []
    
    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
    styles = getSampleStyleSheet()
    paragraph = Paragraph(txt, styles["Normal"])
    elements.append(paragraph)
    
    doc.xml = xml
    doc.logo_path = arguments.logo

    doc.build(elements, onFirstPage=header)
    
if __name__ == '__main__':
    main()