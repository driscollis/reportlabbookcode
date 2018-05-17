# simple_radios.py

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green

def create_simple_radios():
    c = canvas.Canvas('simple_radios.pdf')
    
    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Radio demo')
    c.setFont("Courier", 14)
    form = c.acroForm
    
    c.drawString(10, 650, 'Dog:')
    form.radio(name='radio1', tooltip='Field radio1',
               value='value1', selected=False,
               x=110, y=645, buttonStyle='check',
               borderStyle='solid', shape='square',
               borderColor=magenta, fillColor=pink, 
               textColor=blue, forceBorder=True)
    form.radio(name='radio1', tooltip='Field radio1',
               value='value2', selected=True,
               x=110, y=645, buttonStyle='check',
               borderStyle='solid', shape='square',
               borderColor=magenta, fillColor=pink, 
               textColor=blue, forceBorder=True)    
    
    c.drawString(10, 600, 'Cat:')
    form.radio(name='radio2', tooltip='Field radio2',
               value='value1', selected=True,
               x=110, y=595, buttonStyle='cross',
               borderStyle='solid', shape='circle',
               borderColor=green, fillColor=blue, 
               borderWidth=2,
               textColor=pink, forceBorder=True)
    form.radio(name='radio2', tooltip='Field radio2',
               value='value2', selected=False,
               x=110, y=595, buttonStyle='cross',
               borderStyle='solid', shape='circle',
               borderColor=green, fillColor=blue, 
               borderWidth=2,
               textColor=pink, forceBorder=True)
    
    c.drawString(10, 550, 'Pony:')
    form.radio(name='radio3', tooltip='Field radio3',
               value='value1', selected=False,
               x=110, y=545, buttonStyle='star',
               borderStyle='bevelled', shape='square',
               borderColor=blue, fillColor=green, 
               borderWidth=2,
               textColor=magenta, forceBorder=False)
    form.radio(name='radio3', tooltip='Field radio3',
               value='value2', selected=True,
               x=110, y=545, buttonStyle='star',
               borderStyle='bevelled', shape='circle',
               borderColor=blue, fillColor=green, 
               borderWidth=2,
               textColor=magenta, forceBorder=True)
   
    c.save()
    
if __name__ == '__main__':
    create_simple_radios()