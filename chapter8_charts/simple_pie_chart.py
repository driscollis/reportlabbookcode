# simple_pie_chart.py

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing

def simple_pie_chart():
    data = [10, 20, 30, 40]
    drawing = Drawing()
    pie = Pie()

    pie.x = 150
    pie.y = 65
    pie_data = data
    pie.labels = [letter for letter in 'abcd']
    pie.slices.strokeWidth = 0.5
    pie.slices[3].popout = 20
    pie.slices[3].strokeDashArray = [1,1]
    drawing.add(pie)
    drawing.save(formats=['pdf'], outDir='.', fnRoot='simple_pie_chart')

if __name__ == '__main__':
    simple_pie_chart()