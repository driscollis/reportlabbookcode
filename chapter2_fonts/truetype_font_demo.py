# truetype_font_demo.py

import os
import reportlab

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def embedded_font_demo():
    my_canvas = canvas.Canvas("truetype_font_demo.pdf",
                              pagesize=letter)
    reportlab_folder = os.path.dirname(reportlab.__file__)
    fonts_folder = os.path.join(reportlab_folder, 'fonts')
    print('ReportLab font folder is located at {}'.format(
        fonts_folder))

    # Register the font so we can use it
    vera_font_path = os.path.join(fonts_folder, 'Vera.ttf')
    
    # Usage: TTFont(name,filename)
    vera_font = TTFont('Vera', vera_font_path)
    pdfmetrics.registerFont(vera_font)

    # Use a generic font
    my_canvas.setFont('Helvetica', 40)
    my_canvas.drawString(10, 730, 'The Helvetica font')

    # Use the font!
    my_canvas.setFont('Vera', 40)
    my_canvas.drawString(10, 690, 'The Vera font')
    my_canvas.save()

if __name__ == '__main__':
    embedded_font_demo()