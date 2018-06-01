# fill_by_overlay2.py

import PyPDF2
from reportlab.pdfgen import canvas


def create_overlay():
    """
    Create the data that will be overlayed on top
    of the form that we want to fill
    """
    c = canvas.Canvas('simple_form_overlay.pdf')
    
    c.drawString(115, 650, 'Mike')
    c.drawString(115, 600, 'Driscoll')
    c.drawString(115, 550, '123 Greenway Road')
    c.drawString(115, 500, 'Everytown')
    c.drawString(355, 500, 'IA')
    c.drawString(115, 450, '55555')
    
    c.save()
    
    
def merge_pdfs(form_pdf, overlay_pdf, output):
    """
    Merge the specified fillable form PDF with the 
    overlay PDF and save the output
    """
    form = PyPDF2.PdfFileReader(form_pdf)
    overlay = PyPDF2.PdfFileReader(overlay_pdf)
    pdf_writer = PyPDF2.PdfFileWriter()
    
    form_page_one = form.getPage(0)
    overlay_page_one = overlay.getPage(0)
    
    form_page_one.mergePage(overlay_page_one)
    pdf_writer.addPage(form_page_one)
        
    with open(output, 'wb') as fh:
        pdf_writer.write(fh)
    
if __name__ == '__main__':
    create_overlay()
    merge_pdfs('simple_form.pdf', 
               'simple_form_overlay.pdf', 
               'merged_form2.pdf')