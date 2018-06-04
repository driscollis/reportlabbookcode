# split_with_rl.py

from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

from reportlab.pdfgen.canvas import Canvas

def split(path, number_of_pages, output):
    pdf_obj = PdfReader(path)

    my_canvas = Canvas(output)

    # create page objects
    pages = pdf_obj.pages[0: number_of_pages]
    pages = [pagexobj(page) for page in pages]

    for page in pages:
        my_canvas.setPageSize((page.BBox[2], page.BBox[3]))
        my_canvas.doForm(makerl(my_canvas, page))
        my_canvas.showPage()

    # write the new PDF to disk
    my_canvas.save()


if __name__ == '__main__':
    split('reportlab-sample.pdf', 10, 'subset-rl.pdf')