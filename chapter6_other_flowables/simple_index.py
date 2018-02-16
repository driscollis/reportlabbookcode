# simple_index.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.platypus.tableofcontents import SimpleIndex
from reportlab.lib.styles import getSampleStyleSheet


def simple_index():
    doc = SimpleDocTemplate("simple_index.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    ptext = """I'm a custom <index item="bulletted"/>bulletted paragraph"""
    para = Paragraph(ptext, style=styles["Normal"], bulletText='-')
    flowables.append(para)
    flowables.append(PageBreak())

    ptext = """<index item="Python"/>Python is an indexed word"""
    para = Paragraph(ptext, style=styles["Normal"], bulletText='-')
    flowables.append(para)

    index = SimpleIndex()
    flowables.append(PageBreak())
    flowables.append(index)


    doc.build(flowables, canvasmaker=index.getCanvasMaker())

if __name__ == '__main__':
    simple_index()