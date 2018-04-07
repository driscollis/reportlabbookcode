# custom_canvas.py

from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


class PageNumCanvas(canvas.Canvas):
    
    def __init__(self, *args, **kwargs):
        """Constructor"""
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []
        
    def showPage(self):
        """
        On a page break, add information to the list
        """
        self.pages.append(dict(self.__dict__))
        self._startPage()
        
    def save(self):
        """
        Add the page number to each page (page x of y)
        """
        page_count = len(self.pages)
    
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_page_number(page_count)
            canvas.Canvas.showPage(self)
    
        canvas.Canvas.save(self)
        
    def draw_page_number(self, page_count):
        """
        Add the page number
        """
        page = "Page %s of %s" % (self._pageNumber, page_count)
        self.setFont("Helvetica", 9)
        self.drawRightString(200*mm, 20*mm, page)