# reader.py

from pdfrw import PdfReader

def get_pdf_info(path):
    pdf = PdfReader(path)
    
    print(pdf.keys())
    print(pdf.Info)
    print(pdf.Root.keys())
    print('PDF has {} pages'.format(len(pdf.pages)))
    
if __name__ == '__main__':
    get_pdf_info('reportlab-sample.pdf')