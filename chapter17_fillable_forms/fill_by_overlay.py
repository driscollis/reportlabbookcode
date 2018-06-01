# fill_by_overlay.py

import pdfrw
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
    form = pdfrw.PdfReader(form_pdf)
    olay = pdfrw.PdfReader(overlay_pdf)
    
    for form_page, overlay_page in zip(form.pages, olay.pages):
        merge_obj = pdfrw.PageMerge()
        overlay = merge_obj.add(overlay_page)[0]
        pdfrw.PageMerge(form_page).add(overlay).render()
        
    writer = pdfrw.PdfWriter()
    writer.write(output, form)
    
    
if __name__ == '__main__':
    create_overlay()
    merge_pdfs('simple_form.pdf', 
               'simple_form_overlay.pdf', 
               'merged_form.pdf')