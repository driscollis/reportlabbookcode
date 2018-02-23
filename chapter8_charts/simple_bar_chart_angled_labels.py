# simple_bar_chart_angled_labels.py

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.platypus import SimpleDocTemplate


def simple_bar_chart_angled_labels():
    d = Drawing(280, 250)
    bar = VerticalBarChart()
    bar.x = 50
    bar.y = 85
    data = [[1, 2, 3, None, None, None, 5],
            [10, 5, 2, 6, 8, 3, 5],
            [5, 7, 2, 8, 8, 2, 5],
            [2, 10, 2, 1, 8, 9, 5],
            ]
    bar.data = data
    bar.categoryAxis.categoryNames = ['Year1', 'Year2', 'Year3',
                                      'Year4', 'Year5', 'Year6',
                                      'Year7']

    bar.bars[0].fillColor = colors.green
    bar.bars[1].fillColor = colors.blue
    bar.bars[2].fillColor = colors.red
    bar.bars[3].fillColor = colors.purple
    bar.categoryAxis.labels.angle = 45
    bar.categoryAxis.labels.dy = -15
    bar.groupSpacing = 12
    bar.barSpacing = 2
    
    d.add(bar, '')

    doc = SimpleDocTemplate('simple_bar_chart_angled_labels.pdf')
    story = []
    story.append(d)
    doc.build(story)

if __name__ == '__main__':
    simple_bar_chart_angled_labels()