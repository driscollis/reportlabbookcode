# code93_demo.py

from reportlab.graphics.barcode import code93
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def code93_demo(barcode_value):
    doc = SimpleDocTemplate('code93_demo.pdf')
    styles = getSampleStyleSheet()
    flowables = []

    flowables.append(Paragraph('Code 93 Standard:',
                               style=styles['Normal']))
    barcode93Std = code93.Standard93()
    flowables.append(barcode93Std)

    flowables.append(Spacer(0, 25))

    flowables.append(Paragraph('Code 93 Extended:',
                               style=styles['Normal']))
    barcode93 = code93.Extended93(barcode_value)
    flowables.append(barcode93)

    doc.build(flowables)

if __name__ == "__main__":
    code93_demo('123456789')