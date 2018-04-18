# image_exporter.py

import os
import subprocess

def image_exporter(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    cmd = ['pdfimages', '-all', pdf_path, 
           '{}/prefix'.format(output_dir)]
    subprocess.call(cmd)
    print('Images extracted:')
    print(os.listdir(output_dir))
    

if __name__ == '__main__':
    pdf_path = 'reportlab-sample.pdf'
    image_exporter(pdf_path, output_dir='images')