# image_demo.py

from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image, SimpleDocTemplate

def full_size_image():
    doc = SimpleDocTemplate("image_full_size.pdf", pagesize=letter)
    story = []

    img = Image("snakehead.jpg")
    story.append(img)
    doc.build(story)


def no_scaling():
    doc = SimpleDocTemplate("image_no_scaling.pdf", pagesize=letter)
    story = []

    img = Image("snakehead.jpg", width=50)
    story.append(img)
    doc.build(story)


if __name__ == '__main__':
    full_size_image()
    no_scaling()