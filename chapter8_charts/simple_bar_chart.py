# simple_bar_chart.py

from reportlab.lib.colors import PCMYKColor
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart


def simple_bar_chart():
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

    bar.bars[0].fillColor = PCMYKColor(0,100,100,40,alpha=85)
    bar.bars[1].fillColor = PCMYKColor(23,51,0,4,alpha=85)
    
    d.add(bar, '')

    d.save(formats=['pdf'], outDir='.', fnRoot='simple_bar_chart')

if __name__ == '__main__':
    simple_bar_chart()