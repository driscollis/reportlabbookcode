# string_demo.py

from reportlab.graphics.shapes import String, Drawing
from reportlab.lib import colors


def string_demo():
    drawing = Drawing(width=400, height=200)

    for size in range(10, 32, 4):
        x = 15 + size * 1.5
        y = 15 + size * 1.5
        my_string = String(x, y, 'Python rocks!')
        my_string.fontName = 'Courier'
        my_string.fontSize = size
        drawing.add(my_string)

    other_string = String(200, 150, 'Centered Text')
    other_string.fontName = 'Times-Roman'
    other_string.fontSize = 40
    other_string.fillColor = colors.red
    other_string.textAnchor = 'middle'
    drawing.add(other_string)

    drawing.save(formats=['pdf'], outDir='.', fnRoot='string_demo')

if __name__ == '__main__':
    string_demo()