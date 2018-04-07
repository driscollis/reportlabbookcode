# main5.py

import argparse

from header3 import header
from lxml import objectify
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph


def get_args():
    parser = argparse.ArgumentParser(
            description="Custom PDF Header with Logos")
    parser.add_argument('-l', '-logo', '--logo', 
                        action='store',
                        required=True,
                        help="The logo's file path",
                        dest='logo')
    arguments = parser.parse_args()

    return arguments


def parse_xml(xml_file):
    with open(xml_file) as f:
        xml = f.read()

    root = objectify.fromstring(xml)
    return root


def main(pdf_file, xml_file):
    arguments = get_args()
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
    doc.logo_path = arguments.logo

    doc.build(elements, onFirstPage=header)

if __name__ == '__main__':
    main(pdf_file='main5.pdf', xml_file='eob.xml')