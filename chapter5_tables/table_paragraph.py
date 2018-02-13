# table_paragraph.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph

def table_paragraph():
    doc = SimpleDocTemplate("table_paragraph.pdf", pagesize=letter)
    story = []
    styles = getSampleStyleSheet()

    ptext = 'This is some <font color=blue size=14>formatted</font> text'
    p = Paragraph(ptext, styles['Normal'])

    data = [['col_{}'.format(x) for x in range(1, 6)],
            [p for x in range(1, 6)],
            ['a', 'b', 'c', 'd', 'e']
            ]

    tblstyle = TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)
    story.append(tbl)

    doc.build(story)

if __name__ == '__main__':
    table_paragraph()