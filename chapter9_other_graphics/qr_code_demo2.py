# qr_code_demo2.py

import qrcode

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Image


def qr_code_demo(barcode_value):
    doc = SimpleDocTemplate('qr_code_demo.pdf')
    flowables = []

    qr_img = qrcode.make(barcode_value)
    qr_img.save('test.png')
    flowables.append(Image('test.png'))
    
    doc.build(flowables)

if __name__ == "__main__":
    qr_code_demo('www.mousevspython.com')