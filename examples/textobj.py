from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def textobject_demo():
    my_canvas = canvas.Canvas("txt_obj.pdf",
                              pagesize=letter)
    # Create textobject
    textobject = my_canvas.beginText()

    # Set text location (x, y)
    textobject.setTextOrigin(10, 730)

    # Set font face and size
    textobject.setFont('Times-Roman', 12)

    # Write a line of text + carriage return
    textobject.textLine(text='Python rocks!')

    # Change text color
    textobject.setFillColor(colors.red)

    # Write red text
    textobject.textLine(text='Python rocks in red!')

    # Write text to the canvas
    my_canvas.drawText(textobject)

    my_canvas.save()

if __name__ == '__main__':
    textobject_demo()