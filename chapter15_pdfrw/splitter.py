# splitter.py

from pdfrw import PdfReader, PdfWriter

def split(path, number_of_pages, output):
    pdf_obj = PdfReader(path)
    total_pages = len(pdf_obj.pages)
    
    writer = PdfWriter()
    
    for page in range(number_of_pages):
        if page <= total_pages:
            writer.addpage(pdf_obj.pages[page])
        
    writer.write(output)
    
if __name__ == '__main__':
    split('reportlab-sample.pdf', 10, 'subset.pdf')