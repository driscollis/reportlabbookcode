# simple_listboxes.py

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import magenta, pink, blue, green, red

def create_simple_listboxes():
    c = canvas.Canvas('simple_listboxes.pdf')
    
    c.setFont("Courier", 20)
    c.drawCentredString(300, 700, 'Listboxes')
    c.setFont("Courier", 14)
    form = c.acroForm
    
    c.drawString(10, 650, 'Choose a letter:')
    options = [('A','Av'),'B',('C','Cv'),('D','Dv'),'E',('F',),('G','Gv')]
    form.listbox(name='listbox1', value='A',
                x=165, y=590, width=72, height=72,
                borderColor=magenta, fillColor=pink, 
                textColor=blue, forceBorder=True, options=options,
                fieldFlags='multiSelect')
  
    c.drawString(10, 500, 'Choose an animal:')
    options = [('Cat', 'cat'), ('Dog', 'dog'), ('Pig', 'pig')]
    form.listbox(name='choice2', tooltip='Field choice2',
                value='Cat',
                options=options, 
                x=165, y=440, width=72, height=72,
                borderStyle='solid', borderWidth=1,
                forceBorder=True)
    
    c.save()
    
if __name__ == '__main__':
    create_simple_listboxes()