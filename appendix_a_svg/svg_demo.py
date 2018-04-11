# svg_demo.py

import os

from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg


def svg_demo(image_path, output_path):
    drawing = svg2rlg(image_path)
    renderPDF.drawToFile(drawing, output_path)
    fname = os.path.splitext(os.path.basename(image_path))[0]
    renderPM.drawToFile(drawing, '{}.png'.format(fname), 'PNG')


if __name__ == '__main__':
    svg_demo('snakehead.svg', 'svg_demo.pdf')
    