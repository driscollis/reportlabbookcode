# axes_demo.py

from reportlab.graphics import shapes, renderPDF
from reportlab.graphics.charts.axes import XCategoryAxis, YValueAxis
from reportlab.lib import colors


def axes_demo():
    drawing = shapes.Drawing(width=500, height=300)
    
    data = [(5, 10, 15, 20),
            (10, 17, 25, 31)]
    
    x_axis = XCategoryAxis()
    x_axis.setPosition(100, 100, 350)
    x_axis.configure(data, barWidth=None)
    x_axis.categoryNames = ['Python', 'Ruby', 'C++', 'Haskell', 'Java']
    x_axis.labels.boxAnchor = 'n'
    x_axis.labels[0].angle = 45
    x_axis.labels[0].fontName = 'Times-Bold'
    x_axis.labels[1].fontName = 'Courier'
    x_axis.labels[1].fontSize = 16
    drawing.add(x_axis)
    
    y_axis = YValueAxis()
    y_axis.setPosition(75, 75, 150)
    y_axis.configure(data)
    drawing.add(y_axis)    
        
    renderPDF.drawToFile(drawing, 'axes_demo.pdf')
    
if __name__ == '__main__':
    axes_demo()