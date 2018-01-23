import os
import reportlab

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


def embedded_font_demo():
    my_canvas = canvas.Canvas("embed_font.pdf",
                              pagesize=letter)
    reportlab_folder = os.path.dirname(reportlab.__file__)
    fonts_folder = os.path.join(reportlab_folder, 'fonts')
    print('ReportLab font folder is located at {}'.format(
        fonts_folder))

    afm = os.path.join(fonts_folder, 'DarkGardenMK.afm')
    pfb = os.path.join(fonts_folder, 'DarkGardenMK.pfb')

    # Register the font so we can use it
    font_face = pdfmetrics.EmbeddedType1Face(afm, pfb)
    pdfmetrics.registerTypeFace(font_face)

    face_name = 'DarkGardenMK'
    font = pdfmetrics.Font('DarkGardenMK',
                           face_name,
                           'WinAnsiEncoding')
    pdfmetrics.registerFont(font)

    # Use the font!
    my_canvas.setFont('DarkGardenMK', 40)
    my_canvas.drawString(10, 730, 'The DarkGardenMK font')
    my_canvas.save()

if __name__ == '__main__':
    embedded_font_demo()