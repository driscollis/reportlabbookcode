# circle_demo.py

from reportlab.graphics.shapes import Circle, Drawing
from reportlab.lib import colors


def create_circle():
    drawing = Drawing(width=400, height=200)
    circle = Circle(50, 170, 25)
    circle.fillColor = colors.green
    circle.strokeColor = colors.red
    circle.strokeWidth = 5
    drawing.add(circle)

    drawing.save(formats=['pdf'], outDir='.', fnRoot='circle')

if __name__ == '__main__':
    create_circle()