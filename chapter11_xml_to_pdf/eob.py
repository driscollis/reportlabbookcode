# eob.py

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
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

    def create_header(self):
        """"""
        pass

    def create_payment_summary(self):
        """"""
        pass

    def create_claims(self):
        """"""
        pass

    def save(self):
        """"""
        self.canvas.save()


def main(pdf_file):
    """"""
    eob = EOB(pdf_file)
    eob.save()


if __name__ == '__main__':
    pdf_file = 'eob.pdf'
    main(pdf_file)