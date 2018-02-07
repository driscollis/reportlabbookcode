# paragraph_fonts.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def paragraph_fonts():
    doc = SimpleDocTemplate("paragraph_fonts.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    ptext = "<font name=helvetica size=12>Welcome to Reportlab! (helvetica)</font>"
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    ptext = "<font face=courier size=14>Welcome to Reportlab! (courier)</font>"
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    ptext = "<font name=times-roman size=16>Welcome to Reportlab! (times-roman)</font>"
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    paragraph_fonts()
