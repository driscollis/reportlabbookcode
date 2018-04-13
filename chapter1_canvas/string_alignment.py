# string_alignment.py

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def string_alignment(my_canvas):
    width, height = letter
    
    my_canvas.drawString(80, 700, 'Standard String')
    my_canvas.drawRightString(80, 680, 'Right String')
    
    numbers = [987.15, 42, -1,234.56, (456.78)]
    y = 650
    for number in numbers:
        my_canvas.drawAlignedString(60, y, str(number))
        y -= 20
    
    my_canvas.drawCentredString(width / 2, 550, 'Centered String')
    
    my_canvas.showPage()
    

if __name__ == '__main__':
    my_canvas = canvas.Canvas("string_alignment.pdf")
    string_alignment(my_canvas)
    my_canvas.save()