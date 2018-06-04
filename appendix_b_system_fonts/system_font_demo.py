# system_font_demo.py

import find_installed_fonts

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


def system_font_demo(my_canvas, fonts):
    """
    Get the system's installed fonts, loop over
    the fonts and add them to the PDF
    """
    pos_y = 750
    for font in fonts:
        try:
            ttf = TTFont(font, fonts[font])
        except:
            # Skip this font
            continue

        pdfmetrics.registerFont(ttf)

        my_canvas.setFont(font, 12)
        my_canvas.drawString(30, pos_y, font)
        pos_y -= 10
        if pos_y < 40:
            my_canvas.showPage()
            pos_y = 750

if __name__ == '__main__':
    my_canvas = canvas.Canvas("system_font_demo.pdf")
    font_paths = find_installed_fonts.find_installed_ttf_fonts()
    fonts = find_installed_fonts.get_font_names(font_paths)
    system_font_demo(my_canvas, fonts)
    my_canvas.save()