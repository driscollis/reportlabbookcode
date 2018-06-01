# simple_table_html.py

from fpdf import FPDF, HTMLMixin

class HTML2PDF(FPDF, HTMLMixin):
    pass

def simple_table_html():
    pdf = HTML2PDF()
    
    table = """<table border="0" align="center" width="50%">
    <thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
    <tbody>
    <tr><td>cell 1</td><td>cell 2</td></tr>
    <tr><td>cell 2</td><td>cell 3</td></tr>
    </tbody>
    </table>"""
    
    pdf.add_page()
    pdf.write_html(table)
    pdf.output('simple_table_html.pdf')
    
if __name__ == '__main__':
    simple_table_html()