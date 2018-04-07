# pdf_splitter.py

import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        for page in range(pdf.getNumPages()):
            output = PdfFileWriter()
            output.addPage(pdf.getPage(page))

            output_filename = '{}_page_{}.pdf'.format(
                fname, page+1)
            print('Created: {}'.format(output_filename))
            with open(output_filename, 'wb') as out:
                output.write(out)

if __name__ == '__main__':
    path = 'w9.pdf'
    pdf_splitter(path)