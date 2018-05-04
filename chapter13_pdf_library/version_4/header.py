# header.py

import os

from reportlab.platypus import Paragraph, Image
from util import get_stylesheet

def header(canvas, doc):
    width, height = doc.pagesize
    
    styles = get_stylesheet()
    
    if doc.logo_path:
        img = Image(doc.logo_path, width=76.2, height=76.2)
        img.wrapOn(canvas, width, height)
        img.drawOn(canvas, 100, 700)
    
    ptext = 'Statement Date: {}'.format('01/01/2017')
    p = Paragraph(ptext, styles["Bold"])
    p.wrapOn(canvas, width, height)
    p.drawOn(canvas, 400, 700)

    ptext = '''
    <b>Member:</b> {member}<br/>
    <b>Member ID:</b> {member_id}<br/>
    <b>Group #:</b> {group_num}<br/>
    <b>Group name:</b> {group_name}<br/>
    '''.format(member=doc.data.member_name,
               member_id=doc.data.member_id,
               group_num=doc.data.group_num,
               group_name=doc.data.group_name
               )
    p = Paragraph(ptext, styles["Normal"])
    p.wrapOn(canvas, width, height)
    p.drawOn(canvas, 400, 730)