# paragraph_font_colors.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import reportlab.lib.colors

def paragraph_font_colors():
    doc = SimpleDocTemplate("paragraph_font_colors.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    ptext = """<font name=helvetica size=12 color=red>
    Welcome to Reportlab! (helvetica)</font>"""
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    ptext = """<font name=courier fg=blue size=14>
    Welcome to Reportlab! (courier)</font>"""
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    ptext = """<font name=times-roman size=16 color=#777215>
    Welcome to Reportlab! (times-roman)</font>"""
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    paragraph_font_colors()