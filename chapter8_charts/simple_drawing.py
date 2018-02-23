from reportlab.lib import colors
from reportlab.graphics import shapes, renderPDF


def simple_drawing():
    drawing = shapes.Drawing(400, 400)
    drawing.add(shapes.Circle(200, 200, 100, fillColor=colors.red))
    renderPDF.drawToFile(drawing, 'simple_drawing.pdf', msg='My Drawing')

if __name__ == '__main__':
    simple_drawing()