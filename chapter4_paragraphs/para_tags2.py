# para_tags2.py

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def paragraph_para_markup():
    doc = SimpleDocTemplate("para_tags2.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Centered', alignment=TA_CENTER))
    print(styles)

    flowables = []

    text = "<para align=center>Hello, I'm a Paragraph</para>"
    para = Paragraph(text, style=styles["Centered"])
    flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    paragraph_para_markup()