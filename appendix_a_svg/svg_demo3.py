# svg_demo3.py

from reportlab.platypus import SimpleDocTemplate
from svglib.svglib import svg2rlg


def svg_demo(image_path, output_path):
    """
    Convert an SVG to a PDF
    """
    drawing = svg2rlg(image_path)

    doc = SimpleDocTemplate(output_path,
                            rightMargin=0,
                            leftMargin=0)

    story = []
    story.append(drawing)

    doc.build(story)

if __name__ == '__main__':
    svg_demo('snakehead.svg', 'svg_demo3.pdf')