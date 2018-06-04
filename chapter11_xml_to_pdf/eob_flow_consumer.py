# eob_flow_consumer.py

import os
import time

from lxml import objectify
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.platypus import Flowable, Indenter, Table, TableStyle


class Header(Flowable):

    def __init__(self, width=150, height=50):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.styles = getSampleStyleSheet()

    def coord(self, x, y, unit=1):
        x, y = x * unit, self.height -  y * unit
        return x, y

    def draw(self):
        ptext = '<font size=10><b>Statement Date: {}' \
                    '</b></font>'.format('01/01/2017')

        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height)
        p.drawOn(self.canv, *self.coord(110, 14, mm))

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
        p.wrapOn(self.canv, self.width, self.height)
        p.drawOn(self.canv, *self.coord(110, 35, mm))


class EOB:
    """
    Explanation of Benefits PDF Class
    """

    def __init__(self, xml_file, pdf_file='eob.pdf'):
        """"""
        if not os.path.exists(xml_file):
            raise RuntimeError('XML file ({}) does not exist!'.format(xml_file))

        self.xml = self.parse_xml(xml_file)

        self.doc = SimpleDocTemplate(
                        pdf_file, pagesize=letter,
                        rightMargin=72, leftMargin=36,
                        topMargin=36, bottomMargin=18)
        self.elements = []
        self.styles = getSampleStyleSheet()
        self.width, self.height = letter

    def parse_xml(self, xml_file):
        """"""
        with open(xml_file) as f:
            xml = f.read()

        root = objectify.fromstring(xml)
        return root

    def create_header(self):
        """"""
        header = Header()
        self.elements.append(header)
        self.elements.append(Spacer(1, 50))

    def create_text(self, text, size=8, bold=False):
        """"""
        if bold:
            return Paragraph('''<font size={size}><b>
            {text}</b></font>
            '''.format(size=size, text=text),
               self.styles['Normal'])

        return Paragraph('''<font size={size}>
        {text}</font>
        '''.format(size=size, text=text),
           self.styles['Normal'])

    def create_payment_summary(self):
        """"""
        ptext = '<font size=26>Your payment summary</font>'
        p = Paragraph(ptext, self.styles["Normal"])
        self.elements.append(p)
        self.elements.append(Spacer(1, 20))

        colWidths = [75, 125, 50, 125, 50, 150]
        
        data = [['', '', '', '', '', ''],
                [self.create_text('Patient', bold=True),
                 self.create_text('Provider', bold=True),
                 self.create_text('Amount', bold=True),
                 self.create_text('Sent to', bold=True),
                 self.create_text('Date', bold=True),
                 self.create_text('Amount', bold=True),
                 ]]
        self.elements.append(Indenter(left=60))
        table = Table(data, colWidths=colWidths)
        self.elements.append(table)
        self.elements.append(Indenter(left=-60))

    def create_claims(self):
        """"""
        fsize = 7.5

        ptext = '<font size=26>Your claims up close</font>'
        p = Paragraph(ptext, self.styles["Normal"])
        self.elements.append(p)
        self.elements.append(Spacer(1, 20))

        claim = Paragraph('''<font size={fsize}>
                Claim ID {claim_id}<br/>
                Received on {received_date}<br/></font>
                '''.format(fsize=fsize,
                           claim_id=self.xml.claim_id,
                           received_date=self.xml.received_date),
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
                     copay, remaining, plan_pays, coins, owe],
                    ]

        for claim in self.xml.claims.getchildren():
            data.append([
                self.create_text(claim.description),
                self.create_text(claim.amount_billed.text),
                self.create_text(claim.member_rate),
                self.create_text(claim.pending),
                self.create_text(claim.deductible),
                self.create_text(claim.copay),
                self.create_text(claim.amount_remaining.text),
                self.create_text(claim.plan_pays.text),
                self.create_text(claim.coinsurance),
                self.create_text(claim.total_owed.text)
            ])

        colWidths = [110, 50, 40, 60, 50, 40, 50, 40, 55, 60]
        table_style = TableStyle(
            [('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),  # Add grid to cells
             ('BOX', (0,0), (-1,-1), 0.25, colors.black),  # add outer border
             ('BACKGROUND', (1,0), (1, -1), colors.lightgoldenrodyellow),
             ('BACKGROUND', (7,0), (7, -1), colors.lightgoldenrodyellow)
             ])

        table = Table(data, colWidths=colWidths)
        table.setStyle(table_style)

        self.elements.append(Indenter(left=40))
        self.elements.append(table)
        self.elements.append(Indenter(left=-40))

    def create(self):
        """"""
        self.create_header()
        self.create_payment_summary()
        self.create_claims()
        self.save()

    def save(self):
        """"""
        self.doc.build(self.elements)


if __name__ == '__main__':
    eob = EOB(xml_file='eob.xml')
    eob.create()