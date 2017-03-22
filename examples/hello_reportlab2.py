from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf")
c.drawString(40, 750,"Welcome to Reportlab!")
c.showPage()
c.save()