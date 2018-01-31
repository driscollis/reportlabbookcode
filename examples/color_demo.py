from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def color_demo():
    my_canvas = canvas.Canvas("colors.pdf",
                                  pagesize=letter)
    my_canvas.setFont('Helvetica', 10)
    x = 30

    sample_colors = [colors.aliceblue,
                         colors.aquamarine,
                         colors.lavender,
                         colors.beige,
                         colors.chocolate]

    for color in sample_colors:
        my_canvas.setFillColor(color)
        my_canvas.circle(x, 730, 20, fill=1)
        color_str = "{color}".format(color=color._lookupName())
        my_canvas.setFillColor(colors.black)
        my_canvas.drawString(x-10, 700, color_str)
        x += 75

    my_canvas.save()

if __name__ == '__main__':
    color_demo()
