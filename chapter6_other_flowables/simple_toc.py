from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Flowable
from reportlab.platypus import PageBreak
from reportlab.platypus.tableofcontents import TableOfContents

class DelayedRef(Flowable):
    _ZEROSIZE = True
    def __init__(self, toc, *args):
        self.args = args
        self.toc = toc

    def wrap(self,w,h):
        return 0,0

    def draw(self,*args,**kwd):
        self.toc.addEntry(*self.args)

def simple_toc():
    doc = SimpleDocTemplate("simple_toc.pdf")
    story = []
    styles = getSampleStyleSheet()

    toc = TableOfContents()
    toc.levelStyles = [
            ParagraphStyle(fontName='Helvetica', fontSize=14, name='Heading1',
                               leftIndent=20, firstLineIndent=-20, spaceBefore=5,
                                           leading=16),
                ParagraphStyle(fontName='Times-Roman', fontSize=14, name='Heading2',
                               leftIndent=20, firstLineIndent=-20, spaceBefore=5,
                                                   leading=16),
        ]
    story.append(toc)

    ipsum = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
        nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
        reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
        culpa qui officia deserunt mollit anim id est laborum.'''

    para = Paragraph("The Beginning", style=styles['Heading1'])
    story.append(DelayedRef(toc, 0, 'The Beginning', 1))
    story.append(para)
    para = Paragraph(ipsum, style=styles['Normal'])
    story.append(para)
    story.append(PageBreak())

    para = Paragraph("The Middle", style=styles['Heading1'])
    story.append(DelayedRef(toc, 0, 'The Middle', 2))
    story.append(para)
    para = Paragraph("The Middle Sub-Header", style=styles['Heading2'])
    story.append(DelayedRef(toc, 1, 'The Middle Sub-Header', 2))
    story.append(para)
    para = Paragraph(ipsum, style=styles['Normal'])
    story.append(para)
    story.append(PageBreak())

    para = Paragraph("The End", style=styles['Heading1'])
    story.append(DelayedRef(toc, 0, 'The End', 3))
    story.append(para)

    doc.multiBuild(story)

if __name__ == '__main__':
    simple_toc()