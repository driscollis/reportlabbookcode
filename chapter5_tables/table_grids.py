# table_grids.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Spacer

def table_grids():
    doc = SimpleDocTemplate("table_grids.pdf", pagesize=letter)
    story = []

    data = [['col_{}'.format(x) for x in range(1, 6)],
            [str(x) for x in range(1, 6)],
            ['a', 'b', 'c', 'd', 'e']
            ]

    tblstyle = TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.red),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)
    story.append(tbl)

    story.append(Spacer(0, 25))

    tbl = Table(data, style=[
        ('GRID', (0,0), (-1,-1), 0.5, colors.blue)
    ])
    story.append(tbl)

    doc.build(story)

if __name__ == '__main__':
    table_grids()