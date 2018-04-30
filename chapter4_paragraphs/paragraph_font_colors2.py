# paragraph_font_colors.py

import custom_colors

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import reportlab.lib.colors

def paragraph_font_colors():
    doc = SimpleDocTemplate("paragraph_font_colors2.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    ptext = """<font name=helvetica size=12 color={}>
    Welcome to Reportlab! (helvetica)</font>""".format(custom_colors.lime)
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    ptext = """<font name=courier fg={} size=14>
    Welcome to Reportlab! (courier)</font>""".format(custom_colors.maroon)
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    ptext = """<font name=times-roman size=16 color={}>
    Welcome to Reportlab! (times-roman)</font>""".format(custom_colors.olive)
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    paragraph_font_colors()