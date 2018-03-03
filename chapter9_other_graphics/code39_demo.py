# code39_demo.py

from reportlab.graphics.barcode import code39
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def code39_demo(barcode_value):
    doc = SimpleDocTemplate('code39_demo.pdf')
    styles = getSampleStyleSheet()
    flowables = []
    
    flowables.append(Paragraph('Code 39 Standard:', 
                               style=styles['Normal']))
    barcode39Std = code39.Standard39(
        barcode_value, barHeight=20, stop=1)
    flowables.append(barcode39Std)
    
    flowables.append(Spacer(0, 25))
    
    flowables.append(Paragraph('Code 39 Extended:',
                               style=styles['Normal']))
    barcode39 = code39.Extended39(barcode_value)
    flowables.append(barcode39)
    
    
    doc.build(flowables)
    
if __name__ == "__main__":
    code39_demo('ReportLab')