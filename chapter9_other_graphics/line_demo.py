# line_demo.py

from reportlab.graphics.shapes import Line, PolyLine
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors


def line_demo():
    drawing = Drawing(width=400, height=200)
    line = Line(25, 25, 150, 150)
    line.strokeColor = colors.red
    line.strokeWidth = 5
    strokeLineJoin = 2
    strokeMiterLimit = 10
    drawing.add(line)
    
    line = Line(125, 75, 150, 150)
    line.strokeWidth = 5
    line.strokeLineJoin = 2
    line.strokeMiterLimit = 10
    drawing.add(line)

    points = [25,50, 35,100, 100,50, 150,150]
    poly = PolyLine(points=points,
                    strokeWidth=3,
                    strokeColor=colors.blue)
    drawing.add(poly)
    
    drawing.save(formats=['pdf'], outDir='.', fnRoot='line_demo')

if __name__ == '__main__':
    line_demo()