# scaled_image.py

from reportlab.lib import utils
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image, SimpleDocTemplate

def scaled_image(desired_width):
    doc = SimpleDocTemplate("image_with_scaling.pdf", pagesize=letter)
    story = []

    img = utils.ImageReader('snakehead.jpg')
    img_width, img_height = img.getSize()
    aspect = img_height / float(img_width)

    img = Image("snakehead.jpg",
                width=desired_width,
                height=(desired_width * aspect))
    img.hAlign = 'CENTER'
    story.append(img)
    doc.build(story)

if __name__ == '__main__':
    scaled_image(50)