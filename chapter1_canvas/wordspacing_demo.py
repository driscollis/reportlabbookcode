# wordspacing_demo.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def wordspacer():
    canvas_obj = canvas.Canvas("textobj_word_spacing.pdf",
                               pagesize=letter)

    # Create textobject
    textobject = canvas_obj.beginText()

    # Set text location (x, y)
    textobject.setTextOrigin(10, 730)

    word_spacing = 0
    for indent in range(8):
        textobject.setWordSpace(word_spacing)
        line = '{} - ReportLab spacing demo'.format(word_spacing)
        textobject.textLine(line)
        word_spacing += 1.5

    canvas_obj.drawText(textobject)
    canvas_obj.save()

if __name__ == '__main__':	    
    wordspacer()