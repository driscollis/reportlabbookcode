# svg_scaled_on_canvas.py

from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg


def scale(drawing, scaling_factor):
    """
    Scale a reportlab.graphics.shapes.Drawing()
    object while maintaining the aspect ratio
    """
    scaling_x = scaling_factor
    scaling_y = scaling_factor

    drawing.width = drawing.minWidth() * scaling_x
    drawing.height = drawing.height * scaling_y
    drawing.scale(scaling_x, scaling_y)
    return drawing


def add_image(image_path, scaling_factor):
    """
    Scale an SVG and add it to a PDF
    """
    my_canvas = canvas.Canvas('svg_scaled_on_canvas.pdf')
    drawing = svg2rlg(image_path)
    scaled_drawing = scale(drawing, scaling_factor=scaling_factor)
    renderPDF.draw(scaled_drawing, my_canvas, 0, 40)
    my_canvas.drawString(50, 30, 'My SVG Image')
    my_canvas.save()

if __name__ == '__main__':
    image_path = 'snakehead.svg'
    add_image(image_path, scaling_factor=0.5)