# simple_stacked_bar_chart.py

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.platypus import SimpleDocTemplate


def simple_stacked_bar_chart():
    """
    Creates a bar chart in a PDF
    """
    d = Drawing(280, 250)
    bar = VerticalBarChart()
    bar.x = 50
    bar.y = 85
    data = [[1, 2, 3, None, None, None, 5],
            [10, 5, 2, 6, 8, 3, 5]
            ]
    bar.data = data
    bar.categoryAxis.categoryNames = ['Year1', 'Year2', 'Year3',
                                      'Year4', 'Year5', 'Year6',
                                      'Year7']

    bar.bars[0].fillColor = colors.green
    bar.bars[1].fillColor = colors.blue
    bar.categoryAxis.labels.angle = 45
    bar.categoryAxis.labels.dy = -15
    bar.categoryAxis.style = 'stacked'
    
    d.add(bar, '')

    doc = SimpleDocTemplate('simple_stacked_bar_chart.pdf')
    story = []
    story.append(d)
    doc.build(story)

if __name__ == '__main__':
    simple_stacked_bar_chart()