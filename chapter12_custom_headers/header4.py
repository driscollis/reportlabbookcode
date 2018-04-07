# header4.py

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm

from reportlab.platypus import Paragraph


def header(canvas, doc):
    width, height = doc.pagesize
    
    styles = getSampleStyleSheet()
    
    ptext = '<font size=10><b>Statement Date: {}' \
        '</b></font>'.format('01/01/2017')
    
    p = Paragraph(ptext, styles["Normal"])
    p.wrapOn(canvas, width, height)
    p.drawOn(canvas, 400, 800)

    ptext = '''<font size=10>
    <b>Member:</b> {member}<br/>
    <b>Member ID:</b> {member_id}<br/>
    <b>Group #:</b> {group_num}<br/>
    <b>Group name:</b> {group_name}<br/>
    </font>
    '''.format(member=doc.xml.member_name,
               member_id=doc.xml.member_id,
               group_num=doc.xml.group_num,
               group_name=doc.xml.group_name
               )
    p = Paragraph(ptext, styles["Normal"])
    p.wrapOn(canvas, width, height)
    p.drawOn(canvas, 400, 730)
    
    # Add page number
    page_num = canvas.getPageNumber()
    text = "Page #%s" % page_num
    canvas.drawRightString(200*mm, 20*mm, text)