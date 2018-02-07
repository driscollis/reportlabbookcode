# intra_paragraph_markup.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def intra_tags():
    doc = SimpleDocTemplate("intra_tags.pdf",
                            pagesize=letter
                            )
    styles = getSampleStyleSheet()

    flowables = []

    text = """
    This <b>text</b> is important,
    not <strong>strong</strong>.<br/><br/>

    A book title should be in <i>italics</i><br/><br/>

    You can also <u>underline</u> your text.<br/><br/>

    Bad text should be <strike>struck-through</strike>!<br/><br/>

    You can link to <a href="https://www.google.com" color="blue">Google</a>
    like this.
    """

    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)

    doc.build(flowables)

if __name__ == '__main__':
    intra_tags()