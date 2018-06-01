# rotator.py

from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

def rotate_odd(path, output):
    reader = PdfReader(path)
    writer = PdfWriter()
    pages = reader.pages
    
    for page in range(len(pages)):
        if page % 2:
            pages[page].Rotate = 90
            writer.addpage(pages[page])
        
    writer.write(output)
    
if __name__ == '__main__':
    rotate_odd('reportlab-sample.pdf', 'rotate_odd.pdf')