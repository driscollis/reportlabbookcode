from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def gray_color_demo():
    my_canvas = canvas.Canvas("grays.pdf",
                              pagesize=letter)
    my_canvas.setFont('Helvetica', 10)
    x = 30

    grays = [0.0, 0.25, 0.50, 0.75, 1.0]

    for gray in grays:
        my_canvas.setFillGray(gray)
        my_canvas.circle(x, 730, 20, fill=1)
        gray_str = "Gray={gray}".format(gray=gray)
        my_canvas.setFillGray(0.0)
        my_canvas.drawString(x-10, 700, gray_str)
        x += 75

    my_canvas.save()

if __name__ == '__main__':
    gray_color_demo()