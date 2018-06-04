# svg_on_canvas.py

from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg

def add_image(image_path):
    """
    Convert an SVG to a PDF
    """
    my_canvas = canvas.Canvas('svg_on_canvas.pdf')
    drawing = svg2rlg(image_path)
    renderPDF.draw(drawing, my_canvas, 0, 40)
    my_canvas.drawString(50, 30, 'My SVG Image')
    my_canvas.save()

if __name__ == '__main__':
    image_path = 'snakehead.svg'
    add_image(image_path)