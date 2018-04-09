# form_letter.py

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def form_letter():
    doc = SimpleDocTemplate("form_letter.pdf",
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=72,
                            bottomMargin=18)
    flowables = []
    logo = "python_logo.png"
    magName = "Pythonista"
    issueNum = 12
    subPrice = "99.00"
    limitedDate = "03/05/2010"
    freeGift = "tin foil hat"

    formatted_time = time.ctime()
    full_name = "Mike Driscoll"
    address_parts = ["411 State St.", "Waterloo, IA 50158"]

    im = Image(logo, 2*inch, 2*inch)
    flowables.append(im)

    styles = getSampleStyleSheet()
    # Modify the Normal Style
    styles["Normal"].fontSize = 12
    styles["Normal"].leading = 14
    
    # Create a Justify style
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))    

    flowables.append(Paragraph(formatted_time, styles["Normal"]))
    flowables.append(Spacer(1, 12))

    # Create return address
    flowables.append(Paragraph(full_name, styles["Normal"]))
    for part in address_parts:
        flowables.append(Paragraph(part.strip(), styles["Normal"]))

    flowables.append(Spacer(1, 12))
    ptext = 'Dear {}:'.format(full_name.split()[0].strip())
    flowables.append(Paragraph(ptext, styles["Normal"]))
    flowables.append(Spacer(1, 12))

    ptext = '''
    We would like to welcome you to our subscriber
    base for {magName} Magazine! You will receive {issueNum} issues at
    the excellent introductory price of ${subPrice}. Please respond by
    {limitedDate} to start receiving your subscription and get the
    following free gift: {freeGift}.
    '''.format(magName=magName,
               issueNum=issueNum,
               subPrice=subPrice,
               limitedDate=limitedDate,
               freeGift=freeGift)
    flowables.append(Paragraph(ptext, styles["Justify"]))
    flowables.append(Spacer(1, 12))

    ptext = '''Thank you very much and we look
    forward to serving you.'''

    flowables.append(Paragraph(ptext, styles["Justify"]))
    flowables.append(Spacer(1, 12))
    ptext = 'Sincerely,'
    flowables.append(Paragraph(ptext, styles["Normal"]))
    flowables.append(Spacer(1, 48))
    ptext = 'Ima Sucker'
    flowables.append(Paragraph(ptext, styles["Normal"]))
    flowables.append(Spacer(1, 12))
    doc.build(flowables)

if __name__ == '__main__':
    form_letter()