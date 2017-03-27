from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter

doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)

elements = []

data = [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]

t = Table(data)
elements.append(t)

doc.build(elements)