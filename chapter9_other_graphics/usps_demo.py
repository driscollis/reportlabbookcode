# usps_demo.py

from reportlab.graphics.barcode import usps
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def usps_demo(barcode_value):
    doc = SimpleDocTemplate('usps_demo.pdf')
    styles = getSampleStyleSheet()
    flowables = []

    flowables.append(Paragraph('USPS POSTNET:',
                               style=styles['Normal']))
    barcode128 = usps.POSTNET(barcode_value)
    flowables.append(barcode128)

    doc.build(flowables)

if __name__ == "__main__":
    usps_demo('50158-9999')