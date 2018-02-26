# simple_pie_chart_with_title.py

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, String

def simple_pie_chart_with_title():
    data = list(range(15, 105, 15))
    drawing = Drawing(width=400, height=200)
    my_title = String(170, 40, 'My Pie Chart', fontSize=14)
    pie = Pie()
    pie.sideLabels = True

    pie.x = 150
    pie.y = 65

    pie.data = data
    pie.labels = [letter for letter in 'abcdefg']
    pie.slices.strokeWidth = 0.5
    drawing.add(my_title)
    drawing.add(pie)
    drawing.save(formats=['pdf'], outDir='.',
                 fnRoot='simple_pie_chart_with_title')

if __name__ == '__main__':
    simple_pie_chart_with_title()