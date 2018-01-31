# drawing_polygons.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_shapes():
    c = canvas.Canvas("draw_other.pdf")
    c.setStrokeColorRGB(0.2, 0.5, 0.3)
    c.rect(10, 740, 100, 80, stroke=1, fill=0)
    c.ellipse(10, 680, 100, 630, stroke=1, fill=1)
    c.wedge(10, 600, 100, 550, 45, 90, stroke=1, fill=0)
    c.circle(300, 600, 50)
    c.save()

if __name__ == '__main__':
    draw_shapes()