# table_background_gradient.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def table_background_gradient():
    doc = SimpleDocTemplate("table_background_gradient.pdf", pagesize=letter)
    story = []

    data = [['col_{}'.format(x) for x in range(1, 6)],
            [str(x) for x in range(1, 6)],
            ['a', 'b', 'c', 'd', 'e']
            ]

    tblstyle = TableStyle([('BACKGROUND', (0, 0), (-1, 0), 
                            ["HORIZONTAL", colors.red, colors.blue]),
                            ('TEXTCOLOR', (0, 1), (-1, 1), colors.blue)
                            ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)
    story.append(tbl)

    doc.build(story)

if __name__ == '__main__':
    table_background_gradient()