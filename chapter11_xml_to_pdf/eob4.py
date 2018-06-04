# eob3.py

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.units import inch, mm


class EOB:
    """
    Explanation of Benefits PDF Class
    """

    def __init__(self, pdf_file):
        """"""
        self.canvas = canvas.Canvas(pdf_file, pagesize=letter)
        self.styles = getSampleStyleSheet()
        self.width, self.height = letter

    def coord(self, x, y, unit=1):
        x, y = x * unit, self.height -  y * unit
        return x, y

    def create_bold_text(self, text, size=8):
        """"""
        return Paragraph('''<font size={size}><b>
        {text}</b></font>
        '''.format(size=size, text=text),
           self.styles['Normal'])

    def create_header(self):
        """"""
        ptext = '<font size=10><b>Statement Date: {}' \
                '</b></font>'.format('01/01/2017')
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(self.canvas, self.width, self.height)
        p.drawOn(self.canvas, *self.coord(145, 17, mm))

        ptext = '''<font size=10>
            <b>Member:</b> {member}<br/>
            <b>Member ID:</b> {member_id}<br/>
            <b>Group #:</b> {group_num}<br/>
            <b>Group name:</b> {group_name}<br/>
            </font>
            '''.format(member='MIKE D',
                       member_id='X123456',
                       group_num=789456-1235,
                       group_name='PYTHON CORP'
                       )
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(self.canvas, self.width, self.height)
        p.drawOn(self.canvas, *self.coord(145, 35, mm))

    def create_payment_summary(self):
        """"""
        ptext = '<font size=26>Your payment summary</font>'
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(self.canvas, self.width, self.height)
        p.drawOn(self.canvas, *self.coord(15, 47, mm))

        colWidths = [75, 125, 50, 125, 50, 150]
        
        data = [['', '', '', '', '', ''],
                [self.create_bold_text('Patient'),
                 self.create_bold_text('Provider'),
                 self.create_bold_text('Amount'),
                 self.create_bold_text('Sent to'),
                 self.create_bold_text('Date'),
                 self.create_bold_text('Amount'),
                 ]]
        table = Table(data, colWidths=colWidths)
        table.wrapOn(self.canvas, self.width, self.height)
        table.drawOn(self.canvas, 20, 600)

    def create_claims(self):
        """"""
        fsize = 8

        ptext = '<font size=26>Your claims up close</font>'
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(self.canvas, self.width, self.height)
        p.drawOn(self.canvas, *self.coord(10, 100, mm))

        claim = Paragraph('''<font size={0}>
            Claim ID {1}<br/>
            Received on 12/12/16<br/></font>
            '''.format(fsize, 'ER123456789'),
               self.styles["Normal"])
        billed = Paragraph(
            '<font size={}>Amount<br/>billed</font>'.format(fsize),
            self.styles["Normal"])
        member_rate = Paragraph(
            '<font size={}>Member<br/>rate</font>'.format(fsize),
            self.styles["Normal"])
        pending = Paragraph(
            '<font size={}>Pending or<br/>not payable<br/>(Remarks)</font>'
            .format(fsize),
            self.styles["Normal"])
        applied = Paragraph(
            '<font size={}>Applied to<br/>deductible</font>'.format(fsize),
            self.styles["Normal"])
        copay = Paragraph(
            '<font size={}>Your<br/>copay</font>'.format(fsize),
            self.styles["Normal"])
        remaining = Paragraph(
            '<font size={}>Amount<br/>remaining</font>'.format(fsize),
            self.styles["Normal"])
        plan_pays = Paragraph(
            '<font size={}>Plan<br/>pays</font>'.format(fsize),
            self.styles["Normal"])
        coins = Paragraph(
            '<font size={}>Your<br/>coinsurance</font>'.format(fsize),
            self.styles["Normal"])
        owe = Paragraph(
            '<font size={}>You owe<br/>C+D+E+H=I</font>'.format(fsize),
            self.styles["Normal"])

        data = [[claim, billed, member_rate, pending, applied,
                 remaining, plan_pays, coins, owe],
                ]
        colWidths = [110, 50, 50, 60, 50, 50, 50, 70, 60]
        table = Table(data, colWidths=colWidths)
        table.wrapOn(self.canvas, self.width, self.height)
        table.drawOn(self.canvas, 20, 450)

    def save(self):
        """"""
        self.canvas.save()


def main(pdf_file):
    """"""
    eob = EOB(pdf_file)
    eob.create_header()
    eob.create_payment_summary()
    eob.create_claims()
    eob.save()


if __name__ == '__main__':
    pdf_file = 'eob4.pdf'
    main(pdf_file)