# boxy_line_demo.py

from boxy_line import BoxyLine
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.units import inch

def create_boxy_line_flowable():
    """
    Create a pdf
    """
    doc = SimpleDocTemplate("boxy_line_flowable.pdf",pagesize=letter)
    story=[]

    box = BoxyLine(text="foo")
    story.append(box)
    story.append(Spacer(0, 1*inch))
    box = BoxyLine(text="bar")
    story.append(box)

    doc.build(story)

if __name__ == "__main__":
    create_boxy_line_flowable()