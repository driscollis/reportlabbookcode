# paragraph_spacing.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def paragraph_spacing():
    doc = SimpleDocTemplate("paragraph_spacing.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()
    styles["Normal"].spaceBefore = 10
    styles["Normal"].spaceAfter = 10

    flowables = []

    text = """
    This <b>text</b> is important,
    not <strong>strong</strong>.
    """
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)    

    text = 'A book title should be in <i>italics</i>'
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)    

    text = 'You can also <u>underline</u> your text.'
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)    

    text = 'Bad text should be <strike>struck-through</strike>!'
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)    

    text = """
    You can link to <a href="https://www.google.com" color="blue">Google</a>
    like this.
    """
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    paragraph_spacing()