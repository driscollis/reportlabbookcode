# eanbc_demo.py

from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing
from reportlab.pdfgen import canvas


def eanbc_demo(barcode_value):
    c = canvas.Canvas('eanbc_demo.pdf')

    barcode_eanbc8 = eanbc.Ean8BarcodeWidget(barcode_value)
    bounds = barcode_eanbc8.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(50, 10)
    d.add(barcode_eanbc8)
    renderPDF.draw(d, c, 15, 555)

    # draw the eanbc13 code
    barcode_eanbc13 = eanbc.Ean13BarcodeWidget(barcode_value)
    bounds = barcode_eanbc13.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(50, 10)
    d.add(barcode_eanbc13)
    renderPDF.draw(d, c, 15, 465)
    c.save()

if __name__ == "__main__":
    eanbc_demo('12345678')