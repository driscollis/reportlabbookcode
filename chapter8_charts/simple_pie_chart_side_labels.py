# simple_pie_chart_side_labels.py

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing

def simple_pie_chart_side_labels():
    data = list(range(15, 105, 15))
    drawing = Drawing()
    pie = Pie()
    pie.sideLabels = True

    pie.x = 150
    pie.y = 65

    pie.data = data
    pie.labels = [letter for letter in 'abcdefg']
    pie.slices.strokeWidth = 0.5
    drawing.add(pie)
    drawing.save(formats=['pdf'], outDir='.',
                 fnRoot='simple_pie_chart_side_labels')

if __name__ == '__main__':
    simple_pie_chart_side_labels()