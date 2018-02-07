# paragraph_scripting.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import reportlab.lib.colors

def paragraph_scripting():
    doc = SimpleDocTemplate("paragraph_scripting.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    ptext = "Einstein says: E = mc<super>2</super>"
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    flowables.append(Spacer(1, 15))

    ptext = "Reportlab <super rise=12>superscript</super> and <sub>subscript</sub>"
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)

    flowables.append(Spacer(1, 15))

    ptext = "Reportlab Greek letter e: <greek>e</greek>"
    para = Paragraph(ptext, style=styles["Normal"])
    flowables.append(para)


    doc.build(flowables)

if __name__ == '__main__':
    paragraph_scripting()