# csv_exporter.py

import csv
import os

from miner_text_generator import extract_text_by_page


def export_as_csv(pdf_path, csv_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    
    counter = 1
    with open(csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for page in extract_text_by_page(pdf_path):
            text = page[0:100]
            words = text.split()
            writer.writerow(words)
            
        
if __name__ == '__main__':
    pdf_path = 'w9.pdf'
    csv_path = 'w9.csv'
    export_as_csv(pdf_path, csv_path)
