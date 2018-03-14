# annotations.py

from reportlab.pdfgen import canvas

def annotations():
    my_canvas = canvas.Canvas('annotations.pdf')
    
    my_canvas.drawString(10, 700, 'Annotations demo')
    
    my_canvas.setAuthor('Mike Driscoll')
    my_canvas.setTitle('ReportLab: PDF Processing with Python')
    my_canvas.setSubject('Use Python to create PDFs')
    
    my_canvas.save()
    
if __name__ == '__main__':
    annotations()