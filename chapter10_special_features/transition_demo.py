# transition_demo.py

from reportlab.pdfgen import canvas

def transition_demo():
    my_canvas = canvas.Canvas('transition_demo.pdf')
    
    my_canvas.drawString(20, 750, 'This is page one')
    my_canvas.showPage()
    
    my_canvas.setPageTransition(
        effectname='Blinds', duration=1, direction=0, 
        dimension='H', 
        motion='I')
    my_canvas.drawString(20, 750, 'This is a transitional page')
    my_canvas.drawImage('snakehead.png', 30, 600,
                        width=100, height=100)
    
    my_canvas.save()
    
    
if __name__ == '__main__':
    transition_demo()