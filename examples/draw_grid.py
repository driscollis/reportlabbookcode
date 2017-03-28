from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def draw_grid(canvas_obj, xlist, ylist):
    canvas_obj.grid(xlist, ylist)

if __name__ == '__main__':
    canvas_obj = canvas.Canvas("grid.pdf", pagesize=letter)
    xlist = [10, 30, 50, 70, 90, 110]
    ylist = [750, 730, 710, 690, 670]
    draw_grid(canvas_obj, xlist, ylist)
    canvas_obj.save()