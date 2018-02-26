# simple_pie_chart_label_customization.py

from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing

def simple_pie_chart_label_customization():
    data = [10, 20, 30, 40]
    drawing = Drawing()
    pie = Pie()

    pie.x = 150
    pie.y = 65
    pie.data = data
    pie.labels = [letter for letter in 'abcd']

    # enable label customization
    pie.simpleLabels = 0

    # add some customization
    pie.slices[0].label_angle = 45
    pie.slices[0].label_text = 'foobar'

    # normal pie properties
    pie.slices.strokeWidth = 0.5
    pie.slices[3].popout = 20
    pie.slices[3].strokeDashArray = [1,1]
    drawing.add(pie)
    drawing.save(formats=['pdf'], outDir='.',
                 fnRoot='simple_pie_chart_label_customization')

if __name__ == '__main__':
    simple_pie_chart_label_customization()