# main.py

from header import Header
from lxml import objectify
from reportlab.platypus import SimpleDocTemplate


def parse_xml(xml_file):
    with open(xml_file) as f:
        xml = f.read()

    root = objectify.fromstring(xml)
    return root


def main(pdf_file, xml_file):
    doc = SimpleDocTemplate(
        pdf_file,
        rightMargin=72, leftMargin=36,
        topMargin=36, bottomMargin=18)

    xml = parse_xml(xml_file)

    elements = []

    header = Header(xml)
    elements.append(header)
    doc.build(elements)

if __name__ == '__main__':
    main(pdf_file='header.pdf', xml_file='eob.xml')