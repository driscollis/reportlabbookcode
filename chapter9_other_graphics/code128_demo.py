# code128_demo.py

from reportlab.graphics.barcode import code128
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def code128_demo(barcode_value):
    doc = SimpleDocTemplate('code128_demo.pdf')
    styles = getSampleStyleSheet()
    flowables = []

    flowables.append(Paragraph('Code 128:',
                               style=styles['Normal']))
    barcode128 = code128.Code128(barcode_value)
    flowables.append(barcode128)

    doc.build(flowables)

if __name__ == "__main__":
    code128_demo('123456789')