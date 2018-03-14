# encryption_demo.py

from reportlab.lib import pdfencrypt
from reportlab.pdfgen import canvas


def encryption_demo(userPassword, ownerPassword,
                    canPrint=1, canModify=1, canCopy=1, canAnnotate=1):
    encrypt = pdfencrypt.StandardEncryption(
        userPassword=userPassword,
        ownerPassword=ownerPassword,
        canPrint=canPrint,
        canModify=canModify,
        canCopy=canCopy,
        canAnnotate=canAnnotate,
        strength=40)

    my_canvas = canvas.Canvas('encryption_demo.pdf', encrypt=encrypt)

    my_canvas.drawString(20, 750, 'This is page one')

    my_canvas.save()


if __name__ == '__main__':
    encryption_demo(userPassword='bad_password',
                    ownerPassword='b3Tt3R_P@$$W0Rd')