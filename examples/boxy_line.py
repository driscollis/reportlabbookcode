from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import (Flowable, Paragraph,
                                SimpleDocTemplate, Spacer)

########################################################################
class BoxyLine(Flowable):
    """
    Draw a box + line + text

    -----------------------------------------
    | foobar |
    ---------

    """

    #----------------------------------------------------------------------
    def __init__(self, x=0, y=-15, width=40, height=15, text=""):
        Flowable.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.styles = getSampleStyleSheet()

    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y

    #----------------------------------------------------------------------
    def draw(self):
        """
        Draw the shape, text, etc
        """
        self.canv.rect(self.x, self.y, self.width, self.height)
        self.canv.line(self.x, 0, 500, 0)

        p = Paragraph(self.text, style=self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height)
        p.drawOn(self.canv, *self.coord(self.x+2, 10, mm))


doc = SimpleDocTemplate("test3.pdf",pagesize=letter)
story=[]

box = BoxyLine(text="foo")
story.append(box)
story.append(Spacer(0, 1*inch))
box = BoxyLine(text="bar")
story.append(box)

doc.build(story)