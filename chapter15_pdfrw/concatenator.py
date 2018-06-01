# concatenator.py

from pdfrw import PdfReader, PdfWriter, IndirectPdfDict

def concatenate(paths, output):
    writer = PdfWriter()
    
    for path in paths:
        reader = PdfReader(path)
        writer.addpages(reader.pages)
        
    writer.trailer.Info = IndirectPdfDict(
        Title='Combined PDF Title',
        Author='Michael Driscoll',
        Subject='PDF Combinations',
        Creator='The Concatenator'
    )
        
    writer.write(output)
    
if __name__ == '__main__':
    paths = ['reportlab-sample.pdf', 'w9.pdf']
    concatenate(paths, 'concatenate.pdf')