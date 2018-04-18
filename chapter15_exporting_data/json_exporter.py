# json_exporter.py

import json
import os

from miner_text_generator import extract_text_by_page


def export_as_json(pdf_path, json_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    data = {'Filename': filename}
    data['Pages'] = []
    
    counter = 1
    for page in extract_text_by_page(pdf_path):
        text = page[0:100]
        page = {'Page_{}'.format(counter): text}
        data['Pages'].append(page)
        counter += 1
    
    with open(json_path, 'w') as fh:
        json.dump(data, fh)

if __name__ == '__main__':
    pdf_path = 'w9.pdf'
    json_path = 'w9.json'
    export_as_json(pdf_path, json_path)