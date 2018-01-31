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
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=12>%s</font>' % formatted_time

    flowables.append(Paragraph(ptext, styles["Normal"]))
    flowables.append(Spacer(1, 12))

    # Create return address
    ptext = '<font size=12>%s</font>' % full_name
    flowables.append(Paragraph(ptext, styles["Normal"]))
    for part in address_parts:
        ptext = '<font size=12>%s</font>' % part.strip()
        flowables.append(Paragraph(ptext, styles["Normal"]))

    flowables.append(Spacer(1, 12))
    ptext = '<font size=12>Dear %s:</font>' % full_name.split()[0].strip()
    flowables.append(Paragraph(ptext, styles["Normal"]))
    flowables.append(Spacer(1, 12))

    ptext = '''
    <font size=12>We would like to welcome you to our subscriber
    base for {magName} Magazine! You will receive {issueNum} issues at
    the excellent introductory price of ${subPrice}. Please respond by
    {limitedDate} to start receiving your subscription and get the
    following free gift: {freeGift}.</font>
    '''.format(magName=magName,
               issueNum=issueNum,
               subPrice=subPrice,
               limitedDate=limitedDate,
               freeGift=freeGift)
    flowables.append(Paragraph(ptext, styles["Justify"]))
    flowables.append(Spacer(1, 12))

    ptext = '''<font size=12>Thank you very much and we look
    forward to serving you.</font>'''

    flowables.append(Paragraph(ptext, styles["Justify"]))
    flowables.append(Spacer(1, 12))
    ptext = '<font size=12>Sincerely,</font>'
    flowables.append(Paragraph(ptext, styles["Normal"]))
    flowables.append(Spacer(1, 48))
    ptext = '<font size=12>Ima Sucker</font>'
    flowables.append(Paragraph(ptext, styles["Normal"]))
    flowables.append(Spacer(1, 12))
    doc.build(flowables)

if __name__ == '__main__':
    form_letter()