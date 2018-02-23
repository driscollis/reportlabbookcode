# simple_3d_line_chart.py

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.linecharts import HorizontalLineChart3D
from reportlab.platypus import SimpleDocTemplate


def simple_3d_line_chart():
    d = Drawing(280, 250)
    line = HorizontalLineChart3D()
    line.x = 50
    line.y = 85
    line.height = 150
    line.width = 250
    
    data = [[1, 2, 3, None, None, None, 5],
            [10, 5, 2, 6, 8, 3, 5]
            ]
    line.data = data
    line.categoryAxis.categoryNames = [
        'Dogs', 'Cats', 'Mice', 'Hamsters',
        'Parakeets', 'Gerbils', 'Fish'
    ]

    line.lines[0].strokeColor = colors.green
    line.lines[1].strokeColor = colors.blue
    line.lines[0].strokeWidth = 3
    line.categoryAxis.labels.angle = 45
    line.categoryAxis.labels.dy = -15
    
    d.add(line, '')

    doc = SimpleDocTemplate('simple_3d_line_chart.pdf')
    story = []
    story.append(d)
    doc.build(story)

if __name__ == '__main__':
    simple_3d_line_chart()
