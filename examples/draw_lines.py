from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def draw_strings(my_canvas):
    my_canvas.drawString(30,750, 'John Doe')
    my_canvas.drawString(30,735,'123 AnyWhere Ave')
    my_canvas.drawString(30,720,"Menlo Park CA 12345")


def draw_lines(my_canvas):
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 12)

    start_y = 710
    my_canvas.line(30, start_y, 580, start_y)

    for x in range(10):
        start_y -= 10
        my_canvas.line(30, start_y, 580, start_y)


if __name__ == '__main__':
    my_canvas = canvas.Canvas("lines.pdf", pagesize=letter)
    draw_strings(my_canvas)
    draw_lines(my_canvas)
    my_canvas.save()
