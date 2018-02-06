# cursor_moving.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def textobject_cursor():
    canvas_obj = canvas.Canvas("textobj_cursor.pdf", pagesize=letter)

    # Create textobject
    textobject = canvas_obj.beginText()

    # Set text location (x, y)
    textobject.setTextOrigin(10, 730)

    for indent in range(4):
        textobject.textLine('ReportLab cursor demo')
        textobject.moveCursor(15, 15)

    canvas_obj.drawText(textobject)
    canvas_obj.save()


if __name__ == '__main__':
    textobject_cursor()