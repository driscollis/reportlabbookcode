from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.graphics.shapes import String, Rect, Drawing
from reportlab.platypus import Paragraph, SimpleDocTemplate

def color_demo():
    doc = SimpleDocTemplate("colors.pdf",
                            pagesize=letter)
    flowables = []
    for color in dir(colors):
        attr = getattr(colors, color)
        if isinstance(attr, colors.Color):
            drawing = Drawing(width=100, height=50)
            string = String(10, 10, color)
            rectangle = Rect(125, 10, 100, 35)
            rectangle.fillColor = attr
            
            drawing.add(string)
            drawing.add(rectangle)
            flowables.append(drawing)
        
    doc.build(flowables)
    
if __name__ == '__main__':
    color_demo()