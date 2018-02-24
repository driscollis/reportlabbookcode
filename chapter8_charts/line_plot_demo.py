# line_plot_demo.py

from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.widgets.markers import makeMarker


def line_plot_demo():
    d = Drawing(400, 400)
    line = LinePlot()
    line.x = 50
    line.y = 85
    line.height = 150
    line.width = 250
    line.lineLabelFormat = '%2.0f'

    data = [
            ((1,1), (2,2), (2.5,1), (3,3), (4,5)),
            ((1,2), (2,3), (2.5,2), (3.5,5), (4,6))
        ]
    line.data = data

    line.lines[0].strokeColor = colors.green
    line.lines[1].strokeColor = colors.blue
    line.lines[0].strokeWidth = 3

    line.lines[0].symbol = makeMarker('Circle')
    line.lines[1].symbol = makeMarker('Hexagon')

    line.xValueAxis.valueMin = 0
    line.xValueAxis.valueMax = 10
    line.xValueAxis.valueSteps = [1, 2, 4]
    line.xValueAxis.labelTextFormat = '%2.1f'

    line.yValueAxis.valueMin = 0
    line.yValueAxis.valueMax = 12

    d.add(line, '')
    d.save(formats=['pdf'], outDir='.', fnRoot='line_plot_demo')


if __name__ == '__main__':
    line_plot_demo()