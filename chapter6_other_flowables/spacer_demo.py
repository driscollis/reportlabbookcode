# spacer_demo.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def no_spacers():
    doc = SimpleDocTemplate("no_spacers.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    for p in range(3):
        text = "<para align=center>Hello, I'm a Paragraph</para>"
        para = Paragraph(text, style=styles["Normal"])
        flowables.append(para)

    doc.build(flowables)

def use_spacers():
    doc = SimpleDocTemplate("use_spacers.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    for p in range(3):
        text = "<para align=center>Hello, I'm a Paragraph</para>"
        para = Paragraph(text, style=styles["Normal"])
        flowables.append(para)
        spacer = Spacer(width=0, height=50)
        flowables.append(spacer)

    doc.build(flowables)


if __name__ == '__main__':
    no_spacers()
    use_spacers()