# bookmark_demo.py

from reportlab.pdfgen import canvas

def bookmark_demo():
    my_canvas = canvas.Canvas('bookmarks.pdf')
    
    my_canvas.drawString(10, 700, 'Page 1')
    my_canvas.bookmarkPage('page1')
    
    my_canvas.showPage()
    
    my_canvas.drawString(10, 700, 'Page 2')
    my_canvas.bookmarkPage('page2')
    
    my_canvas.addOutlineEntry('Page 1', 'page1')
    my_canvas.addOutlineEntry('Page 2', 'page2')
    
    my_canvas.save()
    
if __name__ == '__main__':
    bookmark_demo()