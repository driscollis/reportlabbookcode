# scaler.py

from pdfrw import PdfReader, PdfWriter, PageMerge


def get4(srcpages):
    scale = 0.5
    srcpages = PageMerge() + srcpages
    x_increment, y_increment = (scale * i for i in srcpages.xobj_box[2:])
    for i, page in enumerate(srcpages):
        page.scale(scale)
        page.x = x_increment if i & 1 else 0
        page.y = 0 if i & 2 else y_increment
    return srcpages.render()


def scale_pdf(path, output):
    pages = PdfReader(path).pages
    writer = PdfWriter(output)
    scaled_pages = 4

    for i in range(0, len(pages), scaled_pages):
        four_pages = get4(pages[i: i + 4])
        writer.addpage(four_pages)

    writer.write()

if __name__ == '__main__':
    scale_pdf('reportlab-sample.pdf', 'four-page.pdf')