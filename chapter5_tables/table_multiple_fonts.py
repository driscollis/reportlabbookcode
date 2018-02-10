# table_multiple_fonts.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def table_multiple_fonts():
    doc = SimpleDocTemplate("table_multiple_fonts.pdf", pagesize=letter)
    story = []

    data = [['col_{}'.format(x) for x in range(1, 6)],
            [str(x) for x in range(1, 6)],
            ['a', 'b', 'c', 'd', 'e']
            ]

    tblstyle = TableStyle([('FONT', (0, 0), (-1, 0), 'Times-Roman'),
                           ('FONT', (0, 1), (-1, 1), 'Helvetica', 24),
                           ('FONT', (0, 2), (-1, 2), 'Courier', 12)
                           ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)
    story.append(tbl)

    doc.build(story)

if __name__ == '__main__':
    table_multiple_fonts()