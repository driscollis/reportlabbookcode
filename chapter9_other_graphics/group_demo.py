# group_demo.py

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.shapes import Group
from reportlab.graphics.shapes import Circle, String


def group_demo():
    drawing = Drawing(width=400, height=200)
    radius = 25
    circles = Group(
        Circle(50, 40, radius, fillColor=colors.blue),
        Circle(75, 40, radius, fillColor=colors.red),
        Circle(100, 40, radius, fillColor=colors.green),
        Circle(125, 40, radius, fillColor=colors.yellow),
        String(75, 5, 'Circles')
    )
    drawing.add(circles)
    
    more_circles = Group(circles)
    more_circles.translate(75, 55)
    more_circles.rotate(35)
    drawing.add(more_circles)
    
    drawing.save(formats=['pdf'], outDir='.', fnRoot='group_demo')
    
if __name__ == '__main__':
    group_demo()