# char_spacing_demo.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def textobject_char_spacing():
    canvas_obj = canvas.Canvas("textobj_char_spacing.pdf",
                               pagesize=letter)

    # Create textobject
    textobject = canvas_obj.beginText()

    # Set text location (x, y)
    textobject.setTextOrigin(10, 730)

    spacing = 0
    for indent in range(8):
        textobject.setCharSpace(spacing)
        line = '{} - ReportLab spacing demo'.format(spacing)
        textobject.textLine(line)
        spacing += 0.7

    canvas_obj.drawText(textobject)
    canvas_obj.save()


if __name__ == '__main__':
    textobject_char_spacing()