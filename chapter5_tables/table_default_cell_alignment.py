# table_default_cell_alignment.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def table_default_cell_alignment():
    doc = SimpleDocTemplate("table_default_cell_alignment.pdf", pagesize=letter)
    story = []

    data = [['col_{}'.format(x) for x in range(1, 6)],
            [str(x) for x in range(1, 6)],
            ['a', 'b', 'c', 'd', 'e'],
            ['F', 'G', 'H', 'I', 'J']
            ]

    tblstyle = TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black)
                           ])

    tbl = Table(data, colWidths=[55 for x in range(5)],
                rowHeights=[45 for x in range(len(data))]
                )
    tbl.setStyle(tblstyle)
    story.append(tbl)

    doc.build(story)

if __name__ == '__main__':
    table_default_cell_alignment()