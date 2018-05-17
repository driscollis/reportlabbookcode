# simple_checkboxes.py

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green

def create_simple_checkboxes():
    c = canvas.Canvas('simple_checkboxes.pdf')
    
    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Pets')
    c.setFont("Courier", 14)
    form = c.acroForm
    
    c.drawString(10, 650, 'Dog:')
    form.checkbox(name='cb1', tooltip='Field cb1',
                   x=110, y=645, buttonStyle='check',
                   borderColor=magenta, fillColor=pink, 
                   textColor=blue, forceBorder=True)
    
    c.drawString(10, 600, 'Cat:')
    form.checkbox(name='cb2', tooltip='Field cb2',
                   x=110, y=595, buttonStyle='cross',
                   borderWidth=2, forceBorder=True)
    
    c.drawString(10, 550, 'Pony:')
    form.checkbox(name='cb3', tooltip='Field cb3',
                   x=110, y=545, buttonStyle='star',
                   borderWidth=1, forceBorder=True)
    
    c.drawString(10, 500, 'Python:')
    form.checkbox(name='cb4', tooltip='Field cb4',
                   x=110, y=495, buttonStyle='circle',
                   borderWidth=3, forceBorder=True)
    
    c.drawString(10, 450, 'Hamster:')
    form.checkbox(name='cb5', tooltip='Field cb5',
                   x=110, y=445, buttonStyle='diamond',
                   borderWidth=None,
                   checked=True,
                   forceBorder=True)
    
    c.save()
    
if __name__ == '__main__':
    create_simple_checkboxes()