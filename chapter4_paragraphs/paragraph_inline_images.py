# paragraph_inline_images.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def paragraph_inline_images():
    doc = SimpleDocTemplate("paragraph_inline_images.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    ptext = '''Here is a picture:
    <img src="snakehead.jpg" width="50" height="50"/> in the
    middle of our text'''
    p = Paragraph(ptext, styles['Normal'])
    flowables.append(p)

    doc.build(flowables)

if __name__ == '__main__':
    paragraph_inline_images()