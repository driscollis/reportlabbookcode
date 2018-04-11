# pdf_rotator.py

from PyPDF2 import PdfFileWriter, PdfFileReader

def rotator(path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)

    page1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page1)
    page2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page2)
    pdf_writer.addPage(pdf_reader.getPage(2))

    with open('pdf_rotator.pdf', 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == '__main__':
    rotator('reportlab-sample.pdf')