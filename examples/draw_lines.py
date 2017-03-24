from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def draw_strings(canvas_obj):
    canvas_obj.drawString(30,750, 'John Doe')
    canvas_obj.drawString(30,735,'123 AnyWhere Ave')
    canvas_obj.drawString(30,720,"Menlo Park CA 12345")


def draw_lines(canvas_obj):
    canvas_obj.setLineWidth(.3)
    canvas_obj.setFont('Helvetica', 12)

    start_y = 710
    canvas_obj.line(30, start_y, 580, start_y)

    for x in range(10):
        start_y -= 10
        canvas_obj.line(30, start_y, 580, start_y)


if __name__ == '__main__':
    canvas_obj = canvas.Canvas("lines.pdf", pagesize=letter)
    draw_strings(canvas_obj)
    draw_lines(canvas_obj)
    canvas_obj.save()
