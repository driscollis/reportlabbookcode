# flowable_orientation.py

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.platypus import Frame, PageTemplate, NextPageTemplate, Spacer


def alternate_orientations():
    doc = SimpleDocTemplate("orientations.pdf",
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=72,
                            bottomMargin=18)
    styles = getSampleStyleSheet()
    normal = styles["Normal"]

    margin = 0.5 * inch
    frame = Frame(margin, margin, doc.width, doc.height,
                  id='frame')
    portrait_template = PageTemplate(id='portrait',
                                     frames=[frame],
                                     pagesize=letter)
    landscape_template = PageTemplate(id='landscape',
                                      frames=[frame],
                                      pagesize=landscape(letter))
    doc.addPageTemplates([portrait_template, landscape_template])

    story = []
    story.append(Paragraph('This is a page in portrait orientation', normal))

    # Change to landscape orientation
    story.append(NextPageTemplate('landscape'))
    story.append(PageBreak())
    story.append(Spacer(inch, 2*inch))
    story.append(Paragraph('This is a page in landscape orientation', normal))

    # Change back to portrait
    story.append(NextPageTemplate('portrait'))
    story.append(PageBreak())
    story.append(Paragraph("Now we're back in portrait mode again", normal))

    doc.build(story)

if __name__ == '__main__':
    alternate_orientations()