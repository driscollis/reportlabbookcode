# qr_code_demo.py

from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen import canvas


def qr_code_demo(barcode_value):
    c = canvas.Canvas('qr_code_demo.pdf')

    qr_code = qr.QrCodeWidget(barcode_value)
    qr_code.barWidth = 145
    qr_code.barHeight = 145
    qr_code.qrVersion = 1
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing()
    d.add(qr_code)
    renderPDF.draw(d, c, 15, 405)

    c.save()

if __name__ == "__main__":
    qr_code_demo('www.mousevspython.com')