# svg_demo2.py

from reportlab.platypus import SimpleDocTemplate
from svglib.svglib import svg2rlg


def svg_demo(image_path, output_path):
    drawing = svg2rlg(image_path)
    
    doc = SimpleDocTemplate(output_path)
    
    story = []
    story.append(drawing)
    
    doc.build(story)

if __name__ == '__main__':
    svg_demo('Flag_of_Cuba.svg', 'svg_demo2.pdf')