# solid_shapes.py

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.shapes import Rect, Ellipse, Circle
from reportlab.graphics.shapes import Wedge, Polygon

def solid_shapes():
    drawing = Drawing(width=400, height=200)
    
    rectangle = Rect(10, 10, 100, 100)
    rectangle.fillColor = colors.blue
    drawing.add(rectangle)
    
    ellipse = Ellipse(100, 50, 50, 25)
    ellipse.fillColor = colors.red
    drawing.add(ellipse)
    
    circle = Circle(50, 170, 25)
    circle.fillColor = colors.green
    drawing.add(circle)
    
    wedge = Wedge(150, 150, 65, 
                  startangledegrees=0, 
                  endangledegrees=45)
    wedge.fillColor = colors.yellow
    drawing.add(wedge)
    
    poly = Polygon(points=[250, 150, 
                           280, 150, 
                           280, 100, 
                           250, 100
                           ])
    poly.fillColor = colors.purple
    drawing.add(poly)
    
    drawing.save(formats=['pdf'], outDir='.', fnRoot='solid_shapes')
    
if __name__ == '__main__':
    solid_shapes()