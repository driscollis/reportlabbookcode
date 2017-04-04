import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("pride_and_prejudice.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)
Story = []

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

lines = 100
with open('pride_and_prejudice.txt') as f:
    while lines:
        txt = f.readline()
        if txt == '\r\n':
            txt = '<br/><br/>'
        Story.append(Paragraph(txt, styles["Normal"]))
        lines -=1

doc.build(Story)