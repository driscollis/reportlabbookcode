# main.py

import argparse
import json
import os

from header import header
from lxml import objectify
from parsers import parse_json
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
    supported_ext_types = ['.json', '.xml']
    
    # Get the file extension
    _, ext = os.path.splitext(arguments.data_file)
    
    if ext not in supported_ext_types:
        msg = 'PDF Creator only accepts the following file types: ' \
        '{}. Got {}'
        raise RuntimeError(msg.format(str(supported_ext_types, ext)))
    
    doc = SimpleDocTemplate(
        arguments.path,
        rightMargin=72, leftMargin=36,
        topMargin=125, bottomMargin=18)
    
    if ext == '.xml':
        data = parse_xml(arguments.data_file)
    elif ext == '.json':
        data = parse_json(arguments.data_file)
    
    elements = []
    
    txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,'
    styles = getSampleStyleSheet()
    paragraph = Paragraph(txt, styles["Normal"])
    elements.append(paragraph)
    
    doc.data = data
    doc.logo_path = arguments.logo

    doc.build(elements, onFirstPage=header)
    
if __name__ == '__main__':
    main()