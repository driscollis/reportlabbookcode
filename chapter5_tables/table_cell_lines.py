# table_cell_lines.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def table_cell_lines():
    doc = SimpleDocTemplate("table_cell_lines.pdf", pagesize=letter)
    story = []

    data = [['col_{}'.format(x) for x in range(1, 6)],
            [str(x) for x in range(1, 6)],
            ['a', 'b', 'c', 'd', 'e'],
            ['F', 'G', 'H', 'I', 'J']
            ]

    tblstyle = TableStyle(
        [('LINEABOVE', (0, 0), (-1, 0), 0.5, colors.red),
         ('LINEBELOW', (0, 0), (-1, 0), 1.5, colors.blue),
         ('LINEBEFORE', (0, 0), (0, -1), 2.5, colors.orange),
         ('LINEAFTER', (-1, 0), (-1, -1), 3.5, colors.green),
         ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)
    story.append(tbl)

    doc.build(story)

if __name__ == '__main__':
    table_cell_lines()