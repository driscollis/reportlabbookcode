from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def draw_lines(my_canvas):
    my_canvas.setLineWidth(.3)

    start_y = 710
    my_canvas.line(30, start_y, 580, start_y)

    for x in range(10):
        start_y -= 10
        my_canvas.line(30, start_y, 580, start_y)


if __name__ == '__main__':
    my_canvas = canvas.Canvas("lines.pdf", pagesize=letter)
    draw_lines(my_canvas)
    my_canvas.save()
