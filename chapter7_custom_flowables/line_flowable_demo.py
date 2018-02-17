# line_flowable_demo.py

from line_flowable import MyLineFlowable
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def create_line_flowable():
    """
    Create a pdf
    """
    story = []
    doc = SimpleDocTemplate("create_line_flowable.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    spacer = Spacer(0, 0.25*inch)

    ptext = '<font size=12>%s</font>' % "Section #1"
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(spacer)

    line = MyLineFlowable(500)
    story.append(line)
    story.append(spacer)

    ptext = '<font size=12>%s</font>' % "Section #2"
    story.append(Paragraph(ptext, styles["Normal"]))

    doc.build(story)

if __name__ == "__main__":
    create_line_flowable()