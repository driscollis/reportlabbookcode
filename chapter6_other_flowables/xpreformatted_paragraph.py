# xpreformatted_paragraph.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus import XPreformatted
from reportlab.lib.styles import getSampleStyleSheet


def xpreformatted_paragraph():
    doc = SimpleDocTemplate("xpreformatted_paragraph.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    text = """<font color="blue">Hello, I'm a Paragraph</font>"""
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    text = """Hello, I'm a <font color="red">XPreformatted Paragraph</font>"""
    para = XPreformatted(text, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    xpreformatted_paragraph()