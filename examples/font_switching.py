import string
import sys

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas


def standardFonts():
    """
    Create a PDF with all the standard fonts
    """
    for enc in ['MacRoman', 'WinAnsi']:
        canv = canvas.Canvas(
                'StandardFonts_%s.pdf' % enc,
                )
        canv.setPageCompression(0)
 
        x = 0
        y = 744
        for faceName in pdfmetrics.standardFonts:
            if faceName in ['Symbol', 'ZapfDingbats']:
                encLabel = faceName+'Encoding'
            else:
                encLabel = enc + 'Encoding'
 
            fontName = faceName + '-' + encLabel
            pdfmetrics.registerFont(pdfmetrics.Font(fontName,
                                        faceName,
                                        encLabel)
                        )
 
            canv.setFont('Times-Bold', 18)
            canv.drawString(80, y, fontName)
 
            y -= 20
 
            alpha = "abcdefghijklmnopqrstuvwxyz"
            canv.setFont(fontName, 14)
            canv.drawString(x+85, y, alpha)
 
            y -= 20
 
        canv.save()
 
if __name__ == "__main__":
    standardFonts()