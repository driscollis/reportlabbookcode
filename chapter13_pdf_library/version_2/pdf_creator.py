# pdf_creator.py

from header import header
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Indenter, Paragraph, Spacer
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table, TableStyle

class EOB:
    """
    Explanation of Benefits PDF Class
    """

    def __init__(self, data, pdf_file='eob.pdf', logo=None):
        """"""
        self.data = data

        self.doc = SimpleDocTemplate(
                        pdf_file, pagesize=letter,
                        rightMargin=72, leftMargin=36,
                        topMargin=125, bottomMargin=18)
        self.doc.logo_path = logo
        self.doc.data = self.data
        
        self.elements = []
        self.styles = getSampleStyleSheet()
        self.width, self.height = letter
        self.create()
        
    def create(self):
        """
        Create the PDF
        """
        self.create_claims()
        
    def create_text(self, text, size=8, bold=False):
        """
        Create formatted Paragraphs
        """
        if bold:
            return Paragraph('''<font size={size}><b>
            {text}</b></font>
            '''.format(size=size, text=text),
               self.styles['Normal'])

        return Paragraph('''<font size={size}>
        {text}</font>
        '''.format(size=size, text=text),
           self.styles['Normal'])
    
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
                           claim_id=self.data.claim_id,
                           received_date=self.data.received_date),
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

        for claim in self.data.claims.getchildren():
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
        
    def save(self):
        """
        Save the PDF
        """
        self.doc.build(self.elements, onFirstPage=header)