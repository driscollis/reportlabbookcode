# paragraph_numbering.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.sequencer import getSequencer


def paragraph_numbering():
    doc = SimpleDocTemplate("paragraph_numbering.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    for item in range(1, 4):
        ptext = '<seq id="test"> thing(s)'
        para = Paragraph(ptext, style=styles["Normal"])
        flowables.append(para)

    # templates
    seq = getSequencer()
    seq.setFormat('Section', '1')
    seq.setFormat('FigureNo', 'A')

    for item in range(4, 8):
        text = 'Fig. <seq template="%(Section)s-%(FigureNo+)s"/>'
        para = Paragraph(text, style=styles["Normal"])
        flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    paragraph_numbering()