# header_logo.py

from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Flowable, Paragraph, Image

class Header(Flowable):

    def __init__(self, xml_data, logo=None, width=150, height=50):
        Flowable.__init__(self)
        self.xml_data = xml_data
        self.logo = logo
        self.width = width
        self.height = height
        self.styles = getSampleStyleSheet()

    def coord(self, x, y, unit=1):
        x, y = x * unit, self.height -  y * unit
        return x, y

    def draw(self):
        ptext = '<font size=10><b>Statement Date: {}' \
            '</b></font>'.format('01/01/2017')

        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height)
        p.drawOn(self.canv, *self.coord(110, 14, mm))

        ptext = '''<font size=10>
        <b>Member:</b> {member}<br/>
        <b>Member ID:</b> {member_id}<br/>
        <b>Group #:</b> {group_num}<br/>
        <b>Group name:</b> {group_name}<br/>
        </font>
        '''.format(member=self.xml_data.member_name,
                   member_id=self.xml_data.member_id,
                   group_num=self.xml_data.group_num,
                   group_name=self.xml_data.group_name
                   )
        p = Paragraph(ptext, self.styles["Normal"])
        p.wrapOn(self.canv, self.width, self.height)
        p.drawOn(self.canv, *self.coord(110, 35, mm))
        
        if self.logo:
            logo_obj = Image(self.logo, width=76.2, height=76.2)
            logo_obj.wrapOn(self.canv, self.width, self.height)
            logo_obj.drawOn(self.canv, *self.coord(15, 35, mm))