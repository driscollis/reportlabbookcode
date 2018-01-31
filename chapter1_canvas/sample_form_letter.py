# sample_form_letter.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_form(filename, date, amount, receiver):
    """
    @param date: The date to use
    @param amount: The amount owed
    @param receiver: The person who received the amount owed
    """
    my_canvas = canvas.Canvas(filename, pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 12)

    my_canvas.drawString(30, 750,'OFFICIAL COMMUNIQUE')
    my_canvas.drawString(30, 735,'OF ACME INDUSTRIES')

    my_canvas.drawString(500, 750, date)
    my_canvas.line(480, 747, 580, 747)

    my_canvas.drawString(275, 725,'AMOUNT OWED:')
    my_canvas.drawString(500, 725, amount)
    my_canvas.line(378,723, 580, 723)

    my_canvas.drawString(30, 703,'RECEIVED BY:')
    my_canvas.line(120, 700, 580, 700)
    my_canvas.drawString(120, 703, receiver)

    my_canvas.save()

if __name__ == '__main__':
    create_form('form.pdf', '01/23/2018',
                '$1,999', 'Mike')
