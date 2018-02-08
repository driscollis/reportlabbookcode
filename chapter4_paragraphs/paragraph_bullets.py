# paragraph_bullets.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def paragraph_bullets():
    doc = SimpleDocTemplate("paragraph_bullets.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    ptext = "I'm a custom bulletted paragraph"
    para = Paragraph(ptext, style=styles["Normal"], bulletText='-')
    flowables.append(para)

    ptext = "This is a normal bullet"
    para = Paragraph(ptext, style=styles["Normal"], bulletText='•')
    flowables.append(para)

    ptext = "<bullet>&bull;</bullet>This text uses the bullet tag"
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    paragraph_bullets()