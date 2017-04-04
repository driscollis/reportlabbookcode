import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image


class EOB:
    """
    EOB loosely based on AETNA example found here:
    https://ctmirror.org/2014/09/02/what-is-this-form-the-explanation-of-benefits/
    """

    #----------------------------------------------------------------------
    def __init__(self, pdf_file):
        """"""
        self.canvas = canvas.Canvas(pdf_file, pagesize=letter)
        self.styles = getSampleStyleSheet()
        self.width, self.height = letter

    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        x, y = x * unit, self.height -  y * unit
        return x, y

    #----------------------------------------------------------------------
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

        print


    #----------------------------------------------------------------------
    def create_payment_summary(self):
        """"""
        pass


    #----------------------------------------------------------------------
    def create_claims(self):
        """"""
        pass


    #----------------------------------------------------------------------
    def save(self):
        """"""
        self.canvas.save()


#----------------------------------------------------------------------
def main(pdf_file):
    """"""
    eob = EOB(pdf_file)
    eob.create_header()
    eob.save()


if __name__ == '__main__':
    pdf_file = "form_letter.pdf"
    main(pdf_file)