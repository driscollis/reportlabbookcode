# asian_font_demo2.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas


def asian_font_demo():
    my_canvas = canvas.Canvas("asian_font_demo2.pdf",
                              pagesize=letter)

    # Set a Japanese font
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
    my_canvas.setFont('HeiseiMin-W3', 16)

    # Find a word or phrase in Unicode to write out
    nippon = '愛情'  # Love in Japanese

    my_canvas.drawString(25, 730, nippon)
    my_canvas.save()

if __name__ == '__main__':
    asian_font_demo()