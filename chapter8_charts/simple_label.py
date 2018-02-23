# simple_label.py

from reportlab.graphics import shapes, renderPDF
from reportlab.graphics.charts.textlabels import Label
from reportlab.lib import colors


def simple_label():
    drawing = shapes.Drawing(width=400, height=200)
    
    drawing.add(shapes.Rect(200, 100, 10, 10, fillColor=colors.red))
    
    x = 50
    angle = 0
    for item in range(3):
        label = Label()
        label.setOrigin(200, 100)
        label.boxAnchor = 'se'
        label.angle = angle      
        #label.boxStrokeColor = colors.black  
        label.setText('ReportLab label')
        drawing.add(label)
        
        x += 25
        angle += 45
        
    renderPDF.drawToFile(drawing, 'simple_label.pdf')
    
if __name__ == '__main__':
    simple_label()   