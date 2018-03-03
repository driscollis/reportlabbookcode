# flag_demo.py

from reportlab.lib import colors
from reportlab.graphics.widgets import flags
from reportlab.graphics.shapes import Drawing, String


def flag_demo():
    drawing = Drawing(width=612, height=792)
    y = 692
    
    flag = flags.Flag(kind='USA')
    flag.y = y
    drawing.add(flag)
    label = String(95, y-15, 'USA', fontSize=14,
                   textAnchor='middle')
    drawing.add(label)
    
    countries = flag.availableFlagNames()
    countries.pop(1)
    country = 1
    for flag in range(5):
        flag = flags.Flag()
        flag.kind = countries[country]

        flag.y = y - 125
        drawing.add(flag)
        
        label = String(95, flag.y-15, countries[country], 
                       fontSize=14, textAnchor='middle')
        drawing.add(label)        
        
        country += 1
        y -= 125
    
    drawing.save(formats=['pdf'], outDir='.', fnRoot='flag_demo')
    
if __name__ == '__main__':
    flag_demo()