# preformatted_paragraph.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus import Preformatted
from reportlab.lib.styles import getSampleStyleSheet


def preformatted_paragraph():
    doc = SimpleDocTemplate("preformatted_paragraph.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    text = "<para align=center>Hello, I'm a Paragraph</para>"
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    text = "<para align=center>Hello, I'm a Preformatted Paragraph</para>"
    para = Preformatted(text, style=styles["BodyText"])
    flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    preformatted_paragraph()